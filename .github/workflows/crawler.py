from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
import os

def main():
    print("開始執行爬蟲...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 範例：打開公開資訊觀測站
        page.goto("https://mops.twse.com.tw/mops/web/t05st01")
        page.wait_for_timeout(3000)
        
        # 你之後可以把這裡改成你要抓的網站
        print("目前時間:", datetime.now().strftime("%Y-%m-%d %H:%M"))
        print("這裡可以放你的爬蟲邏輯...")
        
        browser.close()

if __name__ == "__main__":
    main()
