from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(file : UploadFile):
    
    is_valid, result_signal = DataController().validate_upload_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
        