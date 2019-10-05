import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json 



url = 'https://coinmarketcap.com/'

page = requests.get(url)
#print(page.status_code)
#print(page.text)
#for i in range(100):
# with open(r"C:\Users\hp\Desktop\currencys1_Data.csv",'w') as csvfile:
#     fieldnamessss = ['Name','Market_cap','Price','Valume','Circulating_supply']
#     writer = csv.DictWriter(csvfile,fieldnames = fieldnamessss)
#     writer.writeheader()


soup = BeautifulSoup(page.text, 'html.parser')

#print(soup.encode('utf-8'))
names=soup.find_all("a", class_="currency-name-container link-secondary")
for name in names:
    name=name.text.strip()
    s1 = pd.Series([name])           # Define series 1 
    #print(name)
    x={
        "name":name
    }
    print(json.dumps(x))




market_caps = soup.find_all("td", class_="no-wrap market-cap text-right")
for market_cap in market_caps:
    market_cap=market_cap.text.strip()
    s2 = pd.Series([market_cap]) # Define series 2 
    #print(market_cap)
    y={
        "market_cap":market_cap
    }
    print(json.dumps(y))



prices=soup.find_all("a", class_="price")
for price in prices:
    price=price.text.strip()
    s3 = pd.Series([price])
    #print(price)
    z={
        "price":price
    }
    print(json.dumps(z))


valumes=soup.find_all("a", class_="volume")
for valume in valumes:
    valume=valume.text.strip()
    s4 = pd.Series([valume])
    #print(valume)
    w={
        "valume":valume
    }
    print(json.dumps(w))

circulating_supplys=soup.find_all("td", class_="no-wrap text-right circulating-supply")
for circulating_supply in circulating_supplys:
    circulating_supply=circulating_supply.text.strip()
    s5 = pd.Series([circulating_supply])     # Define series 3 
    #print(circulating_supply)
    t={
        "circulating_supply":circulating_supply
    }
    print(json.dumps(t))

Data ={'Name':s1, 'Market_cap':s2, 'Price':s3,'Valume':s4,'Circulating_supply':s5} # Define Data 
dfseries = pd.DataFrame(Data) 
print(dfseries)  

my_details={'x':x,
            'y':y,
            'z':z,
            'w':w,
            't':t
            }

with open('personal.json', 'w') as json_file:

    json.dump(my_details, json_file)



    #writer.writerow({'Name':name,'Market_cap':market_cap,'Price':price,'Valume': valume,'Circulating_supply':circulating_supply})

    #writer.writerow({'Name':name,'Market_cap':market_cap,'Price':price,'Valume': valume,'Circulating_supply':circulating_supply})

    





