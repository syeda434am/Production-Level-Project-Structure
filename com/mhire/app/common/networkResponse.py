import time

class NetworkResponse:

    def __init__(self, version=0.1):
        self.version = version

    def success_response(self, http_code, data, resource, start_time):
        return {
            "code": http_code,
            "message": "Success",
            "meta": {
                "result": round((time.time() - start_time) * 1000),  # Time in milliseconds
                "version": self.version,
                "resource": resource
            },
            "data": data
        }

    def error_response(self, http_code, error_code, error_message, resource, start_time):
        return {
            "code": http_code,
            "message": "Fail",
            "error": {
                "code": error_code,
                "message": error_message
            },
            "meta": {
                "result": round((time.time() - start_time) * 1000),  # Time in milliseconds
                "version": self.version,
                "resource": resource
            },
        }

class HTTPCode:
        SUCCESS = 200
        NOT_FOUND = 404
        UNPROCESSABLE_ENTITY = 422
        INTERNAL_SERVER_ERROR = 500
        SERVICE_UNAVAILABLE = 503

class Error:
        class NotFound:
            SOMETHING_NOT_FOUND = 40401

        class UnprocessableEntity:
            INVALID_FIELD_VALUE = 42202

        class InternalServerError:
            UNEXPECTED_ERROR = 50001

        class ServiceUnavailable:
             SERVER_OVERLOADED = 50301
            
class Message:
        class Success:
            SOMETHING_SUCCESS = "Something is successful."

        class NotFound:
            SOMETHING_NOT_FOUND = "Something not found in the given path."

        class UnprocessableEntity:
            INVALID_FIELD_VALUE = "Invalid value provided for the field."

        class InternalServerError:
            UNEXPECTED_ERROR = "An unexpected error occurred."

        class ServiceUnavailable:
             SERVER_OVERLOADED = "The server is currently overloaded. Please try again later."