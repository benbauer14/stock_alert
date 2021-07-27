import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stockPrice(stockTick):
    stockParams = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stockTick,
        "apikey": "RDIL6MF3KVT8KLT5"
    }
    data = requests.get("https://www.alphavantage.co/query", params=stockParams)
    date_keys = data.json()["Time Series (Daily)"].keys()
    list = []
    for key in date_keys:
        list.append(key)
    yesterday = list[0]
    day_before_yest = list[1]
    yesterday_close = data.json()["Time Series (Daily)"][yesterday]["4. close"]
    day_before_yest_close = data.json()["Time Series (Daily)"][day_before_yest]["4. close"]
    print(yesterday_close)
    print(day_before_yest_close)

    #set arbitary 10% threshold
    if abs((yesterday_close - day_before_yest_close) / day_before_yest_close) >= 0.1:
        getNews()
stockPrice("IBM")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def getNews(stockTick):
    

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

