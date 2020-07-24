# libraries
import json
from snorkel.labeling import PandasLFApplier, filter_unlabeled_dataframe, labeling_function, LFAnalysis, LabelingFunction
from snorkel.labeling.model import LabelModel
import pandas as pd 
import string
import re
import sys
import time
import tqdm
from empath import Empath
from collections import defaultdict

patterns = ["i am a", "i am an", "i'm an", "i'm a", "my profession", "i work as", "my job", "my occupation", "i regret becoming"]

ABSTAIN = -1
NEG = 0
POS = 1

hobby_to_syn = eval(open("prof_syn.txt").read())
syn_to_hob = dict((syn, val) for val, syns in hobby_to_syn.items() for syn in syns)
syn_list = list(syn_to_hob.keys())

# LF
def pattern_match(x, keyword, context_len = 3, with_period = False):
    txt_punct = x.values[0]
    txt = x.values[0]
    txt = txt.translate(str.maketrans('', '', string.punctuation.replace("'", ""))).lower()
    txt = " " + txt + " "
    txt_punct = " " + txt_punct.strip() + ". "
    left_cont = " " + " ".join(txt.strip().split(' ')[min(0, - context_len - len(keyword.split(" "))):]) + " "
    split_left_cont = left_cont.strip().split(" ")
    if len(split_left_cont) > 2:
        if split_left_cont[-1] == "and" and split_left_cont[-2] in syn_list:
            left_cont = " " + " ".join(split_left_cont[:-2]) + " "
    pos_kw = left_cont.find(" " + keyword + " ")
    pos_not = min(y for y in [left_cont.find(" not "), left_cont.find("don't"), left_cont.find(" no "), sys.maxsize] if y != -1)
    if pos_kw < pos_not and pos_not != sys.maxsize:
        if any(y in left_cont[pos_not:] for y in [" your ", " his ", " her ", " their ", " the ", " this ", " that "]) and keyword in ["i am a", "i am an", "i'm an", "i'm a"]:
            return POS
        return NEG

    return ABSTAIN

def make_keyword_lf(keyword, context_len, with_period):
    return LabelingFunction(
        name="pattern_%s_%s%s" % (keyword, "context:%d" % context_len, "_period" if with_period else ""),
        f=pattern_match,
        resources=dict(keyword=keyword, with_period=with_period, context_len=context_len),
    )

@labeling_function()
def job_inpost(x):
	txt = x.values[0].lower()
	job_synonyms = ["profession", "job", "career", "occupation", "duty", "position", "speciality", "employment"]

	return POS if any([y in txt.lower() for y in job_synonyms]) else ABSTAIN

@labeling_function()
def check_iama(x):
	txt = x.values[0]
	txt = txt.translate(str.maketrans('', '', string.punctuation.replace("'", ""))).lower()
	txt = " " + txt + " "
	if any(y in txt for y in ["i am a", "i am an", "i'm an", "i'm a"]):
	    return POS
	return ABSTAIN

def label_post(ds, prefix = ""):
	lfs = [job_inpost, check_iama]

	context_lens = [100, 3, 2]
	for with_per in [True, False]:
		for clen in context_lens:
		    for kw in patterns:
		        lfs.append(make_keyword_lf(keyword=kw, context_len=clen, with_period=with_per))

	print("created lfs, their count", len(lfs))

	df_train = ds

	print("loaded dataset")

	t1 = time.time()
	# with tqdm(desc="Dask Apply"):
	applier = PandasLFApplier(lfs=lfs)
	L_train = applier.apply(df=ds)
	print("time mins ", (time.time() - t1) / 60)

	print(LFAnalysis(L=L_train, lfs=lfs).lf_summary())

	df_l_train = pd.DataFrame(L_train, columns=[str(x).split(",")[0] for x in lfs])
	print(df_train.shape)
	print(df_l_train.shape)
	df_train = pd.concat([df_train.reset_index(), df_l_train], axis=1)
	print(df_train.shape)
	print("*************************************************")
	df_train = df_train.drop(["index"], axis=1)

	label_model = LabelModel(cardinality=2, verbose=True)
	label_model.fit(L_train=L_train, n_epochs=1000, lr=0.001, log_freq=100, seed=123)
	probs_train = label_model.predict_proba(L=L_train)

	df_train_filtered, probs_train_filtered = filter_unlabeled_dataframe(
	X=df_train, y=probs_train, L=L_train
	)

	probs_df = pd.DataFrame(probs_train_filtered, columns=["neg_prob", "pos_prob"])
	print(df_train_filtered.shape)
	print(probs_df.shape)
	df_train_filtered = pd.concat([df_train_filtered.reset_index(), probs_df], axis=1)
	print(df_train_filtered.shape)

	df_train_filtered.to_pickle(prefix + ".pkl")
	df_train_filtered.to_csv(prefix + ".csv")
	verbose = True
	if verbose:
		for i in range(len(lfs)):
		    ppath = prefix + str(lfs[i]).split(",")[0] + ".csv"
		    df_train.iloc[L_train[:, i] != ABSTAIN].to_csv(ppath)

# data
print("Dataset Preparation")
ds = open('../../../data/RS_v2_2010-12')

dataset = []
for i in ds:
	j = str(i)
	j = json.loads(j)
	body = j['selftext']
	if body != '':
		dataset.append(body)


dataset = pd.DataFrame(dataset)
label_post(dataset, "output/trial")