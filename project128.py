from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
print(page)

soup = bs(page.text,'html.parser')

starTable = soup.find_all('table')
print(len(starTable))

tempList= []
tableRows = starTable[4].find_all('tr')

for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)
print(tempList)


StarNames = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(tempList)):
    StarNames.append(tempList[i][0])
    Distance.append(tempList[i][0])
    Mass.append(tempList[i][0])
    Radius.append(tempList[i][0])

df2 = pd.DataFrame(list(zip(StarNames,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('project128_2.csv')