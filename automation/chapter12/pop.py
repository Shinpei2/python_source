import openpyxl, pprint

# TODO: country_dataに群の人口と地域数を格納する。
print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet =wb.get_sheet_by_name('Population by Census Tract')
country_data = {}

# TODO: country_dataに群の人口と地域数を格納する。
print('行を読み込んでいます...')
for row in range(2, sheet.max_row +1):
    # シートの1行(row)に、一つの人口調査標準地域データがある
    state =sheet['B'+ str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # 1つの人口調査標準地域データをcountry_dataに格納する
    # このstateのキーが確実に用意されるようにする
    country_data.setdefault(state, {})
    # このstateのこのcountryのキーが確実に存在するようにする tracts:データ数, pop:人口
    country_data[state].setdefault(country, {'tracts':0, 'pop': 0})

    # 各行が人口調査標準地域を表すので、数を1つ増やす
    country_data[state][country]['tracts'] += 1
    country_data[state][country]['pop'] = int(pop)

# TODO: 新しいテキストファイルを開き、country_dataの内容を書き込む
print('結果を書込みます...')
outfile = open('census2010.txt', 'w')
outfile.write('all data = ' + pprint.pformat(country_data))
outfile.close()
print('完了！！！')