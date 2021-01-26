# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:45:07 2021

@author: Loga
"""



from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from time import sleep




req_proxy = RequestProxy() 
proxies = req_proxy.get_proxy_list() 

for i in range(len(proxies)):
 proxy = proxies[i].get_address()
 webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":proxy,
    "ftpProxy":proxy,
    "sslProxy":proxy,
    
    "proxyType":"MANUAL",
    
 }

 driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')
 try:
  driver.get('https://www.youtube.com/watch?v=BO6goZQONvY&t=384s')
  driver.maximize_window()
  driver.refresh()
  driver.sleep(120)
  driver.quit()
 except:
     driver.quit()
     pass
 
