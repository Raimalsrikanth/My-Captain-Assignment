import requests
from bs4 import Beautifulsoup

url='https://www.google.com/'

res=reuests.get(url).content


soup=Beautifulsoup(res,'lxml')
#print(soup.a.preetify())

#print(soup.a.text)
print(soup.script)