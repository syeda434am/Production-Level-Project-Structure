import logging
import time
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Header, Request, Body
from pydantic import BaseModel

from com.mhire.app.database.embedding.embedding_crud import CRUD
from com.mhire.app.common.networkResponse import NetworkResponse, HTTPCode, Error, Message


router = APIRouter()
response = NetworkResponse()

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Define a Pydantic model for the expected request body
class RetrieveRequest(BaseModel):
    search_text: str
    search_fields: List[str]  # List of fields to search on
    
class DeleteRequest(BaseModel):
    connection_name: Optional[str] = 'defaultConnection'
    field_name: Optional[str] = 'id'  # Make field_name optional with a default of 'id'
    field_value: str
    

@router.delete("/embedding")
def delete_embedding(request: DeleteRequest, http_request: Request):
    start_time = time.time()

    try:
        # Initialize the CRUD object using the header values
        crud = CRUD(

            connection_name=request.connection_name
        )
        
        result = crud.delete()
        

        if result is True:  # Check if deletion was successful
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
    

@router.post("/embedding")
async def insert_embedding():
    pass

@router.get("/embedding")
async def retrieve_embedding():
    pass

@router.put("/embedding")
async def update_embedding():
    pass