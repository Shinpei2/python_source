#! python3

import requests, bs4, sys, webbrowser

if len(sys.argv) < 2:
    print('検索するワードを引数に指定してください。')
    exit()

print('Amazon Searching...')
search_result = 'https://www.amazon.co.jp/s?k='  + '+'.join(sys.argv[1:]) + '&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_2'
#webbrowser.open(search_result)
res = requests.get(search_result)
res.raise_for_status()

# 上位のリンクを取得する
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup)
links = soup.select('.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4 .a-link-normal.a-text-normal')     # classをセレクトできない→文字化けしてsoupに格納されてる
# print(links)

# 各結果をブラウザのタブで開く
open_num = min(5, len(links))   # min: 引数のうち最小値を返す
print(open_num)
for i in range(open_num):
    webbrowser.open('https://www.amazon.co.jp' + links[i].get('href'))