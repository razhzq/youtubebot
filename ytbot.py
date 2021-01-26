# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:45:07 2021

@author: Loga
"""


from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from time import sleep




req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list

for i in range(proxies[900]):
 proxy = proxies[i].get_address()
 webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":proxy,
    "ftpProxy":proxy,
    "sslProxy":proxy,
    
    "proxyType":"MANUAL",
    
 }

 driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')
 driver.get('https://www.youtube.com/watch?v=BO6goZQONvY&t=384s')
 driver.maximize_window()
 driver.refresh()
 