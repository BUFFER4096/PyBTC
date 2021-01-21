import requests
from bs4 import BeautifulSoup as BS

import time

logo = """
 _________    _______________    ____________
|  _____  |  |	             |	|	     |							
|  |   |  |  |_______________|	|     _______|
|  |___|  |       |     |       |    |
|_________|	  |	|	|    |
|  |	          |     |       |    |
|__|_______	  |	|	|    |
|  _____  |	  |	|	|    | 
|  |   |  |	  |	|	|    |_______
|  |___|  |       |	|	|	     |
|_________|	  |_____|	|____________|

"""

print(logo)

check = 0

while 1:
    try:
        print("Current BTC price: "+BS(requests.get("https://www.coindesk.com/price/bitcoin").text, "html.parser").find("div", class_="price-large").text, end="\r")
    except:
        pass
    
    if check == 0:
        time.sleep(3)
    else:
        check = 0
        



