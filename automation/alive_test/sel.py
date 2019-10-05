from selenium import webdriver

browser = webdriver.Firefox()   # ブラウザを起動
browser.get('https://www.google.co.jp/webhp?authuser=1')
elem = browser.find_element_by_xpath("html//body//div[1]//div[4]//form[1]//div[2]//div[1]//div[1]//div[1]//div[2]//input[1]")  # [1]が最初を表す点に注意
elem.send_keys('ははは')
# 該当するフォームのidから要素を取得する

# 上から順にパスを辿る
# (browser.find_element_by_xpath('//html/body/....../li/td?')).click()
# (browser.find_element_by_xpath('//li[1]')).click()  # [1]が最初を表す点に注意

# そのidのフォームに値を入力する

# pw_elem = browser.find_element_by_id('login-passwd')
# sign_button.click()


### tips ###
# # 複数のフォームがある場合、どの要素でsubmit()しても送信可能
# pw_elem.submit()
# # 上記の命令は、email_elem.submit()でもOK

# # クリックしたい場合、要素を取得してその要素に以下のコマンド
# elem.click()

# # クラスを指定する場合は、添え字をつけること(リストが作成されるため)　※以下、例
# navi_logo = browser.find_elements_by_class_name('nav-logo-link')
# navi_logo[0].click()


'''
### ALIVEログイン自動化ツール案 ###
import time
from selenium import webdriver
# ブラウザでALIVEのページを開く
browser = webdriver.Firefox()   # ブラウザを起動
browser.get(url)      # urlへ飛ぶ

# フォームに社員番号とパスワードを入力し、ログインボタンをクリック
id = ''
pw = ''
id_elem = browser.find_element_by_id('フォームのid名')  # inputタグ
pw_elem = browser.find_element_by_id('フォームのid名')
ipw_elem.submit()
time.sleep(3) # ページ遷移を待つ

# 就業ボタンを押す
button1_elem = browser.find_element_by_id('ボタン1のid名')
button1_elem.click()
time.sleep(3)

# 出退勤ページボタンを押す
button2_elem = browser.find_element_by_id('ボタン2のid名')
button2_elem.click()
time.sleep(3) # ページ遷移を待つ

# 通常出勤ボタンを押す
button3_elem = browser.find_element_by_id('通常ボタンのid名')
button3_elem.click()
exit()
'''
