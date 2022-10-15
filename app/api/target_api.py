# from flask import request, make_response
# import logging
# from . import api
# from app.service.target_service import add_target_service, get_target_service, update_target_times_service,check_target_is_expired, get_target_by_started
# from app.utils.backend_error import BackendException
# from flasgger import swag_from
# from app.api.api_doc import target_get as get_doc

# root_path = "/target"
# logger = logging.getLogger(__name__)

# # 新增個人計劃表


# @api.route(root_path, methods=['POST'])
# def add_target():
#     data = request.get_json()
#     message = ""
#     status = 200
#     try:
#         add_target_service(data)
#         message = "新增訓練計劃表成功"
#         logger.info(message)
#     except Exception as e:
#         match e.__class__.__name__:
#             case _:
#                 logger.error(str(e))
#                 e = BackendException()
#         (message, status) = e.get_response_message()
#     response = make_response({"message": message}, status)
#     return response

# # 查詢個人計劃表


# @api.route(f"{root_path}/<user_id>", methods=['GET'])
# @swag_from(get_doc)
# def get_target(user_id):
#     """查詢個人計劃表
#     """
#     result = []
#     message = ""
#     status = 200
#     try:
#         result = get_target_service(user_id)
#         message = "查詢訓練計劃表成功"
#         logger.info(message)
#     except Exception as e:
#         match e.__class__.__name__:
#             case _:
#                 logger.error(str(e))
#                 e = BackendException()
#         (message, status) = e.get_response_message()
#     response = make_response({"message": message, "data": result}, status)
#     return response

# @api.route(f"{root_path}/<user_id>/<target_date>", methods=['POST'])
# def update_target(user_id, target_date):
#     data = request.get_json()
#     message = ""
#     status = 200
#     try:
#         update_target_times_service(user_id, target_date, data)
#         message = "更新訓練計劃表成功"
#         logger.info(message)
#     except Exception as e:
#         match e.__class__.__name__:
#             case _:
#                 logger.error(str(e))
#                 e = BackendException()
#         (message, status) = e.get_response_message()
#     response = make_response({"message": message}, status)
#     return response

# @api.route(f"{root_path}/existed/<user_id>", methods=['GET'])
# def target_check_existed(user_id):
#     result = False
#     message = ""
#     status = 200
#     try:
#         result = check_target_is_expired(user_id)
#         message = "確認訓練表成功"
#         logger.info(message)
#     except Exception as e:
#         match e.__class__.__name__:
#             case _:
#                 logger.error(str(e))
#                 e = BackendException()
#         (message, status) = e.get_response_message()
#     response = make_response({"message": message, "data": result}, status)
#     return response


# # 檢查是否為剛建立的訓練表
# @api.route(f"{root_path}/started/<user_id>", methods=['GET'])
# def target_getby_started(user_id):
#     result = False
#     message = ""
#     status = 200
#     try:
#         result = get_target_by_started(user_id)
#         message = "確認訓練表成功"
#         logger.info(message)
#     except Exception as e:
#         match e.__class__.__name__:
#             case _:
#                 logger.error(str(e))
#                 e = BackendException()
#         (message, status) = e.get_response_message()
#     response = make_response({"message": message, "data": result}, status)
#     return response