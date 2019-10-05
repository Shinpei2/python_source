table_data = [
    ['apples', 'oranges', 'cherries', 'banana','grape', 'pinnapple'],
    ['Alice', 'Bob', 'Carol', 'David', 'Emi'],
    ['dogs', 'cats', 'moose', 'goose',]
]

def table_print(datas):
    # 最大要素数の内側リストを探索し、空白部に'*'を追加する。
    max_index = 0
    for i in range(len(datas)):
        if len(datas[max_index]) < len(datas[i]):
            max_index = i
    max_data = datas[max_index]
    # print(max_data)
    for i in range(len(datas)):
        if len(max_data) != len(datas[i]):
            add = len(max_data) - len(datas[i])
            for j in range(add):
                datas[i].append('*')

    col_width = [0] * len(datas)   # 要素数=列数(データ数)のリストcol_widthを用意
    # 各列の最大文字数を取り出し、リストcol_widthに格納
    for i in range(len(datas)):
        max_len = datas[i][0]
        for item in datas[i]:
            if len(max_len) < len(item):
                max_len = item
        # print(f'max_len: {max_len}')
        col_width[i] = len(max_len)
    # print(col_width)


    # 1行ずつ
    col_num = len(datas)
    rec_num = len(max_data)
    # print(rec_num)
    for i in range(rec_num):
        rec_list = []
        for j in range(col_num):
            just_word = datas[j][i].rjust(col_width[j], ' ')
            rec_list.append(just_word)
        # print(rec_list)
        record = ' '.join(rec_list)
        print(record)



table_print(table_data)
