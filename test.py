from bs4 import BeautifulSoup
import requests

def mnen(list_stock):
    # df = None
    # for x in list_stock:
    data = {}
    html = requests.get('https://altmanzscoreplus.com/articles/AltmanZScorePlus_SPWH_Sportsmans_Warehouse_Holdings_Inc.html', headers={'USER-AGENT': "Mozilla/5.0"})
    html = BeautifulSoup(html.text, 'html.parser')
    print(html)
    soup = html.find_all()
    title = html.find_all(attrs={'class':'ui-datatable ui-widget'})
    print(title)
    #     colum_2 = html.find_all(attrs={'data-test':'fin-col'})
    #     n = 1
    #     n_data = 0
    #     c = 0
    #     data['Stock']= x
    #     for i in title:
    #         list_price = []
    #         for j in colum_2:
    #             if n < 6:
    #                list_price.append(float(colum_2[n_data].text.replace(',','').replace('-','0')))
    #             else:
    #                 n = 1
    #                 break
    #             n += 1
    #             n_data += 1
    #         data[i.text] = list_price
    #     if df is None:
    #         df = pd.DataFrame(data)
    #     else:
    #         df = pd.concat([df, pd.DataFrame(data)])
    #         df.drop([0,4],inplace= True)
    #         #print(statistic = df.agg(['count', 'mean', 'std','median', 'max', 'skew','var', 'kurtosis']))
    #         transpose = df.T
    # transpose.to_excel("income.xlsx")
    #print(df)

soup =  BeautifulSoup('https://altmanzscoreplus.com/articles/AltmanZScorePlus_SPWH_Sportsmans_Warehouse_Holdings_Inc.html', headers={'USER-AGENT': "Mozilla/5.0"})
print(soup)