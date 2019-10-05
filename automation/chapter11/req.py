import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()  # 異常時は強制終了
outfile = open('Romeo.txt', 'wb')
for item in res.iter_content(100000):
    outfile.write(item)

outfile.close()