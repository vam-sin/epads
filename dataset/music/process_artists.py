import pickle

infile = open('artists.pickle','rb')
artists = pickle.load(infile)
infile.close()

processed_artists = []
for i in artists:
	if ',' in i:
		# print(i)
		sp = i.split(',')
		# print(sp)
		# print(sp[1].replace(' ', ''), ' ', sp[0].replace(' ', ''))
		new = sp[1].replace(' ', '') + ' ' + sp[0].replace(' ', '')
		processed_artists.append(new)
	else:
		processed_artists.append(i)

filename =  'processed_artists.pickle'
outfile = open(filename, 'wb')
pickle.dump(artists, outfile)
outfile.close()