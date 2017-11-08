from bs4 import BeautifulSoup
import requests,lxml, urllib2

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
	return BeautifulSoup(getPageData.text, 'lxml')


def get_link(url):
	soup = scrape(url)
	#from techcrunch
	my_titles = soup.findAll("h2", { "class" : "post-title" })
	for title in my_titles:
		links = title.a["href"]
		all_links.append(links)
		# print(links)

get_link(url[0])

def get_data(url):
	soup = scrape(url)	
	#getting article titles
	title = soup.find("div",class_="l-main").find('h1').get_text() #search title
	print title

	#getting article image links
	# myImgLinks = soup.find("div", {"class", "article-entry"})
	# for imgLink in myImgLinks:
	# 	# print(imgLink.img["src"])
	# 	img_links = imgLink.img["src"]
	# 	all_img_links.append(img_links)


	#getting article description
	for x in soup.find_all("div",class_="article-entry"):
		body= [y.get_text() for y in x.find_all("p")]
	print body

	print("done processing222")

print all_links[0]
get_data(all_links[0])

# for i in range(len(all_links)):
# 	get_data(all_links[i])

# print('title: ', all_title)
# print('links: ', all_links)
# print('imglinks: ', all_img_links)