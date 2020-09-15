# !/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\python\spider\.vscode\music_spider\main.py
# Project: e:\code\python\spider\.vscode\music_spider
# Created Date: Saturday, September 12th 2020, 10:10:32 pm
# Author: rz
# -----
# Last Modified:
# Modified By:
# -----
# Copyright (c) 2020 rz WTI bupt
#
# All shall be well and all shall be well and all manner of things shall be well.
# Nope...we're doomed!
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###

import requests
import json
import os
import random
import time


def download(url, name):
    if not os.path.exists('music'):  # 创建文件夹
        os.mkdir('music')
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}  # 设置头文件，简单的爬虫伪装
    path = 'music/' + name.replace('/', '').replace('\\', '').replace(':', '').replace(
        '*', '').replace('"', '').replace('<', '').replace('|', '').replace('?', '').replace(',', '')  # 设置路径和文件名，并去除文件名中不允许的字符

    if not os.path.exists(path) or os.path.getsize(path) == 0:  # 文件不存在或大小为0时开始下载
        # 请求时需关闭verify属性，否则会报SSL认证错误
        r = requests.get(url, headers=header, verify=False)
        # r.encoding = r.apparent_encoding
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print(name + '保存成功')
        # time.sleep(random.random()) # 下载完成后随机休眠，对服务器也好
    else:
        print("文件已存在")


def parse(lists):
    for lis in lists:
        name = lis['name']

        if 'lrc' in lis:
            download(lis['lrc'], name+'.lrc')
        if 'url_flac' in lis:
            download(lis['url_flac'], name+'.mp3')
        elif 'url_320' in lis:
            download(lis['url_320'], name + '.mp3')
        elif 'url_128' in lis:
            download(lis['url_128'], name + '.mp3')
        elif 'url' in lis:
            download(lis['url'], name + '.mp3')
        else:
            print('暂无资源')


def main():
    with open('music_list.json', 'r', encoding='utf-8') as raw:
        music_lists = json.load(raw)['data']['list']
        parse(music_lists)


if __name__ == '__main__':
    main()
