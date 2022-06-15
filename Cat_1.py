from Cat import Animal

cats = [
    {
        "name": "Барон",
        "age": "2",
        "gender":"Мальчик"


    },
    {
        "name": "Сэм",
        "age": "2",
        "gender":"Мальчик"
    }
]
for item in cats:
    cat_item = Animal(name=item.get("name"),
                      age=item.get("age"),
                      gender=item.get("gender"))
    print(f"{cat_item.get_age()} года,{cat_item.get_name()},{cat_item.get_gender()}")