import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
stock_api_key = ""
new_api_key = ""
stock_params ={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "datatype":"json",
    "apikey": stock_api_key
}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
stock_data = response.json() 
# print(data)
dates = list(stock_data['Time Series (Daily)'])
close1 = float(stock_data['Time Series (Daily)'][dates[0]]['4. close'])
close2 = float(stock_data['Time Series (Daily)'][dates[1]]['4. close'])
print(close1,"---",close2)
if(abs((close1-close2)/close2)>=0.05):
    print("msg")
news_params={
    "q":"tesla",
    "from":str(stock_data['Time Series (Daily)'][dates[0]]),
    "sortBy":"popularity",
    "apikey":new_api_key,
    "page":1,
    "pageSize":10
    
}
response1 = requests.get(NEWS_ENDPOINT,params=news_params)
response1.raise_for_status()
news_data = response1.json()
print(news_data) 


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

