#!/usr/bin/env python
# coding: utf-8

# In[1]:


#We will take the data from URL
#Make the data more clear and readible with bs

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#Creating 
n = ToastNotifier()

#definin a function to get URL
def getdata(url):
    r = requests.get(url)
    return r.text #returning its form of texts

htmldata = getdata("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Sivas")
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())

current_temp = soup.find_all("div", class_="anlik-sicaklik-deger ng-binding",attrs={'ng-bind': 'sondurum[0].sicaklik | comma'})
temp = (str(current_temp))
result = "current_temp" + temp[128:-9]
print(result)
n.show_toast("Weather update", result, duration = 10)


# In[ ]:





# In[ ]:




