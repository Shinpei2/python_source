from datetime import datetime, timedelta

# ()内の時間の合計(デルタ)を保持するtimedelta関数
delta = timedelta(weeks=3, days=11, hours=10, minutes=9, seconds=8)
print(delta)    # 33days = 3week * 7days + 11days
print(str(delta))
print(delta.days)
print(delta.seconds)
print(delta.microseconds)

dt = datetime.now()
thousand_days = timedelta(days=1000)
print(thousand_days)
delta2 = dt + thousand_days     # 元々のdatetimeオブジェクトにtimedeltaを加算
print(dt)
print(delta2)