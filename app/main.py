from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def xui():
    return 0
@app.get("/2")
async def xui2():
    return 1