from coments.models import Message, User


def create_user(
    *,
    mail: str,
    password: str
) -> User:
    user = User.objects.get_or_create(mail=mail, password=password)

    return user


def create_message(
    *,
    mail: str,
    message: str
) -> Message:
    user = User.objects.filter(mail=mail)[0]
    if user:
        message = Message.objects.create(user=user.mail, message=message)

    return message


def react_message(
    *,
    reaction: str,
    message_id: int
) -> User:
    message = Message.objects.filter(id=message_id)[0]
    if message:
        if reaction == "like":
            message.likes = message.likes + 1
        else:
            message.dislikes = message.dislikes + 1

    message.save()
    return message
