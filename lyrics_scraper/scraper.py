# libraries
from selenium import webdriver
import time
import pickle

# scraper
driver = webdriver.Firefox(executable_path = r'webdriver/geckodriver')

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
artists = []
for i in alph:
	letter = i.lower()
	url = 'https://www.azlyrics.com/' + letter + '.html'

	driver.get(url)

	non_artists = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Cookie Policy', 'Got it!', 'Submit Lyrics', 'Soundtracks', 'Facebook', 'Contact Us', 'Advertise Here', 'Privacy Policy', 'DMCA Policy']
	elems = driver.find_elements_by_tag_name('a')
	for elem in elems:
		# print("Hi")
		href = elem.get_attribute('innerHTML')
		if href is not None and href not in non_artists and '<img alt=' not in href:
			print(href)
			artists.append(href)

driver.close()

# # Pickle
filename =  'artists.pickle'
outfile = open(filename, 'wb')
pickle.dump(artists, outfile)
outfile.close()