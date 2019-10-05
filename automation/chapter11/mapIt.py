#! python3
# mapIt.py - open the map pointed by command-line or clip-board

import webbrowser, sys

if len(sys.argv) > 1:
    # get address by command-line arguments
    address = ' '.join(sys.argv[1:])
    # print(address)
else:
    address = pyperclip.paste()

# get address by clip-board
webbrowser.open('https://www.google.com/maps/place/' + address)
