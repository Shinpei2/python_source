# JSON　：　JSプログラムがデータ構造を記述するネイティブな方法
# JSONはAPI（Webサイトのインターフェース）として用いられる

# json文字列　※""で囲っている点に注意、改行しちゃダメ！
json_data = '{ "name": "Zophie", "isCat": true, "mineCaught": 0, "felineIQ": null }'

import json

# json.loads() : json文字列　→ jsonオブジェクト
json_data_pyv = json.loads(json_data)
print(json_data_pyv)

# json.dumps() : Pythonの辞書型　→ json文字列
json_dict = { "name": "Zophie", "isCat": True, "mineCaught": 0, "felineIQ": None }
json_dict_jsobj = json.dumps(json_dict)
print(json_dict_jsobj)