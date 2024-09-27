from flask import Flask


response = tuple[dict, int]
app = Flask(__name__)
USERS = [
    {"name": "User 1", "age": "30"},
    {"name": "User 2", "age": "23"},
    {"name": "User 3", "age": "54"},
]


def make_response(data: dict, code: int) -> response:
    return {"result": data, "status_code": code}, code


def make_error_message(message: str) -> dict:
    return {"error": message}


def select_user_by_id(id: int) -> dict:
    return USERS[id - 1]


def validate_id(id: int) -> bool:
    return isinstance(id, int) and (id > 0) and (id <= len(USERS))


def build_response(fct: callable, arg: any, code: int) -> response:
    return make_response(fct(arg), code)


def get_response_validation(id: int) -> response:
    if validate_id(id):
        fct = select_user_by_id
        arg = id
        code = 200
    else:
        fct = make_error_message
        arg = f"id {id} is invalid"
        code = 404
    return build_response(fct, arg, code)


def get_user_by_id(id: int) -> response:
    try:
        return get_response_validation(id)
    except Exception:
        return build_response(make_error_message, "unknown error", 500)


@app.route("/user/<int:id>")
def route_get_user_by_id(id: int) -> response:
    return get_user_by_id(id)
