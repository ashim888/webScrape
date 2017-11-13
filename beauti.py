import bs4 as bs
import re
import requests
import requests, lxml

url = ['https://techcrunch.com/', 'https://thenextweb.com/latest/', 'http://www.foxnews.com/']

allTitle = []
allLinks =[]
allImgLinks = []
allDescription = []

agents = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

def scrape(url):
	getPageData = requests.get(url,headers=agents)
	return bs.BeautifulSoup(getPageData.text, 'lxml')

def get_link(url):
	i = 0
	soup = scrape(url)	
	# From techcrunch
	myTitles = soup.findAll("h2", { "class" : "post-title" })
	
	# Deleting the video news from data 
	for d in soup.findAll('div', {'class': 'block-video-in-river'}):
		d.decompose()
	
	# Extracting links 
	for title in myTitles:
		for link in title.findAll("a", href=True):
			links = title.a["href"]	
			allLinks.append(links)
		i = i + 1
		if i == 10:
			break		

def get_data(url):
	soup = scrape(url)
	
	# getting article titles
	title = soup.find("div",class_="l-main").find('h1').text
	print title
	description = ''
	
	#getting article image links
	myImgLinks = soup.find("div", {"class", "article-entry"}).findAll('img', {"class", ""})
	for image in myImgLinks:
		imgLinks = image["src"]
		allImgLinks.append(imgLinks)

	# getting article description
	
	my_desc = soup.find("div", {"class", "article-entry"}).findAll('p')
	for x in soup.find_all("div",class_="article-entry"):
		body= [y.get_text() for y in x.find_all("p")]
		print body
	
	# for desc in soup.find("div", {"class", "article-entry"}).findAll('p'):
	# 	newDesc = desc.text
	# 	description = description+'\n'+newDesc

	# allDescription.append(description)	
	
# Calling functions
get_link(url[0])
# for i in range(len(all_links)):
	# get_data(all_links[i])
get_data(allLinks[0])


print('links: ', allLinks,"\n \n")
# print('title: ', all_title,"\n \n")
# for d in all_description:
# 	print('Desc: ', d,"\n \n")
print('imglinks: ', allImgLinks)


# Calling functions
get_link(url[0])
for i in range(len(allLinks)):
	get_data(allLinks[i])

