from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
from .utils import verify_api_key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def api_key_middleware(request, call_next):
    api_key = request.headers.get("api-key")
    # print(f'API Key Middleware: {api_key}')
    if not verify_api_key(api_key):
        raise HTTPException(status_code=403, detail="Invalid API Key")
    response = await call_next(request)
    return response

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)