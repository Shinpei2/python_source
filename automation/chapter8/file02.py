import os

# getsize
size = os.path.getsize('C:\\Users\\tskak\\python\\automation')
print(size)
dirlist = os.listdir('C:\\Users\\tskak\\python\\automation')
print(dirlist)

total = 0
for item in dirlist:
    total += os.path.getsize(os.path.join('C:\\Users\\tskak\\python\\automation', item))

print(f"total: {total} Byte")
