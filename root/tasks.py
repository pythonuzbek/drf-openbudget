import httpx
from celery import shared_task
import requests
BOT_API = 'https://api.telegram.org/bot5344490283:AAF2-eAVHwVCevHdAyR4V_VKZVPcDhYB5go/sendMEssage'
GROUP_ID = -1001963932495


@shared_task()
def notify_telegram():
    data = {
        'chat_id': GROUP_ID,
        'text': "Groupp SAlom"
    }
    respone = requests.post(BOT_API,data)
    print(respone.status_code, respone.json())
