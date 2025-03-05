from fastapi import FastAPI, Query

import data

app = FastAPI()


@app.get("/")
def index():
    return dict(msg="Hello World")


@app.get("/name/")
def get_name(   
    name: str = Query("Ви не ввели ім'я", description="Введіть своє ім'я"),
    age: int = Query(0, description="Введіть свій вік")
):
    return dict(    
        msg=f"Вітаю '{name}' в нашій інформаційній системі",
        age=age,
        age_type=f"{type(age)}"
        )


@app.get("/info/")
def info(   
    city: str = Query("Ви неввели місто", description="Введіть назву міста"),
    region: str = Query("Не ввели назву області", description="Введіть назву област")
):
    return dict(    
        msg=f"Вітаю ось ваше {city} а ось ваша область {region}"
    )

@app.get("/calculator/")
def calculator(extion: str=Query ( description="Виберіть операцію рlus або minus"), num_1: int = Query(description="Введіть перше число"), num_2: int=Query(description="Введіть друге число"), ):
    if extion == "plus":
        return {"extions": num_1 + num_2}
    elif extion == "minus":
        return {"extions": num_1 - num_2 }

    return dict(msg=f"Вітаю ось ваше число {extion}")


@app.get("/departures/")
def departures(departure: str = Query(None,description="Виберіть напрямок (ex: odesa)")):
    if departure:
        return dict(msg=data.departures.get(departure, "Такого напрямку немає"))
    
    return dict(msg=data.departures)


@app.get("/tours/")
def tours(tour_id: int = Query(None, description="Введіть індекс туру",  )):
    if tour_id:
        return dict(msg=data.tours.get(tour_id, "Такого туру немає"))
    
    return dict(msg=data.tours)

@app.get("/tour/")
def get_tour(tour_id: int = Query(description="Введіть індекс туру"), param: str = Query(None, description="Яка інформація вас цікавить")):
    if param:
        return dict(msg=data.tours.get(tour_id, {}) .get(param))
    
    return dict(msg=data.tours.get(tour_id))