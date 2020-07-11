# libraries
import json

# functions
def check_personal_pronouns(body):
	# I, me, my, mine and myself
	body = body.lower()
	body = body.split()
	# print(text)
	pronouns = ['i', 'me', 'my', 'mine', 'myself']
	if any(pr in body for pr in pronouns) and len(body)>=10 and len(body)<=40 and a:
		return True
	else:
		return False


# data
ds = open('../../data/RS_2011-02')

for i in ds:
	j = str(i)
	j = json.loads(j)
	# print(j)
	name = j['name']
	subreddit = j['subreddit']
	# author = j['author']
	body = j['selftext']
	if body != '' and check_personal_pronouns(body):
		print("Name: ", name, ", ", "Subreddit: ", subreddit)
		print("Body: ", body, "\n")


# print(ds)

'''Attributes:
downs
link_flair_text
distinguished
media
url
link_flair_css_class
id
edited
num_reports
created_utc
banned_by
name
subreddit
title
author_flair_text
is_self
author
media_embed
permalink
author_flair_css_class
selftext
domain
num_comments
likes
clicked
thumbnail
saved
subreddit_id
ups
approved_by
score
selftext_html
created
hidden
over_18

Conditions:
1. Containing a personal pronoun (except for 3rd person ones).
2. 10-40 words long
'''