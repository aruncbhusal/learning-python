# Yet another project today and this time we're tracking the price of an item over time
# The course mentioned https://camelcamelcamel.com/ which I have used in the past too
# Some products don't ship to Nepal so I can't just select any random product, I'll have
# to be careful what item I choose so that the prices will be reflected properly

# Okay even though it took a while to find a product that had a price history on camel3
# The product I settled for was an air fryer.

EMAIL = "<YOUR_EMAIL>"
APP_PASSWORD = "<YOUR_PASS>"
RECIPIENT_EMAIL = "<ANOTHER_EMAIL>"


import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B0CV5ZSR17"
# URL = "https://www.amazon.de/dp/B08QKTXT1N"

desired_price = 350


header = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
          "DNT" : "1",
          }

response = requests.get(url=URL, headers=header).content.decode(encoding='utf-8', errors="replace")
# Without the header, the Amazon page will not load as expected, so we need to pass the
# usual HTTP headerst that our browser sends to Amazon while trying to visit the page
# We can use https://myhttpheader.com to see what headers our browser has sent
# print(response)
soup = BeautifulSoup(response, "html.parser")
# Since html parser can't do it, we have to use lxml parser instead
# html parser worked fine so I'm back to it
# print(soup)
# price_block = soup.find("div", id="corePriceDisplay_desktop_feature_div")
# print(price_block)
# print(soup.find(name="div", id="ppd").prettify())
price = soup.select(selector="#ppd .a-price>.a-offscreen")
article = soup.select(selector="#productTitle")
print(price)
print(article)

price_item = float(price[0].getText().strip("$"))
product_info = article[0].getText().strip()

# I had to consult people in the discord server to make it work, and even so I'm using a VPN
# right now since Amazon isn't yet available fully in Nepal

if price_item <= desired_price:
    with smtplib.SMTP(host= "smtp.gmail.com", port= 587) as connection:
        connection.starttls()
        connection.login(
            user= EMAIL,
            password= APP_PASSWORD,
        )
        connection.sendmail(from_addr= EMAIL,
            to_addrs= RECIPIENT_EMAIL,
            msg= f"{product_info} available for ${price_item} only!\n Don't miss the offer!"
            )
    print("Email sent!")

# This was a pain to do, but in the end, everything worked out and I learned more about
# how to effectively use BeautifulSoup to extract only information that is of value to us.