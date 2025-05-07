from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from src.routes import dev_router, router

app = FastAPI(title="GAP Python AI Workshop")

# Add the CORSMiddleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows specific origins
    allow_credentials=True,  # Allows cookies or other credentials
    allow_methods=["*"],  # Allows all methods: GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers
)


app.include_router(router)
app.include_router(dev_router)


if __name__ == "__main__":
    run(app, port=8000)
