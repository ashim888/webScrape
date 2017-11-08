import bs4 as bs
import urllib.request
import re

url = ['https://techcrunch.com/', 'https://thenextweb.com/latest/', 'http://www.foxnews.com/']

all_title = []
all_links =[]
all_img_links = []
all_description = []

def get_link(url):
	i = 0

	getPageData = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(getPageData, 'lxml')

	#from techcrunch
	my_titles = soup.findAll("h2", { "class" : "post-title" })
	find_list_tag = soup.findAll("li", {"class": "river-block"})

	
	for d in soup.findAll('div', {'class': 'block-video-in-river'}):
		d.decompose()
	
	for title in my_titles:
		for link in title.findAll("a", href=True):
			links = title.a["href"]	
			all_links.append(links)
		i = i + 1
		if i == 10:
			break		

def get_data(url):
	description = ''
	getPageData = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(getPageData, 'lxml')
	
	#getting article titles
	my_title = soup.findAll("h1", {"class", "tweet-title"})
	for title in my_title:
		strTitle = title.string
		all_title.append(strTitle)
		# Testing
		# mainTitle = re.sub("\xa0"," ",strTitle)
		# all_title.append(mainTitle)
	


	#getting article image links
	myImgLinks = soup.find("div", {"class", "article-entry"}).findAll('img')
	for imgLink in myImgLinks:
		print(imgLink["src"])
		img_links = imgLink.img["src"]
		all_img_links.append(img_links)


	# getting article description
	
	# my_desc = soup.find("div", {"class", "article-entry"}).findAll('p')
	# for desc in my_desc:
	# 	new_desc = desc.text
	# 	description = description+'\n'+new_desc
		
		# Testing
		# print(new_desc,"\n")
		# all_description.append(desc.text);

	all_description.append(description)	

# Calling functions
get_link(url[0])
for i in range(len(all_links)):
	get_data(all_links[i])


# print('links: ', all_links)
print('title: ', all_title)
# for d in all_description:
# 	print('Desc: ', d)
print('imglinks: ', all_img_links)
