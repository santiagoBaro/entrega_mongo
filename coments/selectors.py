from collections import Iterable

from coments.models import Message, User


def get_users():
    return User.objects.all()


def get_messages():
    return Message.objects.all()


def get_message(id):
    return Message.objects.get(id=id)


def get_messages_by_user(user_mail):
    return Message.objects.filter(mail=user_mail)