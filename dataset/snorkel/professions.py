# libraries
import json
from snorkel.labeling import labeling_function, PandasLFApplier, LabelingFunction
import pandas as pd 
import re
from empath import Empath

# professions
pf = open('prof_list.txt', 'r')
prof_list = []
for line in pf:
	prof_list.append(line.replace('\n', ''))

# empath lexicon
lexicon = Empath()
lexicon.create_category("prof0", [prof_list[0]], model="reddit", size = 300)
lexicon.create_category("prof1", [prof_list[1]], model="reddit", size = 300)
lexicon.create_category("prof2", [prof_list[2]], model="reddit", size = 300)
lexicon.create_category("prof3", [prof_list[3]], model="reddit", size = 300)
lexicon.create_category("prof4", [prof_list[4]], model="reddit", size = 300)
lexicon.create_category("prof5", [prof_list[5]], model="reddit", size = 300)
lexicon.create_category("prof6", [prof_list[6]], model="reddit", size = 300)
lexicon.create_category("prof7", [prof_list[7]], model="reddit", size = 300)
lexicon.create_category("prof8", [prof_list[8]], model="reddit", size = 300)
lexicon.create_category("prof9", [prof_list[9]], model="reddit", size = 300)
lexicon.create_category("prof10", [prof_list[10]], model="reddit", size = 300)
lexicon.create_category("prof11", [prof_list[11]], model="reddit", size = 300)
lexicon.create_category("prof12", [prof_list[12]], model="reddit", size = 300)
lexicon.create_category("prof13", [prof_list[13]], model="reddit", size = 300)
lexicon.create_category("prof14", [prof_list[14]], model="reddit", size = 300)
lexicon.create_category("prof15", [prof_list[15]], model="reddit", size = 300)
lexicon.create_category("prof16", [prof_list[16]], model="reddit", size = 300)
lexicon.create_category("prof17", [prof_list[17]], model="reddit", size = 300)
lexicon.create_category("prof18", [prof_list[18]], model="reddit", size = 300)
lexicon.create_category("prof19", [prof_list[19]], model="reddit", size = 300)
lexicon.create_category("prof20", [prof_list[20]], model="reddit", size = 300)
lexicon.create_category("prof21", [prof_list[21]], model="reddit", size = 300)
lexicon.create_category("prof22", [prof_list[22]], model="reddit", size = 300)
lexicon.create_category("prof23", [prof_list[23]], model="reddit", size = 300)
lexicon.create_category("prof24", [prof_list[24]], model="reddit", size = 300)
lexicon.create_category("prof25", [prof_list[25]], model="reddit", size = 300)
lexicon.create_category("prof26", [prof_list[26]], model="reddit", size = 300)
lexicon.create_category("prof27", [prof_list[27]], model="reddit", size = 300)
lexicon.create_category("prof28", [prof_list[28]], model="reddit", size = 300)
lexicon.create_category("prof29", [prof_list[29]], model="reddit", size = 300)
lexicon.create_category("prof30", [prof_list[30]], model="reddit", size = 300)
lexicon.create_category("prof31", [prof_list[31]], model="reddit", size = 300)
lexicon.create_category("prof32", [prof_list[32]], model="reddit", size = 300)
lexicon.create_category("prof33", [prof_list[33]], model="reddit", size = 300)
lexicon.create_category("prof34", [prof_list[34]], model="reddit", size = 300)
lexicon.create_category("prof35", [prof_list[35]], model="reddit", size = 300)
lexicon.create_category("prof36", [prof_list[36]], model="reddit", size = 300)
lexicon.create_category("prof37", [prof_list[37]], model="reddit", size = 300)
lexicon.create_category("prof38", [prof_list[38]], model="reddit", size = 300)
lexicon.create_category("prof39", [prof_list[39]], model="reddit", size = 300)
lexicon.create_category("prof40", [prof_list[40]], model="reddit", size = 300)
lexicon.create_category("prof41", [prof_list[41]], model="reddit", size = 300)
lexicon.create_category("prof42", [prof_list[42]], model="reddit", size = 300)

