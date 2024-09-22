from dataclasses import dataclass
import datetime


def validate_user_on_server(user):
    return 'some check data'


def check_username(user_name):
    return 'some check data'


def check_birthday(bd):
    return 'some check data'


def validated_user(user):
    """проверяем юзера, райзит (raise) исключение, если с ним что то"""
    validate_user_on_server(user)
    check_username(user)
    check_birthday(user)


# dataclass
@dataclass()
class User:
    username: str
    created_at: datetime.datetime
    birthday: datetime.datetime | None  # присваивается по-умолчанию значение None, если не передана дата.


def validated_user_class(user: User):
    """проверяем юзера, райзит (raise) исключение, если с ним что то"""
    validate_user_on_server(user)
    check_username(user)
    check_birthday(user.birthday)  # Если необходимо, можно в функции обратится к атрибутам класса.
