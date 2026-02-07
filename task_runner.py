from functools import partial
from typing import Callable, List


class TaskRunnerQueue:
    def __init__(self, fun: List[Callable]):
        self.queue = list(fun)

    def run_queue_funs(self):
        idx = 1
        while self.queue:
            fun = self.queue.pop(0)
            print("-" * 50 + f"Task #{idx}" + "-" * 50)
            print(f"Function '{fun.func.__name__}' is starting... ")
            fun()
            print(f"Function '{fun.func.__name__}' is finished")
            print("-" * 50)
            idx += 1
        return True
    

def send_email(email):
    print(f"sending email to {email}.")

def welcom(name):
    print(f"Welcom {name}!")



quque = TaskRunnerQueue(fun=[partial(send_email, "mezo@gmail.com"), partial(welcom, "Just Mezo")])
quque.run_queue_funs()

