
import requests
from bs4 import BeautifulSoup
import datetime

def visa_rate(to_curr):
    yyyymmdd = str(datetime.datetime.now())
    yyyy = yyyymmdd[:4]
    mm = yyyymmdd[5:7]
    dd = yyyymmdd[8:10]

    url0 ="https://usa.visa.com/support/consumer/travel-support/exchange-rate-calculator.html?amount=1&fee=2.0&utcConvertedDate=&exchangedate="
    url_date = mm+"%2F"+dd+"%2F"+yyyy
    url1 = "&fromCurr=JPY&toCurr="
    url2 = to_curr#USD,EUR,CNY,THB,HKG,TWD,SGD,KRW
    url3 = "&submitButton=Calculate+exchange+rate"

    html = requests.get(url0 + url_date + url1 + url2 + url3)
    soup = BeautifulSoup(html.content, "html.parser")

    det = 0
    for detail in soup.find_all(class_="converted-amount-value"):
        if det == 0:
            return float(detail.text[:6])
        det += 1


usd = []#empty list
eur = []#empty list
cny = []#empty list
krw = []#empty list

twd = []#empty list
thb = []#empty list
hkd = []#empty list
sgd = []#empty list

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

det = 0
table = soup.find(class_="tbright")
#print(table)
for detail in table.find_all("tr"):
    if det == 3:
        ret = detail.find_all(class_="bdt")
        twd.append(float(ret[2].text))
        #print(float(ret[2].text))
    if det == 4:
        ret = detail.find_all(class_="bdt")
        thb.append(float(ret[2].text))
    if det == 5:
        ret = detail.find_all(class_="bdt")
        hkd.append(float(ret[2].text))
    if det == 7:
        ret = detail.find_all(class_="bdt")
        sgd.append(float(ret[2].text))
    det += 1



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
        if det == 3:
            twd.append(float(detail.find(class_="cell-buy").text[:-1]))
        if det == 4:
            hkd.append(float(detail.find(class_="cell-buy").text[:-1]))
        if det == 5:
            krw.append(float(detail.find(class_="cell-buy").text[:-1]))
        if det == 9:
            thb.append(float(detail.find(class_="cell-buy").text[:-1]))
        if det == 10:
            sgd.append(float(detail.find(class_="cell-buy").text[:-1]))
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
    if det == 4:
        ret = detail.find(class_="rBox")
        hkd.append(float(ret.find("dt").text))
    if det == 5:
        ret = detail.find(class_="rBox")
        twd.append(float(ret.find("dt").text))
    if det == 10:
        ret = detail.find(class_="rBox")
        sgd.append(float(ret.find("dt").text))
    if det == 11:
        ret = detail.find(class_="rBox")
        thb.append(float(ret.find("dt").text))
    det += 1
    #print(detail.find("h3").text)
    #ret = detail.find(class_="rBox")
    #print(ret.find("dt").text)


usd.append(visa_rate("USD"))
eur.append(visa_rate("EUR"))
twd.append(visa_rate("TWD"))
cny.append(visa_rate("CNY"))
hkd.append(visa_rate("HKD"))
krw.append(visa_rate("KRW"))
thb.append(visa_rate("THB"))
sgd.append(visa_rate("SGD"))


