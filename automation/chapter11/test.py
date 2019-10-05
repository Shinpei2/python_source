import sys

search_link = 'https://www.amazon.co.jp/s?k='  + '+'.join(sys.argv[1:]) + '&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_2'
print(search_link)