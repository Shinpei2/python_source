from selenium import webdriver

browser = webdriver.Firefox()   # ブラウザを起動
browser.get('https://login.yahoo.com/?.src=ym&lang=&done=https%3A%2F%2Fmail.yahoo.com%2F')
email_elem = browser.find_element_by_id('login-username')
email_elem.send_keys('not_my_real_email')
email_elem.submit()

pw_elem = browser.find_element_by_id('login-passwd')
pw_elem.send_keys('12345')
pw_elem.submit()