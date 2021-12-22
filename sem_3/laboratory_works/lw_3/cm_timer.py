import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.current_time = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('time:', time.time() - self.current_time)


@contextmanager
def cm_timer_2():
    current_time = time.time()
    yield time.time() - current_time
    print('time:', time.time() - current_time)


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1.3)

    with cm_timer_2():
        time.sleep(1.3)
