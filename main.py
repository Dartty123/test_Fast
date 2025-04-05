from fastapi import FastAPI, Query



app = FastAPI()


@app.get("/")
def index():
    return dict(msg="Hello World")


@app.get("/calculator/")
def calculator(extion: str=Query ( description="Виберіть операцію + - / * "), num_1: int = Query(description="Введіть перше число"), num_2: int=Query(description="Введіть друге число"), ):
    if extion == "plus":
        return {"extions": num_1 + num_2}
    elif extion == "minus":
        return {"extions": num_1 - num_2 }
    elif extion == "/":
        return {"extions": num_1 / num_2}
    elif extion == "*":
        return {"extions": num_1 * num_2}

    return dict(msg=f"Вітаю ось ваше число {extion}")

