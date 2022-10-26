class RespectTheEmpire(type):
    def __init__(cls, name, bases, attrs):
        treason = "Vader_is_dump"
        for key, value in attrs.items():
            if callable(value) and treason in key:
                raise Exception("I find your lack of faith disturbing")
        super().__init__(name, bases, attrs)

class Rebellion(metaclass=RespectTheEmpire):
    def we_know_Vader_is_dump():
        print('AAAAA')