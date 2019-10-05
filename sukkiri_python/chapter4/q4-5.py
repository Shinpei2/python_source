# (1)
temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]

# (2)
for i in range(len(temp)):
    print(temp[i])

print("\n")

# (3)
temp_new = []
for item in temp:
    temp_new.append(item)
temp_new[5] = "N/A"

print(temp)
print(temp_new)

# (4)
sum = 0
temp_count = 0
for item in temp_new:
    if isinstance(item,float):
        sum += item
        temp_count += 1
    else:
        pass
avg_temp = sum / temp_count
print(f"平均気温: {avg_temp: .1f}℃")