pronouns = ['i', 'me', 'my', 'mine', 'myself']
# print(prof_list)

# dataset prep functions
def check_personal_pronouns(body):
	# I, me, my, mine and myself
	body = body.lower()
	body = body.split()
	# print(text)
	if any(pr in body for pr in pronouns) and len(body)>=10 and len(body)<=40:
		return True
	else:
		return False

# labeling functions
lf1_patterns = ['i am a', 'im a', 'my profession is', 'i work as', 'my job is', 'my occupation is', 'i regret becoming a']
POS = 1
NEG = -1
ABSTAIN = 0

@labeling_function()
def lf1_0(x): # lf1 works
	text = x.values[0]
	neg = ['no', 'not', 'dont']

	if lf1_patterns[0] in text:
		for n in neg:
			if n in text.split(' '):
				for j in prof_list:
					if j in text.split(' '):
						return NEG
		
		for k in prof_list:
			if k in text.split(' '):
				return POS

	return ABSTAIN

@labeling_function()
def lf1_1(x): # lf1 works
	text = x.values[0]
	neg = ['no', 'not', 'dont']

	if lf1_patterns[1] in text:
		for n in neg:
			if n in text.split(' '):
				for j in prof_list:
					if j in text.split(' '):
						return NEG
		
		for k in prof_list:
			if k in text.split(' '):
				return POS

	return ABSTAIN

@labeling_function()
def lf1_2(x): # lf1 works
	text = x.values[0]
	neg = ['no', 'not', 'dont']

	if lf1_patterns[2] in text:
		for n in neg:
			if n in text.split(' '):
				for j in prof_list:
					if j in text.split(' '):
						return NEG
		
		for k in prof_list:
			if k in text.split(' '):
				return POS

	return ABSTAIN

@labeling_function()
def lf1_3(x): # lf1 works
	text = x.values[0]
	neg = ['no', 'not', 'dont']

	if lf1_patterns[3] in text:
		for n in neg:
			if n in text.split(' '):
				for j in prof_list:
					if j in text.split(' '):
						return NEG
		
		for k in prof_list:
			if k in text.split(' '):
				return POS

	return ABSTAIN

@labeling_function()
def lf1_4(x): # lf1 works
	text = x.values[0]
	neg = ['no', 'not', 'dont']

	if lf1_patterns[4] in text:
		for n in neg:
			if n in text.split(' '):
				for j in prof_list:
					if j in text.split(' '):
						return NEG
		
		for k in prof_list:
			if k in text.split(' '):
				return POS

	return ABSTAIN

@labeling_function()
def lf1_5(x): # lf1 works
	text = x.values[0]
	neg = ['no', 'not', 'dont']

	if lf1_patterns[5] in text:
		for n in neg:
			if n in text.split(' '):
				for j in prof_list:
					if j in text.split(' '):
						return NEG
		
		for k in prof_list:
			if k in text.split(' '):
				return POS

	return ABSTAIN

@labeling_function()
def lf1_6(x): # lf1 works
	text = x.values[0]
	neg = ['no', 'not', 'dont']

	if lf1_patterns[6] in text:
		for n in neg:
			if n in text.split(' '):
				for j in prof_list:
					if j in text.split(' '):
						return NEG
		
		for k in prof_list:
			if k in text.split(' '):
				return POS

	return ABSTAIN

def keyword_lookup(x, keywords, label):
    if any(word in x.values[0].lower() for word in keywords):
        return label
    return ABSTAIN

def lf2(keywords, label, attr_name):
    return LabelingFunction(
        name=f"keyword_lf2_{attr_name}",
        f=keyword_lookup,
        resources=dict(keywords=keywords, label=label),
    )

