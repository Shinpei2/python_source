scores = {"Japanese":70, "Math":80, "English": 60}

print(scores)

print(scores['Japanese'])

del scores['Japanese']
print(scores)

scores['Chinese'] = 100
print(scores)

total = sum(scores.values())
print(f"{total}")
avg = total / len(scores)
print(f"{avg:.1f}")
