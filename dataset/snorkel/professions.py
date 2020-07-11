# libraries
import json
from snorkel.labeling import labeling_function, PandasLFApplier
import pandas as pd 
import re

# professions
pf = open('prof_list.txt', 'r')
prof_list = []
for line in pf:
	prof_list.append(line.replace('\n', ''))

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
POS = 1
NEG = -1
ABSTAIN = 0

@labeling_function()
def lf1(x): # lf1 works
	text = x.values[0]
	patterns = ['i am a', 'im a', 'my profession is', 'i work as', 'my job is', 'my occupation is', 'i regret becoming a']
	neg = ['no', 'not', 'dont']
	
	for pattern in patterns:
		if pattern in text:
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
def lf2(x):
	# temporary filer code
	text = x.values[0]
	for i in pronouns:
		if i in text.split(' '):
			return POS

	return ABSTAIN


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

lfs = [lf1, lf2]

applier = PandasLFApplier(lfs=lfs)
y = applier.apply(df = ds)
print(len(y))

print(y)
lf1_coverage, lf2_coverage = (y != 0).mean(axis=0)
print(f"LF1 coverage: {lf1_coverage * 100:.1f}%")
print(f"LF2 coverage: {lf2_coverage * 100:.1f}%")

# for i in range(len(y)):
# 	if y[i][0] == 1 or y[i][0] == -1:
# 		print(dataset[i])

