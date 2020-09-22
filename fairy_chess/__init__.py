__version__ = '0.1.0'

import time
import uuid
import traceback

from loguru import logger
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from fairy_chess.config import DESCRIPTION
from fairy_chess.exceptions import FairyChessException


logger.level("REQUEST RECEBIDA", no=38, color="<yellow>")
logger.level("REQUEST FINALIZADA", no=39, color="<yellow>")

app = FastAPI(
    title="Fairy Chess",
    description=DESCRIPTION,
    version=__version__,
    docs_url="/swagger",
    redoc_url="/docs"
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    id_ = uuid.uuid1()

    logger.log("REQUEST RECEBIDA", f"[{request.method}] ID: {id_} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path}")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.log("REQUEST FINALIZADA", f"[{request.method}] ID: {id_} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path} - TEMPO: {process_time}")
    response.headers["X-Process-Time"] = str(process_time)

    return response


@app.exception_handler(FairyChessException)
async def camara_exception_handler(request: Request, exception: FairyChessException):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "status": exception.status_code,
            "message": exception.message,
            "stacktrace": traceback.format_exc()
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exception: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "status": 422,
            "message": "Campo de requisição inválido",
            "stacktrace": traceback.format_exc()
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException):
    message = {401: "Não autorizado", 404: "Endereço não encontrado", 405: "Método não permitido"}
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "status": exception.status_code,
            "message": message[exception.status_code],
            "stacktrace": traceback.format_exc()
        }
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']
)
