from fastapi import APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(file : UploadFile):
    
    is_valid = DataController().validate_upload_file(file=file)
    
    return is_valid
        