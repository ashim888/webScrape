import bs4 as bs
# import urllib.request
import re
import requests

url = ['https://techcrunch.com/', 'https://thenextweb.com/latest/', 'http://www.foxnews.com/']

all_title = []
all_links =[]
all_img_links = []
all_description = []

agents = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

def scrape(url):
	getPageData = requests.get(url,headers=agents)
	return bs.BeautifulSoup(getPageData.text, 'lxml')

def get_link(url):
	i = 0

	# getPageData = urllib.request.urlopen(url).read()
	# soup = bs.BeautifulSoup(getPageData, 'lxml')
	soup = scrape(url)

	# From techcrunch
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
	# description = ''
	# getPageData = urllib.request.urlopen(url).read()
	# soup = bs.BeautifulSoup(getPageData, 'lxml')
	soup = scrape(url)
	
	# getting article titles
	title = soup.find("div",class_="l-main").find('h1').get_text()
	print title
	# my_title = soup.findAll("h1", {"class", "tweet-title"})
	# for title in my_title:
	# 	strTitle = title.string
	# 	all_title.append(strTitle)
	
		# Testing
		# print (strTitle)
		# mainTitle = re.sub("\xa0"," ",strTitle)
		# all_title.append(mainTitle)
	


	#getting article image links
	myImgLinks = soup.find("div", {"class", "article-entry"}).findAll('img', {"class", ""})
	for image in myImgLinks:
		img_links = image["src"]
		all_img_links.append(img_links)
	
		# Testing
		# print(image["src"])


	# getting article description
	
	my_desc = soup.find("div", {"class", "article-entry"}).findAll('p')
	for x in soup.find_all("div",class_="article-entry"):
		body= [y.get_text() for y in x.find_all("p")]
		print body
	# for desc in my_desc:
	# 	new_desc = desc.text
	# 	description = description+'\n'+new_desc
		
		# Testing
		# print(new_desc,"\n")
		# all_description.append(desc.text);

	# all_description.append(description)	

# Calling functions
get_link(url[0])
# for i in range(len(all_links)):
	# get_data(all_links[i])
get_data(all_links[0])


print('links: ', all_links,"\n \n")
# print('title: ', all_title,"\n \n")
# for d in all_description:
# 	print('Desc: ', d,"\n \n")
print('imglinks: ', all_img_links)