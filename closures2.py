from typing import Generic, TypeVar

#HOLA --> holaholaholaholahola

#Funcion envolvente
def make_repeater_of(n):
    #Nested funcion
    def repeater(string):
        #Si no es str envia la excepcion
        assert type(string) == str, 'Solo puedes repetir cadenas'
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))


if __name__ == '__main__':
    run()