# Today I will be creating a Stock News Alert Project making use of different APIS
# that gather the stock data, compare two days data and alert about the changes in the
# stock price in percentage, wiht a relevant news headline
# I will be using the Extra Hard difficulty level because why now
# Also I will not be using Twilio since it didn't work for me and I deleted my Twilio
# account because it didn't work.

import requests
            # import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and 
# the day before yesterday then print("Get News").
# It was surprising how easy it was to get an API key, I just had to give a temp email
# Not even sign up completely with a password or anything
av_api_key = "<api_key>"
# From the Core Stock API, we're using the TIME_SERIES_DAILY endpoint so let's set up params
av_parameters = {
    "function": "TIME_SERIES_DAILY",
    # This will make sure we get data of that particular type
    "symbol": STOCK,
    # We need info for this particular stock, in this case Tesla Inc.
    "apikey": av_api_key
}

stock_response = requests.get("https://www.alphavantage.co/query", params = av_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
# Alas, I have reached my API rate limit of 25 requests per day

# Now let's get today's date since the data is formatted as a dictionary with date records on it
                # today = datetime.date.today()
# Instead of today, we need to extract data from the latest day in the list so we need to access that
                # latest_day = stock_data["Meta Data"]["3. Last Refreshed"]
# How do I turn it into a datetime object now?
# or do I just access the elements iteratively?
# Now I am doing this from the docs of datetime completely
                # one_day = datetime.timedelta(days = 1)
# Ok now I should have all the means to retrieve data from the stock_data dictionary

# The enclosing dictionary contains dictionaries called "Meta data" and Time Series (Daily)
# latest_day_close = stock_data["Time Series (Daily)"].keys()
# Alright I give up, I'm watching the lecture
# Okay enough hints, now that I know dictionary can't be accessed just like that and I need to use
# some sort of list comprehension to convert all keys into a list at first

def stock_alert():
    news_api_key = "<api_key>"

    news_parameters = {
        "apiKey": news_api_key,
        "qInTitle": STOCK
        # I had used "q" before but it returns the articles where the search term didn't appear
        # in the title itself. Since some news outlets can use random stock names to boost their
        # impressions, it would be better to use "qInTitle" rather than just "q"
        
        # Now I could use a "country" parameter for US only,
        # or a "category" parameter for business headlines only
        # but since I've kept the search term as the NASDAQ abbreviation
        # those are the only headlines that should pop, most probably
    }
    # print("Stock change by over 5%")
    # It's funny they said "Disposable emails are blocked" but I generated my API Key
    # using a disposable email. fun times
    news_response = requests.get("https://newsapi.org/v2/everything", params = news_parameters)
    # newsapi offers multiple endpoints, like the "everything" that scans the past 20 years of
    # detailed news reports, but I need only the breaking news, so I'll use the "top-headlines"
    # On second thought, after reaching this part of the lessons, I found out most of stock market
    # activities don't really make it to the top-headlines, so I'll have to use "everything"
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    # Hmm the response came back with 0 responses, let me see the course to confirm I'm not doing
    # anything wrong (This was when I used top-headlines)
    # And now with everything I do get the headlines, but jsonviewer said "Invalid JSON format"
    # I don't know what it means but I've got the basic structure down:
    # Inside the 'contents' key's value is a list of dictionaries, each with a key called "source"
    # which I don't think I'll be using, I'll use the "title" and "description" keys
    # I can't believe I confused "articles" for "contents"
    # Let's print three values from the list then. I'll extract the list in the data at the very start
    three_day_data = news_data[1:4]
    # Since the first news seems rubbish and clearly a promotion, I'll have to go with 1:4 on this one
    # for news_stories in news_data[:3]:
    #     # We are only interested in the first 3 stories, so let's go with that
    #     news_source = news_stories["source"]["name"]
        # news_title = news_stories["title"]
        # news_desc = news_stories["description"]
    #     print(f"\n{news_source}\n{news_title}\n{news_desc}\n")
    #     # For some reason I can't use the [] inside an f-string interpolation but nevermind, I'll
    #     # just stick to using good ol' variables. I have no energy to search for that
    #     # Okay this seems fine enough. Let's continue with the course
    # Now let's set up the contents for the actual email message as instructed below
    if change < 0:
        up_down = "📈"
    else:
        up_down = "📉"
    change_p = abs(round(change*100))
    news_messages = [f"{STOCK}: {up_down}{change_p}%\nHeadline: {news['title']}\nBrief: {news['description']}" for news in three_day_data]
    # We need to create a list that contains 3 strings in the format suggested below
    # Looks like I found the answer to why using [] didn't seem to work inside f-string. It was because
    # I was using the same kind of quotes inside and outside of the {} so the interpreter would get
    # confused, thinking whether I wanted to close the f-string or just give a variable
    for news_message in news_messages:
        print(news_message)


dates = [date for date in stock_data]
# In the course the comprehension used was:
# dates = [date for (date,value) in stock_data.items()]
# It works the same so let's just move on

yesterday_closing = float(stock_data[dates[0]]["4. close"])
closing_before = float(stock_data[dates[1]]["4. close"])
change = (closing_before-yesterday_closing)/closing_before

if abs(change) > 0.05:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    stock_alert()


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# For this step, I'll just not bother. But I'll write the code for Twilio
# Since this will all happen IF the stock price has a change greater than expected, I'll just create
# a new function that will have all these stuff enclosed within itself

# Code for Twilio
from twilio.rest import Client
auth_token = "<auth_token>"
phone_no = "<phone_no>"
own_no = "<own_phone_no>"
account_sid = "<twilio_username>"

client = Client(account_sid = account_sid, password = auth_token)
client.messages.create(
    from_ = phone_no,
    to = own_no,
    body = "message"
)