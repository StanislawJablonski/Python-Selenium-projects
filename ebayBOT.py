import requests
from bs4 import BeautifulSoup
import csv

def get_page(url):
	response = requests.get(url)
	print(response.ok)
	print(response.status_code)

	if not response.ok:
		print("Server responded", response.status_code)
	else:
		soup = BeautifulSoup(response.text, 'lxml')
	return soup

def get_detail_data(soup):
	#title
	#price
	#items sold

	try:
		title = soup.find('h1', id='itemTitle').text.replace('\xa0','')
	except:
		title = ''

	try:
		#price = soup.find('span', id = "prcIsum").get("content")
		p = soup.find('span', id = "prcIsum").text.strip()
		currency, price = p.split(' ')
	except:
		price = ''
		currency = ''

	try:
		sold = soup.find('span', class_ = 'vi-qtyS-hot-red').find('a', class_='vi-txt-underline').text.strip().split(' ')[0]
	except:
		sold = ''
	
	data = {'title': title, 'price': price, 'currency': currency, 'total sold': sold}
	print(data)
	return(data)


def get_index_data(soup):
	try:
		links = soup.find_all('a', class_='s-item__link')
	except:
		links = []

	urls = [item.get('href') for item in links]
	return urls

def write_csv(data, url):
	with open('ourput.csv', 'a') as csvfile:
		writer  = csv.writer(csvfile)
		row = [data['title'],data['price'],data['currency'],data['total sold'],url]
		writer.writerow(row)


def main():
	url = 'https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn=1'
	
	products = get_index_data(get_page(url))

	for link in products:
		data = get_detail_data(get_page(link))
		write_csv(data, link)


main()



#if __name__ == '__main__':
#	main()