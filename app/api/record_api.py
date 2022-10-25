from flask import make_response
from flask_login import login_required
from flasgger import swag_from
import logging
from http import HTTPStatus
from . import api
from app.service.record_service import search_records_by_userid, get_count
from app.utils.backend_error import BackendException
from app.api.api_doc import record_search as search_doc, record_count as count_doc
from app.utils.backend_decorator import role_check
from app.enums.user_role import UserRole

root_path = "/record"
logger = logging.getLogger(__name__)

# # 新增運動測試紀錄


# @api.route(root_path, methods=['POST'])
# def add_record():
#     data = request.get_json()
#     message = ""
#     status = 200
#     try:
#         (analyze, has_record) = __analyze_record(data)
#         data['pr'] = analyze['pr']
#         data['test_result'] = analyze['test_result']
#         data.pop('gender', None)
#         data.pop('age', None)
#         add_record_service(data)
#         data.pop('angles', None)
#         data['difference'] = analyze['difference'] if has_record else None
#         message = "新增紀錄成功"
#         logger.info(message)
#     except Exception as e:
#         data = {}
#         match e.__class__.__name__:
#             case _:
#                 logger.error(str(e))
#                 e = BackendException()
#         (message, status) = e.get_response_message()
#     response = make_response({"message": message, "data": data}, status)
#     return response

# 查詢使用者所有測試紀錄


@api.route(f"{root_path}/<user_id>", methods=['GET'])
@login_required
@role_check(role=UserRole.manager.value)
@swag_from(search_doc)
def search_record(user_id):
    """查詢使用者所有測試紀錄
    """
    try:
        result = search_records_by_userid(user_id)
        message = "查詢成功"
        logger.info(message)
        return make_response({"message": message, "data": result}, HTTPStatus.OK)
    except Exception as e:
        match e.__class__.__name__:
            case _:
                logger.error(str(e))
                e = BackendException()
        (message, status) = e.get_response_message()
        return make_response({"message": message}, status)

# 查詢使用者測試筆數


@api.route(f"{root_path}/count/<user_id>", methods=['GET'])
@login_required
@role_check(role=UserRole.manager.value)
@swag_from(count_doc)
def get_record_count(user_id):
    """查詢使用者測試筆數
    """
    try:
        result = get_count(user_id)
        message = "查詢使用者測試筆數成功"
        logger.info(message)
        return make_response({"message": message, "count": result}, HTTPStatus.OK)
    except Exception as e:
        match e.__class__.__name__:
            case _:
                logger.error(str(e))
                e = BackendException()
        (message, status) = e.get_response_message()
        return make_response({"message": message}, status)

# # 測試結果數據分析


# def __analyze_record(data):
#     # the parameters like (user_id, age, part, gender, times)
#     data = request.get_json()
#     result = {}
#     has_record = False
#     standard = get_standard_times_service(data)
#     record = search_record_service(data['user_id'], data['part'], True)
#     times = data['times']
#     compare = [s for s in standard if times >= s]
#     difference = times - record[0]['times'] if len(record) > 0 else -999
#     pr = len(compare) * 5
#     test_result = ""
#     if pr > 75:
#         test_result = "很棒"
#     elif pr > 20:
#         test_result = "正常"
#     else:
#         test_result = "待加強"

#     result = {
#         "pr": pr,
#         "test_result": test_result
#     }
#     if difference > -100:
#         has_record = True
#         result["difference"] = difference
#     logger.info("分析成功")
#     return (result, has_record)
