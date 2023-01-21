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

def myFunc(urlPage):
    myRiquest = requests.get(r'https://swapi.dev/api/people/?page=' + urlPage)
    if myRiquest.status_code == 200:
        objFromString = json.loads(myRiquest.text) # преобразование в словарь
        resultKey = objFromString['results']

        with Session(myEngine) as db:

            for j in range(len(resultKey)):

                row_n = MyColunms(
                                    name = resultKey[j]['name'], 
                                    height = resultKey[j]['height'], 
                                    eye_color = resultKey[j]['eye_color'], 
                                    gender = resultKey[j]['gender']
                                )

                db.add(row_n)

                db.commit()


# создание БД
myEngine = sqlalchemy.create_engine('sqlite:///Star_Wars.db')
myConection = myEngine.connect()

# создание полей БД
ParentClass.metadata.drop_all(myEngine)
ParentClass.metadata.create_all(myEngine)

for i in range(1, 10):
    myFunc(str(i))
