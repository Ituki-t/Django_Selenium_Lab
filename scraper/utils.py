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


def parse_int_year(year_str):
    """
    # '2025年度' のような文字列から整数の年度を抽出して返す.
    - ex)'2025年度' -> 2025

    - /d --- 数字にマッチする
    - {4} --- 直前の文字が4回繰り返される
    - (\d{4}) --- 4桁の数字にマッチし,
    - .group(1) --- 丸括弧で囲んだ第1キャプチャを取り出します（ここでは '2025'）
    """

    result = int(re.search(r'(\d{4})', year_str).group(1))
    return result



def dedup_keep_latest_year(syllabus_records):
    """
    Syllabus オブジェクトのリストから, 同じ course_name を持つものを1つにまとめる.
    まとめる際には, 最新の course_year を持つものを残す.
    """
    deduped_dict = {}
    for syllabus in syllabus_records:
        course_name = syllabus['lecture']
        course_year = syllabus['year']

        # (ex) '2025年度' -> 2025
        # course_year_int = parse_int_year(course_year)
        # deduped_dict_year = parse_int_year(deduped_dict[course_name]['year'])

        if course_name in deduped_dict:
            # (ex) '2025年度' -> 2025
            course_year_int = parse_int_year(course_year)
            deduped_dict_year_int = parse_int_year(deduped_dict[course_name]['year'])

            # すでに同じ course_name が存在する場合，年度を比較して新しいほうを残す
            if course_year_int > deduped_dict_year_int:
                deduped_dict[course_name] = syllabus
        else:
            deduped_dict[course_name] = syllabus

    return list(deduped_dict.values())