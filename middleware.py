import time

from fastapi import FastAPI, Request

from logger import logger

# add middleware 1st method
# @app.middleware("http")

async def ecommerce_middleware(request: Request, call_next):
    logger.info("Starting ..................")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info("ended............")
    return response