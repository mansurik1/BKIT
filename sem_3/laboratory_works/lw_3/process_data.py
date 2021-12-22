import json
from cm_timer import cm_timer_1
from unique import Unique
from gen_random import gen_random

path = 'data_light.json'
with open(path) as f:
    data = json.load(f)


def print_result(func_to_decorate):

    def decorated_func(arg):
        print(func_to_decorate(arg))
        return func_to_decorate(arg)

    return decorated_func


@print_result
def f1(arg):
    return sorted([unique for unique in Unique([job["job-name"] for job in arg], ignore_case=True)])


@print_result
def f2(arg):
    return list(filter(lambda x: x.split()[0] == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda x: "{} c опытом Python".format(x), arg))


@print_result
def f4(arg):
    return list(map(lambda x: "{}, зарплата {} руб.".format(x[0], x[1]), list(zip(arg, gen_random(len(arg), 100000, 200000)))))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