with open("index_FM.html",'r',encoding="utf-8") as f:
    fileText = f.read()
    datetime.datetime.now()
    fileText = fileText.replace('datetime', str(datetime.datetime.now())[:16])
    if min(usd)==usd[0]:
        fileText = fileText.replace('USD[0]', "<b>"+"{:.2f}".format(usd[0])+"</b>")
    else:
        fileText = fileText.replace('USD[0]', "{:.2f}".format(usd[0]))
    if min(eur)==eur[0]:
        fileText = fileText.replace('EUR[0]', "<b>"+"{:.2f}".format(eur[0])+"</b>")
    else:
        fileText = fileText.replace('EUR[0]', "{:.2f}".format(eur[0]))
    if min(cny)==cny[0]:
        fileText = fileText.replace('CNY[0]', "<b>"+"{:.2f}".format(cny[0])+"</b>")
    else:
        fileText = fileText.replace('CNY[0]', "{:.2f}".format(cny[0]))
    if min(krw)==krw[0]:
        fileText = fileText.replace('KRW[0]', "<b>"+"{:.4f}".format(krw[0])+"</b>")
    else:
        fileText = fileText.replace('KRW[0]', "{:.4f}".format(krw[0]))
    if min(twd)==twd[0]:
        fileText = fileText.replace('TWD[0]', "<b>"+"{:.4f}".format(twd[0])+"</b>")
    else:
        fileText = fileText.replace('TWD[0]', "{:.4f}".format(twd[0]))
    if min(hkd)==hkd[0]:
        fileText = fileText.replace('HKD[0]', "<b>"+"{:.2f}".format(hkd[0])+"</b>")
    else:
        fileText = fileText.replace('HKD[0]', "{:.2f}".format(hkd[0]))
    if min(thb)==thb[0]:
        fileText = fileText.replace('THB[0]', "<b>"+"{:.4f}".format(thb[0])+"</b>")
    else:
        fileText = fileText.replace('THB[0]', "{:.4f}".format(thb[0]))
    if min(sgd)==sgd[0]:
        fileText = fileText.replace('SGD[0]', "<b>"+"{:.2f}".format(sgd[0])+"</b>")
    else:
        fileText = fileText.replace('SGD[0]', "{:.2f}".format(sgd[0]))


    if min(usd)==usd[1]:
        fileText = fileText.replace('USD[1]', "<b>"+"{:.2f}".format(usd[1])+"</b>")
    else:
        fileText = fileText.replace('USD[1]', "{:.2f}".format(usd[1]))
    if min(eur)==eur[1]:
        fileText = fileText.replace('EUR[1]', "<b>"+"{:.2f}".format(eur[1])+"</b>")
    else:
        fileText = fileText.replace('EUR[1]', "{:.2f}".format(eur[1]))
    if min(cny)==cny[1]:
        fileText = fileText.replace('CNY[1]', "<b>"+"{:.2f}".format(cny[1])+"</b>")
    else:
        fileText = fileText.replace('CNY[1]', "{:.2f}".format(cny[1]))
    if min(krw)==krw[1]:
        fileText = fileText.replace('KRW[1]', "<b>"+"{:.4f}".format(krw[1])+"</b>")
    else:
        fileText = fileText.replace('KRW[1]', "{:.4f}".format(krw[1]))
    if min(twd)==twd[1]:
        fileText = fileText.replace('TWD[1]', "<b>"+"{:.4f}".format(twd[1])+"</b>")
    else:
        fileText = fileText.replace('TWD[1]', "{:.4f}".format(twd[1]))
    if min(hkd)==hkd[1]:
        fileText = fileText.replace('HKD[1]', "<b>"+"{:.2f}".format(hkd[1])+"</b>")
    else:
        fileText = fileText.replace('HKD[1]', "{:.2f}".format(hkd[1]))
    if min(thb)==thb[1]:
        fileText = fileText.replace('THB[1]', "<b>"+"{:.4f}".format(thb[1])+"</b>")
    else:
        fileText = fileText.replace('THB[1]', "{:.4f}".format(thb[1]))
    if min(sgd)==sgd[1]:
        fileText = fileText.replace('SGD[1]', "<b>"+"{:.2f}".format(sgd[1])+"</b>")
    else:
        fileText = fileText.replace('SGD[1]', "{:.2f}".format(sgd[1]))


    if min(usd)==usd[2]:
        fileText = fileText.replace('USD[2]', "<b>"+"{:.2f}".format(usd[2])+"</b>")
    else:
        fileText = fileText.replace('USD[2]', "{:.2f}".format(usd[2]))
    if min(eur)==eur[2]:
        fileText = fileText.replace('EUR[2]', "<b>"+"{:.2f}".format(eur[2])+"</b>")
    else:
        fileText = fileText.replace('EUR[2]', "{:.2f}".format(eur[2]))
    if min(cny)==cny[2]:
        fileText = fileText.replace('CNY[2]', "<b>"+"{:.2f}".format(cny[2])+"</b>")
    else:
        fileText = fileText.replace('CNY[2]', "{:.2f}".format(cny[2]))
    if min(krw)==krw[2]:
        fileText = fileText.replace('KRW[2]', "<b>"+"{:.4f}".format(krw[2])+"</b>")
    else:
        fileText = fileText.replace('KRW[2]', "{:.4f}".format(krw[2]))
    if min(twd)==twd[2]:
        fileText = fileText.replace('TWD[2]', "<b>"+"{:.4f}".format(twd[2])+"</b>")
    else:
        fileText = fileText.replace('TWD[2]', "{:.4f}".format(twd[2]))
    if min(hkd)==hkd[2]:
        fileText = fileText.replace('HKD[2]', "<b>"+"{:.2f}".format(hkd[2])+"</b>")
    else:
        fileText = fileText.replace('HKD[2]', "{:.2f}".format(hkd[2]))
    if min(thb)==thb[2]:
        fileText = fileText.replace('THB[2]', "<b>"+"{:.4f}".format(thb[2])+"</b>")
    else:
        fileText = fileText.replace('THB[2]', "{:.4f}".format(thb[2]))
    if min(sgd)==sgd[2]:
        fileText = fileText.replace('SGD[2]', "<b>"+"{:.2f}".format(sgd[2])+"</b>")
    else:
        fileText = fileText.replace('SGD[2]', "{:.2f}".format(sgd[2]))


    if min(usd)==usd[3]:
        fileText = fileText.replace('USD[3]', "<b>"+"{:.2f}".format(usd[3])+"</b>")
    else:
        fileText = fileText.replace('USD[3]', "{:.2f}".format(usd[3]))
    if min(eur)==eur[3]:
        fileText = fileText.replace('EUR[3]', "<b>"+"{:.2f}".format(eur[3])+"</b>")
    else:
        fileText = fileText.replace('EUR[3]', "{:.2f}".format(eur[3]))
    if min(cny)==cny[3]:
        fileText = fileText.replace('CNY[3]', "<b>"+"{:.2f}".format(cny[3])+"</b>")
    else:
        fileText = fileText.replace('CNY[3]', "{:.2f}".format(cny[3]))
    if min(krw)==krw[3]:
        fileText = fileText.replace('KRW[3]', "<b>"+"{:.4f}".format(krw[3])+"</b>")
    else:
        fileText = fileText.replace('KRW[3]', "{:.4f}".format(krw[3]))
    if min(twd)==twd[3]:
        fileText = fileText.replace('TWD[3]', "<b>"+"{:.4f}".format(twd[3])+"</b>")
    else:
        fileText = fileText.replace('TWD[3]', "{:.4f}".format(twd[3]))
    if min(hkd)==hkd[3]:
        fileText = fileText.replace('HKD[3]', "<b>"+"{:.2f}".format(hkd[3])+"</b>")
    else:
        fileText = fileText.replace('HKD[3]', "{:.2f}".format(hkd[3]))
    if min(thb)==thb[3]:
        fileText = fileText.replace('THB[3]', "<b>"+"{:.4f}".format(thb[3])+"</b>")
    else:
        fileText = fileText.replace('THB[3]', "{:.4f}".format(thb[3]))
    if min(sgd)==sgd[3]:
        fileText = fileText.replace('SGD[3]', "<b>"+"{:.2f}".format(sgd[3])+"</b>")
    else:
        fileText = fileText.replace('SGD[3]', "{:.2f}".format(sgd[3]))


#print(fileText)
#f.close()#自動で閉じるから不要
with open("index.html",'w',encoding="utf-8") as f:
    f.write(fileText)
    #f.close()
   