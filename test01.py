#!/usr/bin/python
# -*- coding: utf-8 -*-

import bme280_custom
import time
from datetime import datetime

try:
	while True:

		#現在の日付、時間を取得
		pub_date = datetime.now().strftime("%Y/%m/%d")
		pub_time = datetime.now().strftime("%H:%M:%S")

		#センサーから温度、湿度、気圧を取得
		pub_temp = bme280_custom.compensate_T()
		pub_pres = bme280_custom.compensate_P()
		pub_humi = bme280_custom.compensate_H()

		#画面に情報表示
		print ("Time:" ,pub_time)	#時間
		print ("Temp:", pub_temp)	#温度
		print ("Humi:", pub_humi)	#湿度
		print ("Pres:", pub_pres)	#気圧
		print ("-------------------------")

		#スリープ
		time.sleep(3.0)

# Ctrl-Cをキャッチ 
except KeyboardInterrupt:
	pass
