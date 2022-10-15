from app.model.user import User
from app.utils.password_encryption import encrypt_password, compare_passwords
import time
from app.utils.backend_util import dict_to_json, datetime_strf
from app.utils.backend_error import NotFoundEmailException, UserIdOrEmailAlreadyExistedException, NotFoundUseridException, LoginFailedException, PasswordIncorrectException
from app.enums.user_role import UserRole


def user_signup_service(userdata):
    user_id_check = User.objects[:1](user_id=userdata['user_id'])
    email_check = User.objects[:1](email=userdata['email'])
    if user_id_check or email_check:
        raise UserIdOrEmailAlreadyExistedException()
    else:
        userdata['password'] = encrypt_password(
            userdata['password']).decode("utf-8")
        userdata['create_time'] = int(time.time())

        userdata_json = dict_to_json(userdata)
        user = User.from_json(userdata_json)
        user.role = UserRole.normal
        user.save()


def user_login_service(userdata):
    user_id = userdata['user_id']
    user_check = User.objects[:1](user_id=user_id)
    if not user_check:
        raise NotFoundUseridException()
    else:
        user = user_check.get(user_id=user_id)
        if not compare_passwords(userdata['password'], user.password):
            raise LoginFailedException()


def search_user_service():
    users = []
    for user in User.objects:
        user_data = user.to_json()
        user_data['create_time'] = datetime_strf(user.create_time)
        user_data['update_time'] = "" if user.update_time is None else datetime_strf(
            user.update_time)
        users.append(user_data)

    return users


def getuser_by_id_service(user_id):
    for user in User.objects[:1](user_id=user_id):
        user_data = user.to_json()
        user_data['create_time'] = datetime_strf(user.create_time)
        user_data['update_time'] = "" if user.update_time is None else datetime_strf(
            user.update_time)
        return user_data


def update_user_service(user, user_id):
    old_user = User.objects(user_id=user_id)
    update_time = int(time.time())
    if old_user:
        old_user = old_user.get(user_id=user_id)
        userdata_json = dict_to_json(user)
        new_user = User().from_json(userdata_json)
        old_user.height = new_user.height
        old_user.weight = new_user.weight
        old_user.birthday = new_user.birthday
        old_user.update_time = update_time
        old_user.save()

def update_user_service_ethsum(user, user_id):
    old_user = User.objects(user_id=user_id)
    update_time = int(time.time())
    if old_user:
        old_user = old_user.get(user_id=user_id)
        userdata_json = dict_to_json(user)
        new_user = User().from_json(userdata_json)
        old_user.eth_sum = new_user.eth_sum
        old_user.update_time = update_time
        old_user.save()


def check_email_existed(email):
    email_check = User.objects[:1](email=email)
    if not email_check:
        raise NotFoundEmailException()


def update_pwd_service(userdata, query_index):
    update_time = int(time.time())
    if "email" in userdata.keys():
        user = User.objects.get(email=query_index)
        user.update_time = update_time
        user.password = encrypt_password(
            userdata['password']).decode("utf-8")
        user.save()
    else:
        user = User.objects.get(user_id=query_index)
        if compare_passwords(userdata['old_password'], user.password):
            user.password = encrypt_password(
                userdata['new_password']).decode("utf-8")
            user.update_time = update_time
            user.save()
        else:
            raise PasswordIncorrectException()
