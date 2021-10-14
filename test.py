import time
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome()            # Chromeを準備
driver.get('https://www.google.com/')  # Googleを開く
time.sleep(5)                          # 5秒間待機
driver.quit()                          # ブラウザを閉じる
