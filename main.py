from fastapi import FastAPI
from routes.insights import router as insights_router

app = FastAPI(title="LinkedIn Insights API")

# Include routers
app.include_router(insights_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)