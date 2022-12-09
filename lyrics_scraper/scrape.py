from selenium import webdriver
from bs4 import BeautifulSoup

# double check non-english songs manually

year = "2022"
country = "estonia"

url = 'https://eurovisionworld.com/eurovision/' + year + '/' + country

driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
div = soup.find('div', {'class': 'lyrics_div_wrap mm'})

love_mentions = 0

for p in div.find_all('p'):
    p = str(p)
    p = p.replace("<p>", "").replace("</p>", "")
    p = p.split("<br/>")
    
    for line in p:
        line = line.lower()
        words = line.split(" ")
        
        for word in words:
            for symbol in [",", ".", ";", "?", "!", "-", "=", '"']:
                if symbol in word:
                    word = word.replace(symbol, "")
                
            if word == "love" or word == "loving" or "love" in word:
                love_mentions += 1

print(f"{country} - {love_mentions}")

driver.close()
