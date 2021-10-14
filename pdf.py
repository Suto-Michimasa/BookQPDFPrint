# Step1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# Step2


def PrintSetUp():
    # 印刷としてPDF保存する設定
    chopt = webdriver.ChromeOptions()
    appState = {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account": ""
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isLandscapeEnabled": True,  # 印刷の向きを指定 tureで横向き、falseで縦向き。
        "pageSize": 'A4',  # 用紙タイプ(A3、A4、A5、Legal、 Letter、Tabloidなど)
        # "mediaSize": {"height_microns": 355600, "width_microns": 215900}, #紙のサイズ　（10000マイクロメートル = １cm）
        # "marginsType": 0, #余白タイプ #0:デフォルト 1:余白なし 2:最小
        # "scalingType": 3 , #0：デフォルト 1：ページに合わせる 2：用紙に合わせる 3：カスタム
        # "scaling": "141" ,#倍率
        # "profile.managed_default_content_settings.images": 2,  #画像を読み込ませない
        "isHeaderFooterEnabled": False,  # ヘッダーとフッター
        "isCssBackgroundEnabled": True,  # 背景のグラフィック
        # "isDuplexEnabled": False, #両面印刷 tureで両面印刷、falseで片面印刷
        # "isColorEnabled": True, #カラー印刷 trueでカラー、falseで白黒
        # "isCollateEnabled": True #部単位で印刷
    }

    prefs = {'printing.print_preview_sticky_settings.appState':
             json.dumps(appState),
             "download.default_directory": "~/Downloads"
             }  # appState --> pref
    chopt.add_experimental_option('prefs', prefs)  # prefs --> chopt
    chopt.add_argument('--kiosk-printing')  # 印刷ダイアログが開くと、印刷ボタンを無条件に押す。
    return chopt

# Step3


def main_WebToPDF(BlogURL):
    # Web ページもしくはhtmlファイルをPDFにSeleniumを使って変換する
    chopt = PrintSetUp()
    driver_path = "./chromedriver"  # webdriverのパス
    driver = webdriver.Chrome(executable_path=driver_path, options=chopt)
    driver.implicitly_wait(10)  # 秒 暗示的待機
    driver.get(BlogURL)  # ブログのURL 読み込み
    # ページ上のすべての要素が読み込まれるまで待機（15秒でタイムアウト判定）
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    driver.execute_script('return window.print()')  # Print as PDF
    time.sleep(10)  # ファイルのダウンロードのために10秒待機
    driver.quit()  # Close Screen


 # Step4
if __name__ == '__main__':
    BlogURLList = ['https://degitalization.hatenablog.jp/entry/2020/05/15/084033',
                   'https://note.com/makkynm/n/n1343f41c2fb7',
                   "file:///Users/makky/Documents/Python/Sample.html"]
    for BlogURL in BlogURLList:
        main_WebToPDF(BlogURL)
