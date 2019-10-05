from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ゲームを起動する
browser = webdriver.Firefox()
browser.get('https://play2048.co/')

browser_html = browser.find_element_by_tag_name('html')
gameover_elem = browser.find_element_by_class_name('game-message')
while gameover_elem.is_displayed() == False:
    browser_html.send_keys(Keys.UP)
    browser_html.send_keys(Keys.RIGHT)
    browser_html.send_keys(Keys.DOWN)
    browser_html.send_keys(Keys.LEFT)

print('終了！')
    