from datetime import datetime

#How much time a func run

def execution_time(func):
    #No matter how many arguments it gonna works, without it, will be necessary explicit arguments
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper

#How many seconds a for takes to do 10m cycles
@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


random_func()