import subprocess
from datetime import datetime
import time
from plyer import notification
try:
    def ping_test():
        print("===========[🌐 Furi_NetWatch]===========")
        while True:
            #[hostはping先なので変更したいときはここを変更して]
            #変更したら下の失敗バージョンも変えたほうがいいかも
            host = "8.8.8.8"
            
            result = subprocess.run(
                ["ping", "-n", "1", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            current_datetime = datetime.now()
            #フォーマット。左のログの書き方を変えれるよ。
            #例[[ 2025-10-31 20:41:41 ]] <<<-- これ初期状態の例です。
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print("[",formatted_datetime,"] ",end="")

            if result.returncode == 0:
                #通常モードでの通信成功メッセージ
                print(f"✅ ネットワーク通信ができました")
                time.sleep(30)
            else:
                #通常モードの通信失敗メッセージ
                print(f"❌ {host} に到達できません")
                print("\n⚠️ 再接続チェックを開始(通信頻度が上がります)...\n")
                notification.notify(
                    title="⚠️ネットワークの接続に失敗",
                    message="8.8.8.8に接続を試みましたが接続ができません。インターネットが途切れた可能性があります。通信頻度が上がります。",
                    app_name="Furi_NetWatch", #名前は変えないで :(
                    timeout=10
                    )
                err_ping_test()
    
    def err_ping_test():
        while True:
            #失敗したとき用の関数。ここもhostを変えるとping先を変更化。
            host = "8.8.8.8"
            result = subprocess.run(
                ["ping", "-n", "1", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print("[",formatted_datetime,"] ",end="")

            if result.returncode == 0:
                #失敗バージョンからネットワークつながって復旧したときのメッセージ
                print(f"✅ ネットワークが復旧しました 通常モードへ移行います")
                notification.notify(
                    title="✅ネットワークが復旧しました!",
                    message="インターネット接続が確認されました 通信頻度を通常に戻します",
                    app_name="Furi_NetWatch",#名前は変えないで :(
                    timeout=10
                )
                
                time.sleep(5)
                ping_test()
            else:
                print(f"❌ 接続できません 再接続待機中...")
                time.sleep(5)


    if __name__ == "__main__":
        ping_test()



except KeyboardInterrupt:
    print("停止します")