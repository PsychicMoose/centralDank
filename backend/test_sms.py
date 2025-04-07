import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centraldank.settings')
django.setup()

from core.utils import send_sms

sid = send_sms("This is CentralDank. You are the mission.")
print(f"Message sent! SID: {sid}")
