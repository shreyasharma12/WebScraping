from cgi import print_exception
from traceback import print_tb
from unicodedata import name
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client
import twilio 

##############################################################################################################################################

url = "https://www.livecoinwatch.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}

req = Request(url, headers = headers)
webpage = urlopen(req).read()			
soup = BeautifulSoup(webpage, "html.parser")

#############################################################################################################################################

cryptocurrency_table = soup.find("table")

cryptocurrency_rows = cryptocurrency_table.findAll("tr")
print()
print("Top 5 Cryptocurrency Companies:")
for x in range(1,6):

    td = cryptocurrency_rows[x].findAll("td")
    ranking = td[0].text
    name = td[1].text
    current_price = float(td[2].text.strip('$'))
    percent_change = float(td[8].text.strip('%'))

    print()
    print("Currency Ranking:", ranking)

    print("Currency:", name)

    currentprice_ = "${:,.2f}".format(current_price)
    print("Current Price:", currentprice_)

    print("% Change:",percent_change,"%")
    following_change = round((current_price)/(1+(percent_change/100)),2)
    following_change_format = "${:,.2f}".format(following_change)

    print("Price (based on % change):",following_change_format)

##############################################################################################################################################

    AccountSID = "ACe837848febdaeecb690ac3e967e17013"
    AuthToken = "e26ca57be5e1ecfa0145db35351d2671"
    client = Client(AccountSID,AuthToken)
    TwilioNumber = "+13156653626"
    mycellphone = "+12816610425"

################################################################################################################################################
    
    if "Bitcoin" in name and current_price < 40000:
        Bitcoin_phonetext = client.messages.create(to = mycellphone, from_= TwilioNumber, body = "Bitcoin Cryptocurrency price is below $40,000.")

    if "Ethereum" in name and current_price < 3000: 
        Ethereum_phonetext = client.messages.create(to= mycellphone, from_= TwilioNumber, body = "Ethereum Cryptocurrency price is below $3,000.")