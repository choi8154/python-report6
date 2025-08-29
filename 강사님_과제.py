from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get("https://search.daum.net/search?w=news&q=%EC%A3%A0%EC%8A%A4%EB%B0%94")

response.content

soup = BeautifulSoup(response.content,'lxml')

tage = soup.select('.tit-g a') 

len(tage)
tage[0].text.strip()

for i, tag in enumerate(tage):
    title = tag.text.strip()
    link = tag.get('href').strip()  
    print(f"{i + 1}. {title}")
    print(f"   링크: {link}")
    print("=" * 50)

