from fastapi import APIRouter, FastAPI

router = APIRouter()


@router.get("/")
@router.get("/ping")
def ping():
    return {"message": "pong"}


def create_app() -> FastAPI:
    app = FastAPI(title="PingPong")
    app.include_router(router)

    return app
