from src import API_KEY
from src.utils import func1, func2, func3, func4, func5
from src.json_class import Obj2, Obj3
from src.obj import Obj
from src.objs import Obj4, Obj5, Obj6
from dotenv import load_dotenv
import os
load_dotenv()

        
if __name__ == "__main__":
    HELLO = os.getenv("HELLO")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    print(HELLO)
    print(API_KEY, EMAIL, PASSWORD)
    a = func1(1, 2)
    b = func2(1, 2)
    c = func3(1, 2)
    d = func4(1, 2)
    e = func5(1, 2)
    obj2 = Obj2(1, 2)
    obj3 = Obj3(1, 2)
    obj4 = Obj4(1, 2)
    obj5 = Obj5(1, 2)
    print(a, b, c, d, e)
    print(obj2.method1("obj2", {"a": 1, "b": 2}))