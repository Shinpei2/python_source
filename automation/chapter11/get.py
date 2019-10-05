import bs4, requests

infile = open('example.html')
soup = bs4.BeautifulSoup(infile, 'lxml')
p_li = soup.select('.slogan')
for item in p_li:
    print(item)