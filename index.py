import requests
import json
import os
import config


def gpt(auth_headers):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    with open('body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f)) 
    resp = requests.post(url, headers=auth_headers, data=data)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )

    return resp.text

if __name__ == "__main__":
    if os.getenv('b1ghnehmnn3n3dvbqi90') is not None:
        iam_token = os.environ['b1ghnehmnn3n3dvbqi90']
        headers = {
            'Authorization': f'Bearer {iam_token}',
        }
    elif os.getenv('AQVNz9XUQGq4KhejXKZ-8PLoDVwLZrPGARRazGnK') is not None:
        api_key = os.environ['AQVNz9XUQGq4KhejXKZ-8PLoDVwLZrPGARRazGnK']
        headers = {
            'Authorization': f'Api-Key {api_key}',
        }
    else:
        print ('Eror')
        exit()

    print(gpt(headers))