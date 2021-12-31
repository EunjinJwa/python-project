import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token='5057469943:XXXXXXXXXX')
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220103"

def job_function():
    html = requests.get(url)
    # print(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    print(imax)
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        print("IMAX 예매가 열렸습니다.")
        bot.sendMessage(chat_id= 5015230730, text=title + ' IMAX 예매가 열렸습니다. ')
        sched.pause()       # scheduler 중단
    else:
        print("IMAX 예매가 아직 열리지 않았습니다.")

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=10)
sched.start()





