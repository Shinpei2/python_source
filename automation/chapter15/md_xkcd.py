#! python3
# md_xkcd.py - XKCDコミックをマルチスレッドでダウンロード

import requests, os, bs4, threading
dir_name = 'xkcd'
os.makedirs(dir_name, exist_ok=True)

def dl_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # ページをダウンロード
        print(f'ページをダウンロード中 https://www.xkcd.com/{url_number}...')
        res = requests.get(f'https://www.xkcd.com/{url_number}')
        res.raise_for_status

        soup = bs4.BeautifulSoup(res.text)      #ページのhtmlを読み取る

        # コミック画像のURLを探す
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('コミック画像が見つかりませんでした')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            print(f'画像をダウンロード中{comic_url}...')
            res = requests.get(comic_url)
            res.raise_for_status
        
        # 画像を./xkcdに保存する
        outfile = open(os.path.join(dir_name, os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            outfile.write(chunk)
        outfile.close()
    
# TODO: Threadオブジェクトを生成して開始する
dl_threads_list = []
for i in range(1,1400, 100):
    dl_thr = threading.Thread(target=dl_xkcd, args=(i, i+100))
    dl_threads_list.append(dl_thr)
    dl_thr.start()  # Threadオブジェクトにstart()する度に新しいスレッドで処理が始まる

# TODO:全てのスレッドが終了するのを待つ
for dl_thr in dl_threads_list:
    dl_thr.join()   #list無いから呼び出したdl_thrが終了するまで待つ
print('完了')