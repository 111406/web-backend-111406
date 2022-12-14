user_model = \
    {
        "User": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string"
                },
                "birthday": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "gender": {
                    "type": "string"
                },
                "height": {
                    "type": "number"
                },
                "weight": {
                    "type": "number"
                },
                "role": {
                    "type": "string"
                },
                "password": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "create_time": {
                    "type": "string"
                },
                "update_time": {
                    "type": "string"
                },
                "eth_account": {
                    "type": "string"
                },
                "eth_password": {
                    "type": "string"
                },
                "eth_sum": {
                    "type": "int"
                },
                "other_detail": {
                    "type": "string"
                },
            }
        }
    }

user_list = \
    {
        "UserList": {
            "type": "array",
            "items": user_model["User"]
        }
    }

record_model = \
    {
        "Record": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string"
                },
                "angles": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "sec": {
                                "type": "number"
                            },
                            "angle": {
                                "type": "number"
                            }
                        }
                    }
                },
                "times": {
                    "type": "number"
                },
                "fails": {
                    "type": "number"
                },
                "part": {
                    "type": "string"
                },
                "pr": {
                    "type": "string"
                },
                "test_result": {
                    "type": "string"
                },
                "create_time": {
                    "type": "string"
                },
            }
        }
    }

record_list = \
    {
        "RecordList": {
            "type": "array",
            "items": record_model["Record"]
        }
    }

todo_model = \
    {
        "UserTodo": {
            "type": "object",
            "properties": {
                "target_times": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "times": {
                                "type": "number"
                            },
                            "set": {
                                "type": "number"
                            },
                            "total": {
                                "type": "number"
                            }
                        }
                    }
                },
                "target_date": {
                    "type": "string"
                },
                "complete": {
                    "type": "boolean"
                },
                "actual_times": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "left": {
                                "type": "object",
                                "properties": {
                                    "times": {
                                        "type": "number"
                                    }
                                }
                            },
                            "right": {
                                "type": "number",
                                "properties": {
                                    "times": {
                                        "type": "number"
                                    }
                                }
                            },
                        }
                    }
                },
            }
        }
    }

target_model = \
    {
        "Target": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string"
                },
                "start_date": {
                    "type": "string"
                },
                "end_date": {
                    "type": "string"
                },
                "user_todos": {
                    "type": "array",
                    "items": todo_model["UserTodo"]
                },
            }
        }
    }

logrecord_model = \
    {
        "LogRecord": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string"
                },
                "ip": {
                    "type": "string"
                },
                "message": {
                    "type": "string"
                },
                "request_url": {
                    "type": "string"
                },
                "action_time": {
                    "type": "string"
                },
            }
        }
    }


user_signup = {
    "parameters": [
        {"name": "user_id", "in": "Body", "type": "string", "required": "true"},
        {"name": "password", "in": "Body", "type": "string", "required": "true"},
        {"name": "email", "in": "Body", "type": "string", "required": "true"},
        {"name": "gender", "in": "Body", "type": "number", "required": "true"},
        {"name": "role", "in": "Body", "type": "number", "required": "true"},
        {"name": "height", "in": "Body", "type": "number"},
        {"name": "weight", "in": "Body", "type": "number"},
        {"name": "birthday", "in": "Body", "type": "string", "required": "true"},
        {"name": "institution", "in": "Body", "type": "string"},
        {"name": "other_detail", "in": "Body", "type": "string"},
    ], "responses": {
        "200": {
            "description": "?????????????????????",
            "examples": {
                "message": "????????????"
            }
        },
        "500": {
            "description": "?????????????????????",
        }
    }
}


user_login = {
    "parameters": [
        {"name": "user_id", "in": "Body", "type": "string", "required": "true"},
        {"name": "password", "in": "Body", "type": "string", "required": "true"},
    ], "responses": {
        "200": {
            "description": "?????????????????????",
            "examples": {
                "message": "????????????"
            }
        },
        "500": {
            "description": "?????????????????????",
        }
    }
}

user_logout = {
    "responses": {
        "200": {
            "description": "?????????????????????",
            "examples": {
                "message": "????????????"
            }
        },
        "500": {
            "description": "?????????????????????",
        }
    }
}

user_search = {
    "definitions": user_list,
    "responses": {
        "200": {
            "description": "???????????????????????????",
            "schema": {
                "$ref": "#/definitions/UserList"
            },
        },
        "500": {
            "description": "???????????????????????????",
        }
    }
}


user_get = {
    "definitions": user_model,
    "responses": {
        "200": {
            "description": "?????????????????????",
            "schema": {
                "$ref": "#/definitions/User"
            },
        },
        "500": {
            "description": "?????????????????????",
        }
    }
}

record_search = {
    "parameters": [
        {"name": "user_id", "in": "Path", "type": "string", "required": "true"},
    ],
    "definitions": record_list,
    "responses": {
        "200": {
            "description": "??????????????????????????????",
            "schema": {
                "$ref": "#/definitions/RecordList"
            },
        },
        "500": {
            "description": "??????????????????????????????",
        }
    }
}

record_count = {
    "parameters": [
        {"name": "user_id", "in": "Path", "type": "string", "required": "true"},
    ],
    "definitions": {
        "count": {
            "type": "number"
        }
    },
    "responses": {
        "200": {
            "description": "?????????????????????????????????",
            "schema": {
                "id": "count",
                "type": "number"
            },
        },
        "500": {
            "description": "?????????????????????????????????",
        }
    }
}

target_get = {
    "parameters": [
        {"name": "user_id", "in": "Path", "type": "string", "required": "true"},
    ],
    "definitions": target_model,
    "responses": {
        "200": {
            "description": "???????????????????????????",
            "schema": {
                "$ref": "#/definitions/Target"
            },
        },
        "500": {
            "description": "???????????????????????????",
        }
    }
}

log_search = {
    "parameters": [
        {"name": "user_id", "in": "Query", "type": "string"},
        {"name": "start", "in": "Query", "type": "string"},
        {"name": "end", "in": "Query", "type": "string"},
    ],
    "definitions": logrecord_model,
    "responses": {
        "200": {
            "description": "??????Log??????",
            "schema": {
                "$ref": "#/definitions/LogRecord"
            },
        },
        "500": {
            "description": "??????Log??????",
        }
    }
}