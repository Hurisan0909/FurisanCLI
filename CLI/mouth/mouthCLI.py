#個人用hyper計算機
import os
import platform
from datetime import datetime

#def用space
try:
    #clearコマンド実装
    def clear_screen():
        if platform.system() == "Windows": #Windows対応
            os.system("cls") 
        else:
            os.system("clear") # Linux / Mac用


    def help_data():#HELPメニュー
        print(("\n==========HELP=========="))
        print("数値を入力することでいろんなツールが以下の通りです。")
        print("\n>>>>計算の入力欄には「0123456789+-*/. 」のみ入力してください!<<<<\n")
        print("プログラム上の四則演算が分からない方はこちらをご覧ください")
        print("https://www.headboost.jp/python-operators/#index_id1")
        print("-------------------------")
        print("メニュー画面では以下の数値を入力して選択できます。")
        print("'clear'コマンドで画面をクリア可能。[注意clearを打つとメニュー戻ります]")
        print("1.四則演算機")
        print("2.割引計算機")
        print("3.元号表記変換")
        print("=========================")

    def calculation(): #四則演算処理
        print("\n==========CLI四則演算機==========")
        while True:
            print("\n!!!終了するには[q, exit, end]のいずれかを入力してください。")
            #ユーザーの入力
            user_cal_data = input("計算式を入力-> ")

            if user_cal_data == "clear":
                clear_screen()

            #終了処理
            if user_cal_data == "q" or user_cal_data =="exit" or user_cal_data == "end": # 終了処理
                back1 = input("メニューに戻りますか？[y/N]")
                if back1 == "N" or back1 == "n" or back1 == "": #自動選択でNoを選択
                    loop = True
                    return loop
                    break
                else:
                    break
            #evalによる計算
            #危険なcommandが悪用できるため悪用禁止。あくまでローカル用
            try:
                result = eval(user_cal_data)
                print("結果>",result)
            except:
                if user_cal_data == "clear":
                    print("")
                else:
                    print("\n>>>>計算の入力欄には「0123456789+-*/. 」のみ入力してください!<<<<")

    def discount_calculation(): #割引計算
        print("方式を選択してください")
        print("1. ? ％割引")
        print("2. ? 割引")
        try:
            user_select_dis = int(input(">"))
        except:
            print("1 or 2を入力してください")
        
        #input
        try:
            price = int(input("元の価格は? >"))
            #％計算
            if user_select_dis == 1: 
                percent = int(input("割引率(%)は? > "))
                price_data = price * (1 - percent / 100)
                print(f'\n_____「{price}円」を「{percent}%」引きすると「「{price_data}円」」です。_____\n')
            #割引計算
            elif user_select_dis == 2:
                wari = int(input("割引はどれくらい? > "))
                price_data2 = price * (1 - wari * 0.1)
                print(f'\n_____{price}円を{wari}割引すると{price_data2}円です。_____\n')
        
            back1 = input("メニューに戻りますか？[y/N]")
            if back1 == "N" or back1 == "n" or back1 == "": #自動選択でNoを選択
                loop2 = True
                return loop2
        
        except ValueError:
            print("整数を入力してください。")

    def year_name():
        print("======方式を選択======")
        print("基本的には'1'を入力[2]は指定の年を直すときに使用")
        print("1. 現在の年を自動所得する")
        print("2. 手動で入力")
        print("")

        try:
            
            user_sel_input = input(">")
            
            if user_sel_input == "clear":
                clear_screen()


            #例外処理
            if user_sel_input == "0":
                print("選択に0はありません")
            elif user_sel_input >= "3":
                print("1か2を選択してください。")


            if user_sel_input == "1":
                auto_year = datetime.now().year #今の年を所得
                reiwa = auto_year - 2018 #直打ちは各年の元年 -1
                heisei = auto_year - 1988
                syouwa = auto_year - 1925
                taisyo = auto_year - 1911
                meizi = auto_year - 1867
                print("年号の'1'は元年を指します。(例 令和1年 == 令和元年)")
                print(f'現在({auto_year}年)の変換は [')
                print(f'\n    令和{reiwa}年')
                print(f'    平成{heisei}年')
                print(f'    昭和{syouwa}年')
                print(f'    大正{taisyo}年')
                print(f'    明治{meizi}年')
                print("\n]")
            elif user_sel_input == "2":
                user_year_num = int(input("計算したい年を入力 > "))
                reiwa = user_year_num - 2018 #直打ちは各年の元年 -1
                heisei = user_year_num - 1988
                syouwa = user_year_num - 1925
                taisyo = user_year_num - 1911
                meizi = user_year_num - 1867
                print("年号の'1'は元年を指します。(例 令和1年 == 令和元年)")
                print(f'({user_year_num}年)の変換は [')
                print(f'\n    令和{reiwa}年')
                print(f'    平成{heisei}年')
                print(f'    昭和{syouwa}年')
                print(f'    大正{taisyo}年')
                print(f'    明治{meizi}年')
                print("\n]")

            back1 = input("メニューに戻りますか？[y/N]")
            if back1 == "N" or back1 == "n" or back1 == "": #自動選択でNoを選択
                loop2 = True
                return loop2



            
        except ValueError:
            print("整数を入力してください。")





    while True: # メインメニュー画面 clear コマンド後の先
        print("\n==========CLI計算機メニュー==========")
        print("[[©2025 FuriCLI All Rights Reserved]]")
        print("### Ver.1.0 ###")
        print("--------------------------------------")
        print("分からないときは'help'を入力してください")
        user_select_num = input(">")

        #HELP処理
        if user_select_num == "help":
            help_data()
        #clear処理
        elif user_select_num == "clear":
            clear_screen()
        #終了処理
        elif user_select_num == "0":
            print("終了します。")
            break
        
        #メニュー操作

        #[1]---四則演算---
        if user_select_num == "1":
            data1 = calculation()
            if data1 == True:
                break
        
        elif user_select_num == "2":
            data2 = discount_calculation()
            if data2 == True:
                break

        elif user_select_num == "3":
            data3 = year_name()
            if data3 == True:
                break

except KeyboardInterrupt: # control + Cの対策
    print("\n強制終了します。")