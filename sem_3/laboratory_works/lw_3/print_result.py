def print_result(func_to_decorate):

    def decorated_func():
        print(func_to_decorate.__name__)
        func_product = func_to_decorate()

        if type(func_product) == list:
            for item in func_product:
                print(item)
        elif type(func_product) == dict:
            for key in func_product.keys():
                print('{} = {}'.format(key, func_product[key]))
        else:
            print(func_product)

    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
