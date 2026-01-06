import time

import requests
import json


def refactoring_text(text):

    # для того чтобы на сервак не сохранялись дублированные статьи, на сервак отправлется текст с оригинальным названием
    # и переведенной статьей
    # на сервере название переводиться полностью, а тексе по словно
    prompt = f"Reduce the article to 300 words and return this text only on Russian. Text: {text}"

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyCo2y0CiSaTNdri5Cxn7d0QHI3C_mK29ug"

    payload = json.dumps({
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


    print("AI RESPONSE")
    print(response.status_code)

    try:
        print("response.text"),
        print(response.text)

    except Exception:
        print("response"),
        print(response)
        print("Exception")
        print(Exception)

    counter = 0
    while str(response.status_code) == str(429) and counter < 100:
        time.sleep(30)
        response = requests.request("POST", url, headers=headers, data=payload)

        print("AI RESPONSE")
        print(response.status_code)

        try:
            print("response.text"),
            print(response.text)

        except Exception:
            print("response"),
            print(response)
            print("Exception")
            print(Exception)

    if str(response.status_code) == str(201) or str(response.status_code) == str(200):
        return json.loads(response.text)['candidates'][0]['content']['parts'][0]['text']
    else:
        return False


def post_request(json_text):
    #url = "http://127.0.0.1:8000/api/v1/save_original_articles"
    # url = "http://0.0.0.0:81//api/v1/save_original_articles"
    url = "http://93.85.88.38:82/api/v1/save_original_articles"


    payload = json.dumps(json_text)
    headers = {
        # 'Authorization': 'Token 2eb2d23fcf6e5abf15c6914ce2cc3df3d6bf43d3',
        'Authorization': 'Token e5282c2098165fe1b4f9d8e2ef55bb4e4fa6414f', # http://93.85.88.38:82
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)

    return response.status_code