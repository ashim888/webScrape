from bs4 import BeautifulSoup 
import requests, lxml, urllib3

url = ['https://techcrunch.com/', 'https://thenextweb.com/latest/', 'http://www.foxnews.com/']

allTitle = []
allLinks =[]
allImgLinks = []
allDescription = []

agents = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def scrape(url):
	getPageData = requests.get(url, headers=agents)
	return BeautifulSoup(getPageData.text, 'lxml')

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
	description = ''
	soup = scrape(url)
	
	# getting article titles
	my_title = soup.findAll("h1", {"class", "tweet-title"})
	for title in my_title:
		strTitle = title.string
		allTitle.append(strTitle)

	#getting article image links
	myImgLinks = soup.find("div", {"class", "article-entry"}).findAll('img', {"class", ""})
	for image in myImgLinks:
		imgLinks = image["src"]
		allImgLinks.append(imgLinks)

	# getting article description
	for desc in soup.find("div", {"class", "article-entry"}).findAll('p'):
		newDesc = desc.text
		description = description+'\n'+newDesc

	allDescription.append(description)	

# Calling functions
get_link(url[0])
for i in range(len(allLinks)):
	get_data(allLinks[i])


# print('links: ', allLinks,"\n \n")
# print('title: ', allTitle,"\n \n")
# for d in allDescription:
# 	print('Desc: ', d,"\n \n")
# print("desc: ", allDescription,"\n \n")
# for i in allImgLinks:
# 	print('imglink: ', i)
