from selenium import webdriver
import requests, time

browser = webdriver.Firefox()   # ブラウザを起動
browser.get('https://www.amazon.co.jp/')

item = 'サカナクション'

item_elem = browser.find_element_by_id('twotabsearchtextbox')
item_elem.send_keys(item) 
item_elem.submit()

time.sleep(3)

# browser.get('https://www.amazon.co.jp/s?k=%E3%82%B5%E3%82%AB%E3%83%8A%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss')



