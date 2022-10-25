from datetime import datetime
from app.model.record import Record
from app.utils.backend_util import datetime_strf_yyyymmddHHMMSS


# def add_record_service(record_data):
#     record_data['create_time'] = get_now_timestamp()
#     record_json = dict_to_json(record_data)
#     record = Record().from_json(record_json)
#     record.save()


# def get_record_before_last_target(user_id, target_create_time, part):
#     record = Record.objects(user_id=user_id, part=part, create_time__lt=target_create_time).order_by(
#         '-create_time').first()
#     return record.to_json()


# def get_standard_times_service(data):
#     times = []
#     age = max(data['age'], 65)
#     gender = Gender(data['gender'])
#     part = TrainingPart(data['part'])
#     for standard in Standard.objects(age__lte__0=age, age__gte__1=age, gender=gender, part=part):
#         times = standard.times

#     if len(times) == 0:
#         raise Exception('occurred some unexpected accident')

#     return times


def search_records_by_userid(user_id):
    records = Record.objects(user_id=user_id).order_by('-create_time')
    return __records_to_json(records)

def get_count(user_id):
    return len(Record.objects(user_id=user_id))


def __records_to_json(records):
    result = []
    for record in records:
        record_data = record.to_json()
        record_data['create_time'] = datetime_strf_yyyymmddHHMMSS(record.create_time)
        result.append(record_data)
    return result
