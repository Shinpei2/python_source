import time
from selenium import webdriver


SN_email = 'takahashi-shinpei@mki.co.jp'
SN_pw = 'ki41922960M@'

browser = webdriver.Firefox()   # ブラウザを起動
browser.get('https://developer.servicenow.com/app.do#!/home')
time.sleep(3)


# LOG IN ボタンの要素を取得
elem = browser.find_element_by_xpath('html//body//ui-view//div[1]//header//nav[1]//div[1]//div[1]//div[1]//div[2]//ul[1]/li[2]//a[1]')
elem.click()

time.sleep(8)  # ログイン画面に遷移するのを待つ

# emailをフォームに入力後、nextボタンをクリック
email_elem = browser.find_element_by_id('username')
email_elem.send_keys(SN_email)
(browser.find_element_by_id('usernameSubmitButton')).click()

time.sleep(2)

# パスワードをフォームに入力後、Sign inボタンをクリック
pw_elem = browser.find_element_by_id('password')
pw_elem.send_keys(SN_pw)
(browser.find_element_by_id('submitButton')).click()


time.sleep(15)

# instanceをクリック　※リンク先をJavaScriptで取ってくてるので、下記のコードでは不可能
# (browser.find_element_by_xpath('html//body//ui-view//div[1]//header//nav[1]//div[1]//div[2]//div[1]//div[2]//ul[1]//li[5]//ul[1]//li[1]//a')).click()

