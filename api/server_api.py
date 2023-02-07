from typing import Union

from fastapi import FastAPI


def envfile(link):
    with open("../actions/.env", "w+", encoding="utf-8") as file:
        file.write("EPITECK-LOGIN="+link)
    return True

app = FastAPI()

@app.get("/login/")
async def login(link: str):
    status = envfile(link)
    if status:
        return {"message": "Link saved"}
    else:
        return {"message": "Error"}
 