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
        print("Current BTC price: "+BS(requests.get("https://cryptowat.ch/it-it/").text, "html.parser").find("span", attrs={"class": "_3XNm6CSrchU-MNbu1Zh3m2"}).text, end="\r")
    except:
        check = 1
    
    if check == 0:
        time.sleep(3)
    else:
        check = 0
        



