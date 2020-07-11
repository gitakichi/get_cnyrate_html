
import requests
from bs4 import BeautifulSoup


usd = []#empty list
eur = []#empty list
cny = []#empty list
krw = []#empty list

#exchangers
html = requests.get("https://www.exchangers.co.jp/rate.php")
soup = BeautifulSoup(html.content, "html.parser")

det = 0
for detail in soup.find_all(class_="common-currency"):
    if det == 0:
        ret = detail.find_all(class_="bdt")
        usd.append(float(ret[2].text))
    if det == 1:
        ret = detail.find_all(class_="bdt")
        eur.append(float(ret[2].text))
    if det == 2:#人民元は3番目
        ret = detail.find_all(class_="bdt")
        #shop_a = float(ret[2].text)
        cny.append(float(ret[2].text))
    if det == 3:
        ret = detail.find_all(class_="bdt")
        krw.append(float(ret[2].text))
    det += 1
    #print(ret[1].text)
    #print(ret[2].text)


#D-ranger
html = requests.get("https://d-ranger.jp/shop/shinjuku/")
soup = BeautifulSoup(html.content, "html.parser")

det = 0
for detail in soup.find_all("tr"):
    if detail.find(scope="row"):
        if det == 0:
            usd.append(float(detail.find(class_="cell-buy").text[:-1]))
        if det == 1:
            eur.append(float(detail.find(class_="cell-buy").text[:-1]))
        if det == 2:#人民元は3番目
            #shop_b = float(detail.find(class_="cell-buy").text[:-1])
            cny.append(float(detail.find(class_="cell-buy").text[:-1]))
        if det == 5:
            krw.append(float(detail.find(class_="cell-buy").text[:-1]))
        det += 1
        #print(detail.find(class_="shoprate-name").text)
        #print(detail.find(class_="cell-buy").text)


#interbank
html = requests.get("https://www.interbank.co.jp/")
soup = BeautifulSoup(html.content, "html.parser")

det = 0
for detail in soup.find_all(class_="subBox"):
    if det == 0:
        ret = detail.find(class_="rBox")
        usd.append(float(ret.find("dt").text))
    if det == 1:
        ret = detail.find(class_="rBox")
        eur.append(float(ret.find("dt").text))
    if det == 2:#人民元は3番目
        ret = detail.find(class_="rBox")
        #shop_c = float(ret.find("dt").text)
        cny.append(float(ret.find("dt").text))
    if det == 3:
        ret = detail.find(class_="rBox")
        krw.append(float(ret.find("dt").text))
    det += 1
    #print(detail.find("h3").text)
    #ret = detail.find(class_="rBox")
    #print(ret.find("dt").text)


#print("Compare CNY cny\nExchangers:%.2f\nD-ranger:%.2f\nInterbank:%.2f"%(cny[0],cny[1],cny[2]))


import datetime
datetime.datetime.now()

#cny = [15.00,15.10,15.20]

with open("index_FM.html",'r',encoding="utf-8") as f:
    fileText = f.read()
    fileText = fileText.replace('datetime', str(datetime.datetime.now())[:16])
    fileText = fileText.replace('USD[0]', "{:.2f}".format(usd[0]))
    fileText = fileText.replace('EUR[0]', "{:.2f}".format(eur[0]))
    fileText = fileText.replace('CNY[0]', "{:.2f}".format(cny[0]))
    fileText = fileText.replace('KRW[0]', "{:.4f}".format(krw[0]))
    
    fileText = fileText.replace('USD[1]', "{:.2f}".format(usd[1]))
    fileText = fileText.replace('EUR[1]', "{:.2f}".format(eur[1]))
    fileText = fileText.replace('CNY[1]', "{:.2f}".format(cny[1]))
    fileText = fileText.replace('KRW[1]', "{:.4f}".format(krw[1]))
    
    fileText = fileText.replace('USD[2]', "{:.2f}".format(usd[2]))
    fileText = fileText.replace('EUR[2]', "{:.2f}".format(eur[2]))
    fileText = fileText.replace('CNY[2]', "{:.2f}".format(cny[2]))
    fileText = fileText.replace('KRW[2]', "{:.4f}".format(krw[2]))
    #print(fileText)
    #f.close()#自動で閉じるから不要
    with open("index.html",'w',encoding="utf-8") as f:
        f.write(fileText)
        #f.close()
    