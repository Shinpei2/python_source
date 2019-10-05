'''
import traceback

try:
    raise Exception('これはエラーメッセージです')

except:
    err_file = open('errorInfo.txt', 'w')
    err_file.write(traceback.format_exc())
    err_file.close()
    print('エラー情報をerrorInfo.txtに書きました。')
format_exc()
'''
