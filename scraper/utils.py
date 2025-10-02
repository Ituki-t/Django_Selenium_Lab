from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import subprocess

import re

def make_selenium_driver():
    """
    ChromeDriverの設定を行い、Selenium WebDriverのインスタンスを返す。
    "--headless=new" --- UI を表示せずバックグラウンドで動く
    "--disable-notifications" --- 通知を無効化
    "--disable-features=PushMessaging,Notifications" --- 通知を無効化
    "excludeSwitches", ["enable-logging"] --- 不要な DevTools ログを抑制
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=PushMessaging,Notifications")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(
        ChromeDriverManager().install(),
        log_output=subprocess.DEVNULL
    )
    return webdriver.Chrome(service=service, options=options)


def split_whitespace(text):
    """
    文字列を半角スペース, 全角スペースで分割してリストで返す
    - re --- 正規表現モジュール
    - r'...' --- raw文字列
    - [...] --- 文字クラス
    - \s --- 空白文字 (半角スペース, タブ, 改行など)
    - \u3000 --- 全角スペース
    - + --- 直前の文字が1回以上繰り返される
    - r'[\s\u3000]+' --- 半角スペース, 全角スペースが1回以上繰り返される部分で分割
    """

    result = re.split(r'[\s\u3000]+', text.strip())
    return result