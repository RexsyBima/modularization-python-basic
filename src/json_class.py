import json 
class Obj2:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        
    def method1(self, filename : str, data : dict):
        with open(f"{filename}.json", "w") as f:
            json.dump(data, f) 
class Obj3:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        
    def method1(self, filename : str, data : dict):
        with open(f"{filename}.json", "w") as f:
            json.dump(data, f)