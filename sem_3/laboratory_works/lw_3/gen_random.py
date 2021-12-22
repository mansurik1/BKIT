import random


def gen_random(num_count, begin, end):
    random.seed(version=2)
    for i in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    random_gen = gen_random(5, 1, 3)
    for item in random_gen:
        print(item, end=' ')