lf2_0 = lf2(keywords=lexicon.cats["prof0"], label=POS, attr_name="prof0")
lf2_1 = lf2(keywords=lexicon.cats["prof1"], label=POS, attr_name="prof1")
lf2_2 = lf2(keywords=lexicon.cats["prof2"], label=POS, attr_name="prof2")
lf2_3 = lf2(keywords=lexicon.cats["prof3"], label=POS, attr_name="prof3")
lf2_4 = lf2(keywords=lexicon.cats["prof4"], label=POS, attr_name="prof4")
lf2_5 = lf2(keywords=lexicon.cats["prof5"], label=POS, attr_name="prof5")
lf2_6 = lf2(keywords=lexicon.cats["prof6"], label=POS, attr_name="prof6")
lf2_7 = lf2(keywords=lexicon.cats["prof7"], label=POS, attr_name="prof7")
lf2_8 = lf2(keywords=lexicon.cats["prof8"], label=POS, attr_name="prof8")
lf2_9 = lf2(keywords=lexicon.cats["prof9"], label=POS, attr_name="prof9")
lf2_10 = lf2(keywords=lexicon.cats["prof10"], label=POS, attr_name="prof10")
lf2_11 = lf2(keywords=lexicon.cats["prof11"], label=POS, attr_name="prof11")
lf2_12 = lf2(keywords=lexicon.cats["prof12"], label=POS, attr_name="prof12")
lf2_13 = lf2(keywords=lexicon.cats["prof13"], label=POS, attr_name="prof13")
lf2_14 = lf2(keywords=lexicon.cats["prof14"], label=POS, attr_name="prof14")
lf2_15 = lf2(keywords=lexicon.cats["prof15"], label=POS, attr_name="prof15")
lf2_16 = lf2(keywords=lexicon.cats["prof16"], label=POS, attr_name="prof16")
lf2_17 = lf2(keywords=lexicon.cats["prof17"], label=POS, attr_name="prof17")
lf2_18 = lf2(keywords=lexicon.cats["prof18"], label=POS, attr_name="prof18")
lf2_19 = lf2(keywords=lexicon.cats["prof19"], label=POS, attr_name="prof19")
lf2_20 = lf2(keywords=lexicon.cats["prof20"], label=POS, attr_name="prof20")
lf2_21 = lf2(keywords=lexicon.cats["prof21"], label=POS, attr_name="prof21")
lf2_22 = lf2(keywords=lexicon.cats["prof22"], label=POS, attr_name="prof22")
lf2_23 = lf2(keywords=lexicon.cats["prof23"], label=POS, attr_name="prof23")
lf2_24 = lf2(keywords=lexicon.cats["prof24"], label=POS, attr_name="prof24")
lf2_25 = lf2(keywords=lexicon.cats["prof25"], label=POS, attr_name="prof25")
lf2_26 = lf2(keywords=lexicon.cats["prof26"], label=POS, attr_name="prof26")
lf2_27 = lf2(keywords=lexicon.cats["prof27"], label=POS, attr_name="prof27")
lf2_28 = lf2(keywords=lexicon.cats["prof28"], label=POS, attr_name="prof28")
lf2_29 = lf2(keywords=lexicon.cats["prof29"], label=POS, attr_name="prof29")
lf2_30 = lf2(keywords=lexicon.cats["prof30"], label=POS, attr_name="prof30")
lf2_31 = lf2(keywords=lexicon.cats["prof31"], label=POS, attr_name="prof31")
lf2_32 = lf2(keywords=lexicon.cats["prof32"], label=POS, attr_name="prof32")
lf2_33 = lf2(keywords=lexicon.cats["prof33"], label=POS, attr_name="prof33")
lf2_34 = lf2(keywords=lexicon.cats["prof34"], label=POS, attr_name="prof34")
lf2_35 = lf2(keywords=lexicon.cats["prof35"], label=POS, attr_name="prof35")
lf2_36 = lf2(keywords=lexicon.cats["prof36"], label=POS, attr_name="prof36")
lf2_37 = lf2(keywords=lexicon.cats["prof37"], label=POS, attr_name="prof37")
lf2_38 = lf2(keywords=lexicon.cats["prof38"], label=POS, attr_name="prof38")
lf2_39 = lf2(keywords=lexicon.cats["prof39"], label=POS, attr_name="prof39")
lf2_40 = lf2(keywords=lexicon.cats["prof40"], label=POS, attr_name="prof40")
lf2_41 = lf2(keywords=lexicon.cats["prof41"], label=POS, attr_name="prof41")
lf2_42 = lf2(keywords=lexicon.cats["prof42"], label=POS, attr_name="prof42")

