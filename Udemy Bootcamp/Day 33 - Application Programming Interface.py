import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)

# 여기까지는 response code만 받음
# <Response [200]>

Resonse Code

1XX: Hold On
2XX: Here You Go
3XX: Go Away
4XX: You Screwed Up
5XX: Server Screwed Up

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    print(f"Status code: {response.status_code}. Error")
elif ....    
# 이렇게 모든 status code를 나열할 수는 없으니 response 모듈을 사용
response.raise_for_status()
# json data 가져오기
response.json()
print(response.json()["iss_position"]["longitude"])  # Dictionary 객체로 활용 가능

# ISS 위치 찾기
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

# Kanye Quote
def get_quote():
    resp = requests.get(url="https://api.kanye.rest")
    resp.raise_for_status()
    quote_data = resp.json()["quote"]
    canvas.itemconfig(quote_text, text=quote_data)
    if resp.status_code != 200:
        raise Exception("Error in calling the API.")

# 일몰 일출, 현재 시각

import requests
from datetime import datetime

MY_LAT = 37.490394
MY_LONG = 127.042262

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

resp = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters) # params= 로 변수 추가
resp.raise_for_status() # status 확인
data = resp.json() # json response 파싱
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] # split으로 UNIX 타임 구분
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now() # 현재일자시각
print(time_now.hour)

Project
# ISS가 내 머리 위에 오면 이메일 알림 전송

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "tk_na@naver.com"
MY_PASSWORD = "보안상 생략"

MY_LAT = 보안상 생략
MY_LONG = 보안상 생략

# ISS가 현재 내 위치에 근접했는지 판단
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

# 현재 밤인지 판단
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Seoul" # 시간대 변수 추가
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset <= time_now or time_now <= sunrise: # 24시간인점 주의
        return True

while True:
    time.sleep(60) # 1분에 한번씩 실행
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.naver.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: 위를 보시오.\n\n국제우주정거장 접근중"
        )
