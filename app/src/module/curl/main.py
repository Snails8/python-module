import json

import requests

webhook_url_dev = 'xxx'
message = {"text": "Dev環境テストメッセージ"}
response = requests.post(webhook_url_dev, data=json.dumps(message), headers={'Content-Type': 'application/json'})
if response.status_code == 200:
    print("Dev環境へのメッセージ送信に成功しました。")
else:
    print(f"Dev環境へのメッセージ送信に失敗しました。ステータスコード: {response.status_code}")

webhook_url_prod = 'xxx'
message = {"text": "Prod環境テストメッセージ"}
response = requests.post(webhook_url_prod, data=json.dumps(message), headers={'Content-Type': 'application/json'})
if response.status_code == 200:
    print("Prod環境へのメッセージ送信に成功しました。")
else:
    print(f"Prod環境へのメッセージ送信に失敗しました。ステータスコード: {response.status_code}")
