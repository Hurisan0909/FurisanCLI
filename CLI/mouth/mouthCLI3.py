import os
import platform
import time
from datetime import datetime

'''
Note

計算機の0を割るときの例外処理を実装する
'''



# --- def_space ---
#エラー処理関数
#===エラー関数について===
# select_num => 選択個数+1
# user_select_num => userの入力の変数
def input_inspection(select_num, user_select_num):
    if user_select_num >= select_num:
        print(f'\n!>> {select_num}以上の選択はありません。もう一度やり直してください')
        time.sleep(2)
    elif user_select_num == 0:
        print("\n!>> 0の選択はありません。")
        time.sleep(2)
    elif user_select_num <= 0:
        print(f'\n!>> マイナス値は存在しません。')
        time.sleep(2)

#---clearコマンド---
def clear_screen():
    if platform.system() == "Windows": #Windows対応
        os.system("cls") 
    else:
        os.system("clear") # Linux / Mac用

#---終了メッセージ---
def end_program():
    print("\nメインメニューに戻りますか？")
    user_select_end = input("[y/N]>>> ").lower() 
    if user_select_end in ("y", "yes","ye","ok"):
        return True
    elif user_select_end in ("n", "no", "off", ""):
        return False
    else:
        print("'y'か'n'の選択をしてください。")

# ---HELP関数----
def help_data():
    print(("\n==========HELP=========="))
    print("数値を入力することでいろんなツールが以下の通りです。")
    print("\n>>>>計算の入力欄には「0123456789+-*/. 」のみ入力してください!<<<<\n")
    print("プログラム上の四則演算が分からない方はこちらをご覧ください")
    print("https://www.headboost.jp/python-operators/#index_id1")
    print("-------------------------")
    print("メニュー画面では以下の数値を入力して選択できます。")
    print("'clear'コマンドで画面をクリア可能")
    print("1.四則演算機")
    print("2.割引計算機")
    print("3.元号表記変換")
    print("4.準備中...")
    print("clear. OSのclearコマンドを実行")
    print("[q, exit, end]のどれかでプログラムの終了")
    print("---------------------------")
    print("\n/// 注意事項 ///")
    print("clearコマンドはOSのクリアを使用するのでこのプログラムより前のログも消えます。")
    print("[!>>]これはエラーを意味しています")
    print("")
    print("=========================")
    time.sleep(3)

#---四則演算メニュー---
def calculation(cal_data):
    try:
        result = eval(cal_data)
        return result
    except NameError:
        print("\n!>> 整数で入力してください")
        time.sleep(2)
    except SyntaxError:
        print("\n!>> 数値を入力してください")
        time.sleep(2)
    except ZeroDivisionError:
        print("!>> 0で割ることはできません。")
        time.sleep(2)

#--- 割引計算(％)---
def discount_calculation_percent(price, percent):
    price_data = price * (1 - percent / 100)
    return price_data

def discount_calculation(price, wari):
    price_data = price * (1 - wari * 0.1)
    return price_data

def auto_year_cal(auto_year):
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



# --- end_def ---




