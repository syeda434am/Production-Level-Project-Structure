import logging
import time

from fastapi import APIRouter, Request

from com.mhire.app.common.networkResponse import NetworkResponse, HTTPCode, Error, Message

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

router = APIRouter()
response = NetworkResponse()

@router.post("/endpoint_name")
def post_epname(http_request: Request):
    start_time = time.time()

    try:
        
        result = "Something"

        if result is "Something":
            return response.success_response(
                http_code=HTTPCode.SUCCESS,
                data={"message": Message.Success.SOMETHING_SUCCESS}, 
                resource=http_request.url.path, 
                start_time=start_time
            )
        else:
            return response.error_response(
                http_code=HTTPCode.NOT_FOUND,
                error_code=Error.NotFound.SOMETHING_NOT_FOUND, 
                error_message=Message.NotFound.SOMETHING_NOT_FOUND, 
                resource=http_request.url.path, 
                start_time=start_time
            )

    except Exception as e:
        return response.error_response(HTTPCode.INTERNAL_SERVER_ERROR, Error.InternalServerError.UNEXPECTED_ERROR, str(e), http_request.url.path, start_time)
