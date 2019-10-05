#! python3

import json, requests, sys

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: ')
    sys.exit()
location = ' '.join(sys.argv[1:])

# APIキーの定義
APPID = '052e4193c260cff5a17c4bebf7515a8e'

# TODO:OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}'
response = requests.get(url)    # urlのページ(responseオブジェクト)を取得
response.raise_for_status() # 異常時は強制終了
# print(response.text)     # WEBページをテキストベースで画面出力

# TODO: JSONデータ(JSON文字列)からPython変数を読み込む
weather_data = json.loads(response.text)

# TODO: 天気予報の情報を表示する
w = weather_data['main']    # 必要なデータはJSONデータのうち、キーが'list'の中のみ
print(w)
print(f'{location}の今日の天気: ')
# print('：{}%'.format(humidity))
print('湿度：{}%'.format(w['humidity']))
print('平均気温：{}℃'.format( round((w['temp']-273), 2)) )
print('最高気温：{}℃'.format( round((w['temp_max']-273), 2)) )
print('最低気温：{}℃'.format( round((w['temp_min']-273), 2)) )


# 手順まとめ
# 1．検索キーワードをコマンドラインから入力
# 2. APIを用いてJSON文字列を取得し
# 　・APIキーの用意
# 　・APIと検索キーワードからURL文字列を作成する
# 　・URLのWebサイトをrequests.get()で獲得
# 　・json.loads()でrespons.textをjsonオブジェクトとして読み込み
# 3．情報の取得
# 　・josnデータから必要なデータを取り出し、表示

