from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from com.mhire.app.services.feature1 import router as feature1_router
from com.mhire.app.services.feature2 import router as feature2_router
from com.mhire.app.common.networkResponse import NetworkResponse, HTTPCode

app = FastAPI(
    title="My API",
    description="My API description",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(feature1_router)
app.include_router(feature2_router)

response = NetworkResponse()

@app.get("/")
async def health_check():
    """
    Health check endpoint to verify API is running
    """
    return response.success_response(
                http_code=HTTPCode.SUCCESS,
                message="Server is healthy",
                data={"status": "running"}
                ) 