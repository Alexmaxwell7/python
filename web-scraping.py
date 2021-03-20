import requests

url = 'https://timesofindia.indiatimes.com/videos?from=mdr#_ga=2.135146417.1486211953.1616041818-amp-nGGGc9pnM-cmw7Tkv3GejPTeBzV0DH7wluFUS3V4fKzxYIGy1VBx8dWDTT403H36'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',

    'Referer': 'https://timesofindia.indiatimes.com/'

}

response = requests.get(url=url, headers=headers).json()

print(type(response))