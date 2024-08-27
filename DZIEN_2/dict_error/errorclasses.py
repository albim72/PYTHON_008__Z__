class IntFloatValueError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"wartosc {self.value} jest niewłaściwa! Akceptowalne są tylko wartości w typie: int, float!"

class KeyValueConstructorError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return (f"""
                klucze i wartości winny byc przekazane w listach lub krotkach...
                klucz: {self.key} jest w typie {type(self.key)},
                wartośc: {self.value} jest w typie {type(self.value)}.
                """)
