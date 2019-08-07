#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import string
import rc


host = 'localhost'   # Raspberry PiのIPアドレス
port = 10500         # juliusの待ち受けポート

# パソコンからTCP/IPで、自分PCのjuliusサーバに接続
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

data = ""
rc.setup()
while True:

    # "/RECOGOUT"を受信するまで、一回分の音声データを全部読み込む。
	while (string.find(data, "\n.") == -1):
		data = data + sock.recv(1024)

    # 音声XMLデータから、<WORD>を抽出して音声テキスト文に連結する。
	strTemp = ""
	for line in data.split('\n'):
		index = line.find('WORD="')

		if index != -1:
			line = line[index + 6:line.find('"', index + 6)]
		if line != "[s]":
			strTemp = strTemp + line

	if "ぜんしん" in strTemp:
		print("result: 前進")
		rc.forward()
	if "こうたい" in strTemp:
		print("result: 後退")
		rc.back()
	if "ていし" in strTemp:
		print("result: 停止")
		rc.stop()
	if "みぎかーぶ" in strTemp:
		print("result: 右カーブ")
		rc.rightTurn()
	if "ひだりかーぶ" in strTemp:
		print("result: 左カーブ")
		rc.leftTurn()
	if "みぎかいてん" in strTemp:
		print("result: 右回転")
		rc.rightRoll()
	if "ひだりかいてん" in strTemp:
		print("result: 左回転")
		rc.leftRoll()
	if "しゅうりょう" in strTemp:
		print("result: 終了")
		rc.destroy()
		exit()

	data = ""
