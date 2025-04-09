import requests
from bs4 import BeautifulSoup
import datetime

url = "https://pixelford.com/blog/"

requests.get(url)
response = requests.get(url, headers={'user-agent': 'whereyouwrite_newuseragent_name'})
html = (response.content)
soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article',class_='type-post')

for blog in blogs:
    title= blog.find('a', class_="entry-title-link").get_text()

    blog_datetime_string= blog.find('time', class_="entry-time").get('datetime')
    blog_datetime= datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date =blog_datetime.strftime("%b,%d,%Y")


    print(f"{pretty_date},{title}")



#print(requests.utils.default_headers())
#Run into 403 Forbidden error due to the website blocking the request
#response = requests.get(url, headers={'user-agent': 'whereyouwrite_newuseragent_name'})
#Can find the user-agent in the browser dev tools>Network>Headers>User-Agent Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
