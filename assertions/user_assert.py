from assertions.expect import expect
from models.user_response import UserResponse


def assert_user_response(
        expected_code: int,
        expected_type: str,
        expected_message: str,
        actual_user_response: UserResponse):
    expect(expected_code)\
    .set_description("code")\
    .to_be_equal(actual_user_response["code"])

    expect(expected_type)\
    .set_description("type")\
    .to_be_equal(actual_user_response["type"])

    expect(expected_message)\
    .set_description("message")\
    .not_to_be_equal(actual_user_response["message"])
