from fastapi import FastAPI
from routers.async_converter import router as async_router
from routers.sync_converter import router as sync_router

app = FastAPI()

# Incluindo Rotas
app.include_router(router=async_router)
app.include_router(router=sync_router)


@app.get("/")
async def root():
    return "Olá mundo!"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
