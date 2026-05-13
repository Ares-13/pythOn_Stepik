import requests
import pprint

# response = requests.get("https://google.com")
#response = requests.get("https://api.github.com")

# HTTP статус-коды:
# 1xx - информационные
# 2xx - успешные
# 3xx - перенаправление
# 4xx - клиентские ошибки
# 5xx - серверные ошибки

#print(response.status_code) #  выводит статус
# print(response.ok) #  выводит True, если меньше 400

# if response.ok:
#     print("Сделай что-нибудь...")

#print(response.text) # ответ сервера в виде строки
# print(response.content) # если ответ сервера файл

# response_json = response.json()
# pprint.pprint(response_json) # ответ будет в виде словаря

# Cookies
# cookies = {'session_token': '123456789'}
# response = requests.get('https://httbin.org/cookies', cookies=cookies)
# print(response.text)


# Получение картинки
img_url = 'https://sun9-59.userapi.com/s/v1/ig2/J7rYi0A20xBAu9iPliXP4XTaZigGjC_VacRhsjkszCsKUN_t8ViDXFqUgk9ksa9Q6WBYiJzLB-QeitEUzGN3SFV_.jpg?quality=96&as=32x31,48x47,72x70,108x105,160x156,240x234,360x351,480x468,540x526,640x624,720x702&from=bu&u=4sg_9F4ELoykfCS-rMl3U0zmQLL9q43M3Q260cGrPPs&cs=720x09'
res = requests.get(img_url)

with open('img.png', 'wb') as file:
    file.write(res.content)