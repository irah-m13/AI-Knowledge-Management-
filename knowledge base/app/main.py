from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.src.routers import answer_router, history_router
from app.utils.logging.logging import setup_logger
from app.src.routers.km_question_router import router as km_router

# Initialize the FastAPI app
app = FastAPI()

# Setup logger
setup_logger()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace with specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Include routers
app.include_router(answer_router.router, prefix="/answer")
app.include_router(history_router.router, prefix="/history")
app.include_router(km_router, prefix="/km")

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
