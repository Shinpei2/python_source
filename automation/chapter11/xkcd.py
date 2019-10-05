#! python3

import requests, bs4, sys, webbrowser, os

url = 'https://www.xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO ページをダウンロード
    print(f'ページをダウンロード中{url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO コミック画像のURLを探索
    images = soup.select('#comic img')
    # print(images)
    # TODO 画像をダウンロード
    if images == []:
        print('画像が見つかりませんでした。')
    else:
        for i in range(len(images)):       
            comic_url = 'https://www.xkcd.com/' + images[i].get('src')
            # print(comic_url)
            res_i = requests.get(comic_url)
            res_i.raise_for_status()

    # TODO 画像をフォルダに保存　※ファイル名：リンクのファイル部分
    outfile = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for item in res_i.iter_content(100000):
        outfile.write(item)
    outfile.close()
    # TODO PrevボタンのURL取得
    prev_link = soup.select('a[rel="prev"]')[0] 
    url = 'https://www.xkcd.com' + prev_link.get('href')
    # print(url)