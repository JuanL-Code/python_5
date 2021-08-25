#Run fibonacci with generators but with a max number to get

from time import sleep

def fibonacci_gen(max_counter:int):
    a, b = 0, 1
    while a <= max_counter:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    #until 89
    for element in fibonacci_gen(89):
        print(element)
        sleep(0.3)