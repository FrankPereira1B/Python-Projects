# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import smatplib



URL = "https://www.amazon.com.au/Full-Frame-Mirrorless-Interchangeable-Lens-28-70mm-ILCE7M3K/dp/B07B45D8WV/ref=pd_lpo_421_t_1/357-7009886-6327419?_encoding=UTF8&pd_rd_i=B07B45D8WV&pd_rd_r=b8210ed4-9ecc-416b-b34f-fa0e3f865bd3&pd_rd_w=lF9aT&pd_rd_wg=GECjH&pf_rd_p=ad2d1e6e-bc60-4795-b4c0-2dbd35f6678d&pf_rd_r=JMZYD29CJJXXX6XE68V1&psc=1&refRID=JMZYD29CJJXXX6XE68V1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)
    
    Soup = BeautifulSoup(page.content, 'html.parser')
    
    title = Soup.find(id="ProductTitle").get_text()
    price = Soup.find(id="priceblock_outprice").get_text()
    converted_price = float(price[0:5])
    
    if(converted_price < 1.700):
        send_mail()
    
    print(converted_price)
    print(title.strip())
    
    
    if(converted_price < 1.700):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    
    server.login('', '')
    
    subject = 'Price Fell Down'
    body = 'Check the amazon Link - 'https://www.amazon.com.au/Full-Frame-Mirrorless-Interchangeable-Lens-28-70mm-ILCE7M3K/dp/B07B45D8WV/ref=pd_lpo_421_t_1/357-7009886-6327419?_encoding=UTF8&pd_rd_i=B07B45D8WV&pd_rd_r=b8210ed4-9ecc-416b-b34f-fa0e3f865bd3&pd_rd_w=lF9aT&pd_rd_wg=GECjH&pf_rd_p=ad2d1e6e-bc60-4795-b4c0-2dbd35f6678d&pf_rd_r=JMZYD29CJJXXX6XE68V1&psc=1&refRID=JMZYD29CJJXXX6XE68V1'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        '',
        '',
        msg
        
        
        )
   print('HEY EMAIL HAS BEEN SENT')
   
   server.quit()
   
   
   
   check_price()
   