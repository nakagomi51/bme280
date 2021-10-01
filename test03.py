#!/usr/bin/python
# -*- coding: utf-8 -*-

import bme280_custom
import time
from datetime import datetime
import json
import requests

try:
	while True:

		#現在の日付、時間を取得
		pub_date = datetime.now().strftime("%Y/%m/%d")
		pub_time = datetime.now().strftime("%H:%M:%S")

		#センサーから温度、湿度、気圧を取得
		pub_temp = bme280_custom.compensate_T()
		pub_pres = bme280_custom.compensate_P()
		pub_humi = bme280_custom.compensate_H()


		payload = {}

		dict = {
			"保存日時": pub_date+" "+pub_time,
			'温度': pub_temp,
			'湿度': pub_humi,
			'気圧': pub_pres
		}

		#PowerBIサービスへデータを送信
		#	'https://api.powerbi.com/beta/(PowerBIサービスのID)'
		response = requests.post(
			'https://api.powerbi.com/beta/3e9e6dd6-1d14-41df-bb88-5ef504476de7/datasets/e69b0b63-0841-4b0c-93e7-e279a7242e1f/rows?key=oDYBMokAx49LPznLsM1FQmyOCQzw3xNxwmJsXE8LVKOcwIX3Dwz%2BYih0higARHkvfaMTI%2BTrXPj54dmF2AzN4g%3D%3D',
			json.dumps(dict),
			headers={'Content-Type': 'application/json'}
		)

		#スリープ
		time.sleep(3.0)

except KeyboardInterrupt:
	pass
