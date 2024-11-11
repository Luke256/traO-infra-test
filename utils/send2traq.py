import requests
import hashlib
import hmac
from config import WEBHOOK_ID, WEBHOOK_SECRET

def send2traq(message):
    m = hmac.new(
        WEBHOOK_SECRET.encode(),
        message.encode(),
        hashlib.sha1
    )

    signature = m.hexdigest()

    headers = {
        "X-Traq-Signature": signature,
        'Content-Type': 'text/plain; charset=utf-8'
    }

    url = f"https://q.trap.jp/api/v3/webhooks/{WEBHOOK_ID}"

    res = requests.post(url, headers=headers, data=message)