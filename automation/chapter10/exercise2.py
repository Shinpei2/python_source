# 10-4
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 10-5
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 10-6 ログレベル DEBUG < INFO < WARNING < ERROR < CRITICAL
# 10-7 logging.disable(logging.critical)
# 10-8 ①ログ目的でないprint関数を消す可能性が無くなる。②print関数をコメントアウトする手間が無くなる。③logging.disable(logging.critical)1回だけでいつでもログ出力を消せる
# 10-9 Step: 次の行を実行して一時停止  Over:関数呼び出しを飛び越して次の行を実行  Out: 関数呼び出しから飛び出し実行
# 10-10 終了するかブレークポイントに到達するまで
# 10-11 デバッガが特定の行に到達した際に一時停止させるために設定するもの
# 10-12 設定する行を右クリックし、Set Breakpointを選択
