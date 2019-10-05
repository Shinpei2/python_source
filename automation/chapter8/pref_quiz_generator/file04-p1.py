#! python
# randomQuizGenerator.py

import random

# key: prefecture  value: capital
capitals = {'北海道': '札幌市', '青森県': '青森市', '岩手県': '盛岡市',
  '宮城県': '仙台市', '秋田県': '秋田市', '山形県': '山形市', '福島県': '福島市',
  '茨城県': '水戸市', '栃木県': '宇都宮市', '群馬県': '前橋市',
  '埼玉県': 'さいたま市', '千葉県': '千葉市', '東京都': '東京',
  '神奈川県': '横浜市', '新潟県': '新潟市', '富山県': '富山市', '石川県': '金沢市',
  '福井県': '福井市', '山梨県': '甲府市', '長野県': '長野市', '岐阜県': '岐阜市',
  '静岡県': '静岡市', '愛知県': '名古屋市', '三重県': '津市', '滋賀県': '大津市',
  '京都府': '京都市', '大阪府': '大阪市', '兵庫県': '神戸市', '奈良県': '奈良市',
  '和歌山県': '和歌山市', '鳥取県': '鳥取市', '島根県': '松江市',
  '岡山県': '岡山市', '広島県': '広島市', '山口県': '山口市', '徳島県': '徳島市',
  '香川県': '高松市', '愛媛県': '松山市', '高知県': '高知市', '福岡県': '福岡市',
  '佐賀県': '佐賀市', '長崎県': '長崎市', '熊本県': '熊本市', '大分県': '大分市',
  '宮崎県': '宮崎市', '鹿児島県': '鹿児島市', '沖縄県': '那覇市'}

# 35個の問題集を作成
for q_num in range(35):
    # TODO_1 問題集と解答集のファイルを作成する
    quiz = open(f'CapitalQuiz_Ver.{q_num+1}.txt', 'w')
    answer = open(f'CapitalQuiz_Answer_Ver{q_num+1}.txt', 'w')

    # TODO_2 問題集のヘッダーを書く
    quiz.write('Name:\n\nDate:\n\nQuater:\n\n')
    quiz.write(f'都道府県庁所在地クイズ(問題番号{q_num+1})'.center(40,'='))
    quiz.write('\n\n')
    # TODO_3 都道府県の順番をシャッフルする
    pref = list(capitals.keys())
    random.shuffle(pref)
    # TODO_4 47都道府県をループして、それぞれ問題を作成する
    for i in range(len(pref)):
        correct_ans = capitals[pref[i]]
        wrong_ans = list(capitals.values())
        del wrong_ans[wrong_ans.index(correct_ans)] # []内: wrong_ansのうちC_Aのある添え字を取り出す
        wrong_ans = random.sample(wrong_ans, 3)
        answer_options = wrong_ans + [correct_ans]
        random.shuffle(answer_options)

        # TODO_5 問題文と解答文を問題ファイルへ書き込み
        quiz.write(f'問{i+1}. {pref[i]}の県庁所在地は?\n')
        for j in range(4):
            quiz.write(f"{'ABCD'[j]}. {answer_options[j]}\n")
        quiz.write('\n')

        # TODO_6 答えの選択肢をファイルに書く
        answer.write(f"問{i+1}. {'ABCD'[answer_options.index(correct_ans)]}\n\n")

    quiz.close()
    answer.close()
