import requests
from twilio.rest import Client 

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stockPrice():
    stockParams = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
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
    change_percent = int((yesterday_close - day_before_yest_close) / day_before_yest_close * 100)
    if abs(change_percent) >= 10:
        getNews(yesterday, change_percent)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def getNews(fromDate, change_percent):
    newsParams = {
        "q": COMPANY_NAME,
        "from": fromDate,
        "sortBy": "popularity",
        "apiKey": "0e848ccf53374313b3b5d26c5ad2fcbf"
    }

    message_to_send = ""
    articles = requests.get("https://newsapi.org/v2/everything", params=newsParams)
    for article in range(0,3):
        sourceName = articles.json()["articles"][article]["source"]["name"]
        title = articles.json()["articles"][article]["title"]
        url = articles.json()["articles"][article]["url"]
        message_to_send = message_to_send + f"STOCK: {STOCK} {change_percent}%\nPublished by: {sourceName}\nHeadline: {title}\nurl: {url}\n\n"
    
    sendSMS(message_to_send)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def sendSMS (message):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    receiver = "+11234567890"
    sender = "+11234567890"

    message = client.messages \
            .create(
                body=message,
                from_=sender,
                to=receiver
            )

stockPrice(STOCK)