# data
print("Dataset Preparation")
ds = open('../../../data/RS_v2_2010-12')

dataset = []

for i in ds:
	j = str(i)
	j = json.loads(j)
	# print(j)
	# name = j['name']
	subreddit = j['subreddit']
	# author = j['author']
	body = j['selftext']
	if body != '' and check_personal_pronouns(body):
		# print("Name: ", name, ", ", "Subreddit: ", subreddit)
		# print("Body: ", body, "\n")
		# lowercase and remove punctuation
		x = re.sub(r'[^\w\s]', '', body.lower())
		dataset.append(x)

# snorkel
print("Snorkel")
ds = pd.DataFrame(dataset)

lfs = [lf1_0, lf1_1, lf1_2, lf1_3, lf1_4, lf1_5, lf1_6, lf2_0, lf2_1, lf2_2, lf2_3, lf2_4, lf2_5, lf2_6, lf2_7, lf2_8, lf2_9, lf2_10, lf2_11, lf2_12, lf2_13, lf2_14, lf2_15, lf2_16, lf2_17, lf2_18, lf2_19, lf2_20, lf2_21, lf2_22, lf2_23, lf2_24, lf2_25, lf2_26, lf2_27, lf2_28, lf2_29, lf2_30, lf2_31, lf2_32, lf2_33, lf2_34, lf2_35, lf2_36, lf2_37, lf2_38, lf2_39, lf2_40, lf2_41, lf2_42]

applier = PandasLFApplier(lfs=lfs)
y = applier.apply(df = ds)
print(len(y))

print(y)
lf1_0_coverage, lf1_1_coverage, lf1_2_coverage, lf1_3_coverage, lf1_4_coverage, lf1_5_coverage, lf1_6_coverage, lf2_0_coverage, lf2_1_coverage, lf2_2_coverage, lf2_3_coverage, lf2_4_coverage, lf2_5_coverage, lf2_6_coverage, lf2_7_coverage, lf2_8_coverage, lf2_9_coverage, lf2_10_coverage, lf2_11_coverage, lf2_12_coverage, lf2_13_coverage, lf2_14_coverage, lf2_15_coverage, lf2_16_coverage, lf2_17_coverage, lf2_18_coverage, lf2_19_coverage, lf2_20_coverage, lf2_21_coverage, lf2_22_coverage, lf2_23_coverage, lf2_24_coverage, lf2_25_coverage, lf2_26_coverage, lf2_27_coverage, lf2_28_coverage, lf2_29_coverage, lf2_30_coverage, lf2_31_coverage, lf2_32_coverage, lf2_33_coverage, lf2_34_coverage, lf2_35_coverage, lf2_36_coverage, lf2_37_coverage, lf2_38_coverage, lf2_39_coverage, lf2_40_coverage, lf2_41_coverage, lf2_42_coverage = (y != 0).mean(axis=0)

# Results
print(f"LF1:0 coverage: {lf1_0_coverage * 100:.4f}%")
print(f"LF1:1 coverage: {lf1_1_coverage * 100:.4f}%")
print(f"LF1:2 coverage: {lf1_2_coverage * 100:.4f}%")
print(f"LF1:3 coverage: {lf1_3_coverage * 100:.4f}%")
print(f"LF1:4 coverage: {lf1_4_coverage * 100:.4f}%")
print(f"LF1:5 coverage: {lf1_5_coverage * 100:.4f}%")
print(f"LF1:6 coverage: {lf1_6_coverage * 100:.4f}%")

