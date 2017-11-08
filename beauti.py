import bs4 as bs
import urllib.request
import re

url = ['https://techcrunch.com/', 'https://thenextweb.com/latest/', 'http://www.foxnews.com/']

all_title = []
all_links =[]
all_img_links = []
all_description = []

def get_link(url):
	getPageData = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(getPageData, 'lxml')

	#from techcrunch
	my_titles = soup.findAll("h2", { "class" : "post-title" })
	for title in my_titles:
		links = title.a["href"]
		all_links.append(links)
		print(links)

	# #from thenextweeb
	# gettitles = soup.findAll("h4", { "class" : "story-title" })
	# # mytitles = gettitles.findAll("a")
	# for title in range(gettitles):
	# 	# print(title.a.string)
	# 	link = title.a['href']
	# 	links.append(link)

	# # for link in links[:]:
	# # 	print("link: ", links)
	# 	print(links)		


get_link(url[0])

def get_data(url):
	getPageData = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(getPageData, 'lxml')
	
	#getting article titles
	my_title = soup.findAll("h1", {"class", "tweet-title"})
	for title in my_title:
		# strTitle = title.string
		# mainTitle = re.sub("\xa0"," ",strTitle)
		# all_title.append(mainTitle)
		# print(title.string)
		all_title.append(title.string)

	#getting article image links
	# myImgLinks = soup.find("div", {"class", "article-entry"})
	# for imgLink in myImgLinks:
	# 	# print(imgLink.img["src"])
	# 	img_links = imgLink.img["src"]
	# 	all_img_links.append(img_links)


	#getting article description
	my_desc = soup.find("div", {"class", "article-entry"}).findAll('p')
	for desc in my_desc:
		print(desc.string)

	print("done processing222")
for i in range(len(all_links)):
	get_data(all_links[i])

print('title: ', all_title)
print('links: ', all_links)
print('imglinks: ', all_img_links)