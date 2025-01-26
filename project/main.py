from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Main dashboard website:
@app.get("/")
async def read_root():
    return FileResponse("static/index.html")


# API Routes:
@app.get("/api/v1/refresh_stats")
async def refresh_stats():
    return {"message": "Stats refreshed!"}


# Driver Code
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)