#メインメニュー画面
try:
    loooop = True
    while loooop:
        print("\n==========CLIメインメニュー==========")
        print("[[©2025 FuriCLI All Rights Reserved]]")
        print("(ver1.3)")
        print("--------------------------------------")
        print("分からないときは'help'を入力してください")

        #入力
        user_menu_input = input(">").lower()
        #clearと終了処理
        if user_menu_input == "clear":
            clear_screen()
            continue
        elif user_menu_input == "help":
            help_data()
            continue
        elif user_menu_input in ("q", "end","exit"):
            print("!>> 終了します。")
            time.sleep(1)
            break
        #Strをintに変換
        try:
            user_menu_input = int(user_menu_input)
        except ValueError:
            print("\n!>> 整数で入力してください。")
            time.sleep(2)
            continue
        
        #menu_select_numはメニュー個数
        #err_1でエラー処理
        menu_select_num = 4
        err_1 = input_inspection(menu_select_num, user_menu_input)


        #====================メインメニューIF====================
        if user_menu_input == 1:
            while True:
                print("\n==========CLI四則演算機==========")
                user_cal_data = input("計算式を入力 > ")
                if user_cal_data == "clear":
                    clear_screen()
                    continue
                elif user_cal_data in ("q", "end", "exit"):
                    end_data = end_program()
                    if end_data == False:
                        loooop = False
                        break
                    elif end_data == True:
                        print("メニューに戻ります...")
                        time.sleep(2)
                        break
                        
                data1 = calculation(user_cal_data)
                print(f'結果__{data1}__')

        elif user_menu_input == 2:
            while True:
                print("\n==========CLI割引計算機==========")
                price = input("商品の価格は？ > ").lower()
                if price == "clear":
                    clear_screen()
                    continue
                elif price in ("q", "end", "exit"):
                    end_data = end_program()
                    if end_data == False:
                        loooop = False
                        break
                    elif end_data == True:
                        print("メニューに戻ります...")
                        time.sleep(2)
                        break

                print("\n計算はどっち？")
                print("[1. ? ％割引 , 2. ? 割引]")

                user_select_dis = input(">").lower()
                if user_select_dis == "clear":
                    clear_screen()
                    continue
                elif user_select_dis in ("q", "end", "exit"):
                    end_data = end_program()
                    if end_data == False:
                        loooop = False
                        break
                    elif end_data == True:
                        print("メニューに戻ります...")
                        time.sleep(2)
                        break
                try:
                    price = int(price)
                    user_select_dis = int(user_select_dis)
                except ValueError:
                    print("\n!>> 整数で入力してください")
                    time.sleep(2)
                    continue
                cal_count = 3
                err_2 = input_inspection(cal_count, user_select_dis)
                
                if user_select_dis == 1:
                    try:
                        percent = int(input("なん％引き？ > "))
                    except ValueError:
                        print("\n!>> 整数で入力してください")
                        time.sleep(2)
                        continue
                    data2 = discount_calculation_percent(price, percent)
                    print(f'{price}円を{percent}％引きすると__{data2}円__です。')
                else:
                    try:
                        wari = int(input("なん割引き？ > "))
                    except ValueError:
                        print("\n!>> 整数で入力してください")
                        time.sleep(2)
                        continue
                    data3 = discount_calculation(price, wari)
                    print(f'{price}円を{wari}割引きすると__{data3}円__です。')
                
        elif user_menu_input == 3:
            while True:
                print("\n==========CLI年号計算==========")
                print("[1.年を自動所得 , 2.手動で年を入力]")
                user_year_input = input(">").lower()

                if user_year_input == "clear":
                    clear_screen()
                    continue
                elif user_year_input in ("q", "end", "exit"):
                    end_data = end_program()
                    if not end_data:
                        loooop = False
                        break
                    else:
                        print("メニューに戻ります...")
                        time.sleep(2)
                        break
                try:
                    user_year_input = int(user_year_input)
                except ValueError:
                    print("\n!>> 整数で入力してください")
                    time.sleep(2)
                    continue

                year_count = 3
                err_3 = input_inspection(year_count, user_year_input)

                if user_year_input == 1:
                    now_data = datetime.now().year
                    data4 = auto_year_cal(now_data)
                
                elif user_year_input == 2:
                    user_year_data = input("指定の年 > ").lower()

                    if user_year_data == "clear":
                        clear_screen()
                        continue
                    elif user_year_data in ("q", "end", "exit"):
                        end_data = end_program()
                        if not end_data:
                            loooop = False
                            break
                        else:
                            print("メニューに戻ります...")
                            time.sleep(2)
                            break

                    try:
                        user_year_data = int(user_year_data)
                    except ValueError:
                        print("\n!>> 整数で入力してください")
                        time.sleep(2)
                        continue

                    data5 = auto_year_cal(user_year_data)
except KeyboardInterrupt:
    print("\n!>> 強制終了します。")