from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from weather import settings
import time
from django.utils import timezone
from .models import *
from django import dispatch


User = get_user_model()


@receiver(post_save, sender = User)

def welcome_user_mail(sender, instance, created, **kwargs):

    if created:
        if instance.role == 'user':
            subject = 'Double D welcomes you'

            message = f"Dear {instance.first_name}, welcome to my system. My name is Double D. I am here to help you. If you have any question"

            print("sending mail")
            time.sleep(5)
            print('mail sent')

            print(f"""

            subject: {subject}
            message: {message}

            """)
        else:
            print("Admin created")
            print(f"""

            subject: Double D welcomes Admin
            message: Dear Admin, welcome to the Admin dashboard. My name is Double D. I am here to help you. If you hve any questions, please feel free to ask

            """)

# @receiver(data_signal)
# def 