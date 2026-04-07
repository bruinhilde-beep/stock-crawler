from playwright.sync_api import sync_playwright
import requests
from datetime import datetime

# ================== 設定區 ==================
LINE_CHANNEL_TOKEN = os.getenv("LINE_CHANNEL_TOKEN")   # 從 GitHub Secrets 自動取得

# 要發送訊息的 USER ID（你的 LINE 官方帳號好友的 User ID）
# 目前先用你自己的 User ID，之後再教你怎麼找
YOUR_USER_ID = "bruinhilde"   

def send_line_message(message):
    if not LINE_CHANNEL_TOKEN or not YOUR_USER_ID:
        print("⚠️ LINE Token 或 User ID 未設定")
        return
    
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_TOKEN}"
    }
    data = {
        "to": YOUR_USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("✅ LINE 訊息發送成功")
    else:
        print(f"❌ LINE 發送失敗: {response.status_code} {response.text}")

# ================== 主要爬蟲 ==================
def main():
    print(f"🚀 爬蟲開始執行 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # 範例：打開公開資訊觀測站
            page.goto("https://mops.twse.com.tw/mops/web/t05st01", timeout=60000)
            page.wait_for_timeout(5000)
            
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            message = f"📢 爬蟲測試成功\n時間：{current_time}\n狀態：正常運行"
            
            send_line_message(message)
            
            browser.close()
            
    except Exception as e:
        error_msg = f"❌ 爬蟲執行錯誤\n時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n錯誤：{str(e)}"
        send_line_message(error_msg)
        print(error_msg)

if __name__ == "__main__":
    main()