print(f"LF2:0 coverage: {lf2_0_coverage * 100:.4f}%")
print(f"LF2:1 coverage: {lf2_1_coverage * 100:.4f}%")
print(f"LF2:2 coverage: {lf2_2_coverage * 100:.4f}%")
print(f"LF2:3 coverage: {lf2_3_coverage * 100:.4f}%")
print(f"LF2:4 coverage: {lf2_4_coverage * 100:.4f}%")
print(f"LF2:5 coverage: {lf2_5_coverage * 100:.4f}%")
print(f"LF2:6 coverage: {lf2_6_coverage * 100:.4f}%")
print(f"LF2:7 coverage: {lf2_7_coverage * 100:.4f}%")
print(f"LF2:8 coverage: {lf2_8_coverage * 100:.4f}%")
print(f"LF2:9 coverage: {lf2_9_coverage * 100:.4f}%")
print(f"LF2:10 coverage: {lf2_10_coverage * 100:.4f}%")
print(f"LF2:11 coverage: {lf2_11_coverage * 100:.4f}%")
print(f"LF2:12 coverage: {lf2_12_coverage * 100:.4f}%")
print(f"LF2:13 coverage: {lf2_13_coverage * 100:.4f}%")
print(f"LF2:14 coverage: {lf2_14_coverage * 100:.4f}%")
print(f"LF2:15 coverage: {lf2_15_coverage * 100:.4f}%")
print(f"LF2:16 coverage: {lf2_16_coverage * 100:.4f}%")
print(f"LF2:17 coverage: {lf2_17_coverage * 100:.4f}%")
print(f"LF2:18 coverage: {lf2_18_coverage * 100:.4f}%")
print(f"LF2:19 coverage: {lf2_19_coverage * 100:.4f}%")
print(f"LF2:20 coverage: {lf2_20_coverage * 100:.4f}%")
print(f"LF2:21 coverage: {lf2_21_coverage * 100:.4f}%")
print(f"LF2:22 coverage: {lf2_22_coverage * 100:.4f}%")
print(f"LF2:23 coverage: {lf2_23_coverage * 100:.4f}%")
print(f"LF2:24 coverage: {lf2_24_coverage * 100:.4f}%")
print(f"LF2:25 coverage: {lf2_25_coverage * 100:.4f}%")
print(f"LF2:26 coverage: {lf2_26_coverage * 100:.4f}%")
print(f"LF2:27 coverage: {lf2_27_coverage * 100:.4f}%")
print(f"LF2:28 coverage: {lf2_28_coverage * 100:.4f}%")
print(f"LF2:29 coverage: {lf2_29_coverage * 100:.4f}%")
print(f"LF2:30 coverage: {lf2_30_coverage * 100:.4f}%")
print(f"LF2:31 coverage: {lf2_31_coverage * 100:.4f}%")
print(f"LF2:32 coverage: {lf2_32_coverage * 100:.4f}%")
print(f"LF2:33 coverage: {lf2_33_coverage * 100:.4f}%")
print(f"LF2:34 coverage: {lf2_34_coverage * 100:.4f}%")
print(f"LF2:35 coverage: {lf2_35_coverage * 100:.4f}%")
print(f"LF2:36 coverage: {lf2_36_coverage * 100:.4f}%")
print(f"LF2:37 coverage: {lf2_37_coverage * 100:.4f}%")
print(f"LF2:38 coverage: {lf2_38_coverage * 100:.4f}%")
print(f"LF2:39 coverage: {lf2_39_coverage * 100:.4f}%")
print(f"LF2:40 coverage: {lf2_40_coverage * 100:.4f}%")
print(f"LF2:41 coverage: {lf2_41_coverage * 100:.4f}%")
print(f"LF2:42 coverage: {lf2_42_coverage * 100:.4f}%")


# for i in range(len(y)):
# 	if y[i][0] == 1 or y[i][0] == -1:
# 		print(dataset[i])

