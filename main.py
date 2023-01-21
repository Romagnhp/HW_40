# модуль для реализации ORM
import sqlalchemy

# импорт файла с классом для создания полей БД
from models.User import MyColunms, ParentClass

# модуль для доступа к обьекту Session
from sqlalchemy.orm import Session

# подкл. модуля для отправи запроса на получения API с сайт https://swapi.dev/
import requests

# модуль для десириализации полученного запроса в формате json
import json

# подкл. регулярных выражений
import re 

def myFunc(urlPage):
    myRiquest = requests.get(r'https://swapi.dev/api/people/?page=' + urlPage)
    if myRiquest.status_code == 200:

        objFromString = json.loads(myRiquest.text) # преобразование полученого запроса в словарь

        resultKey = objFromString['results'] # словарь, обращение к значению по ключу, первая вложенность обьекта запроса

        with Session(myEngine) as db: # открытие сеcсии для сохранения значений в аблицу БД

            for j in range(len(resultKey)): # перебор списка, обращение по индексу, вторая вложенности обьекта запроса

                # создание обьетка класса MyColunms - строки таблици БД
                row_n = MyColunms(
                                    name = resultKey[j]['name'], # словарь, образение к значению по ключу, третья вложенность обьекта запроса     
                                    height = resultKey[j]['height'], 
                                    eye_color = resultKey[j]['eye_color'], 
                                    gender = resultKey[j]['gender']
                                )
                
                # добавление строки со значениями в таблицу БД
                db.add(row_n) 
                db.commit()

# создание БД
myEngine = sqlalchemy.create_engine('sqlite:///Star_Wars.db')
myConection = myEngine.connect()

# удаление полей БД
ParentClass.metadata.drop_all(myEngine)
# создание полей БД
ParentClass.metadata.create_all(myEngine)

for i in range(1, 10):
    myFunc(str(i))

with Session(myEngine) as db:

        # вывод персонажей у которых голубые глаза
        # select_Blue_Eyes = db.query(MyColunms).filter(MyColunms.eye_color == "blue")
        # for k in select_Blue_Eyes:
        #     print(k.id, k.name, f"(eye color) - {k.eye_color}") 

        # вывод трьох самых высоких 
        # select_Highest = db.query(MyColunms).order_by(MyColunms.height.desc()).limit(3)
        # for k in select_Highest:
        #     print(k.id ,k.name, k.height)

        # вывод всех людей (по свойству gender) у которых рост больше 170 см
        # select  = db.query(MyColunms).filter(MyColunms.height > 170).all()
        # for k in select:
        #     print(k.id, k.name, k.height)