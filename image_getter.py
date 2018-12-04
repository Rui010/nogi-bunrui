import requests
import bs4
import datetime
import os
import re
import time
import datetime
import json


# HTML要素の取得
def get_html(url):
    response = requests.get(url)
    text = response.text
    return text

# 画像リンクを取得
def scan_images(text, selector):
    imgs_url = []
    soup = bs4.BeautifulSoup(text, "html.parser")
    if soup.select(selector)is None:
        return []
    block = soup.select(selector)[0]
    imgs = block.findAll("img")
    for img in imgs:
        imgs_url.append(img.get("src"))
    return imgs_url

def get_image(path, filename, url):
    if not os.path.exists(path):
        os.mkdir(path)

    file_name = os.path.join(path, filename + ".jpg")

    try:
        response = requests.get(url)
        image = response.content
        with open(file_name, "wb") as f:
            f.write(image)

    except:
        print("url error..." + url)

if __name__ == "__main__":
    # 設定ファイルは保存先Path, 対象URL, CSSセレクターが要素
    with open("./url_list.json") as f:
        url_list = json.load(f)

    for i, l in enumerate(url_list):
        print("Progress..." + str(i+1) + " / " + str(len(url_list)))
        url = l["URL"]
        path = l["path"]
        selector = l["selector"]

        img_urls = scan_images(get_html(url), selector)
        for j, img_url in enumerate(img_urls):
            filename = str(int(time.time()))
            get_image(path, filename, img_url)
            time.sleep(5)
            print("%d ％" % (j / len(img_urls)*100))
