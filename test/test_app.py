from src.app import USERS
from src.app import (
    make_response,
    make_error_message,
    select_user_by_id,
    get_response_validation,
    get_user_by_id,
    build_response,
)

import pytest


def test_make_response():
    data_mock = dict(test="test")
    code_mock = 999
    result = make_response(data_mock, code_mock)

    assert isinstance(result, tuple)
    assert result[0].get("result", None) == data_mock
    assert result[0].get("status_code", None) == code_mock


def test_make_error_message():
    message_mock = "test"
    result = make_error_message(message_mock)

    assert isinstance(result, dict)
    assert result.get("error") == message_mock


def test_select_user_by_id_in_bounds():
    id_mock = 1
    result = select_user_by_id(id_mock)

    assert isinstance(result, dict)
    assert result in USERS


def test_select_user_by_id_out_bounds():
    id_mock = 9999
    with pytest.raises(IndexError):
        select_user_by_id(id_mock)


def identity(x: any) -> any:
    return x


def test_build_response():
    fct_mock = identity
    arg_mock = "test"
    code_mock = 999
    result = build_response(fct_mock, arg_mock, code_mock)

    assert isinstance(result, tuple)
    assert code_mock in result
    assert len(result) == 2


def test_get_response_validation_validated():
    id_mock = 1
    result = get_response_validation(id_mock)

    assert isinstance(result, tuple)
    assert 200 in result
    assert len(result) == 2


def test_get_response_validation_invalid():
    id_mock = 999
    result = get_response_validation(id_mock)

    assert isinstance(result, tuple)
    assert 404 in result
    assert len(result) == 2


def test_get_user_by_id_valid():
    id_mock = 1
    result = get_user_by_id(id_mock)
    result_data = result[0].get("result", None)
    result_code = result[0].get("status_code", None)

    assert isinstance(result, tuple)
    assert result_data == USERS[id_mock - 1]
    assert result_code == 200


def test_get_user_by_id_not_found():
    id_mock = 999
    result = get_user_by_id(id_mock)
    result_data = result[0].get("result", None)
    result_code = result[0].get("status_code", None)

    assert isinstance(result, tuple)
    assert result_data.get("error", None)
    assert result_code == 404
