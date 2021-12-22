def field(items, *args):
    assert len(args) > 0

    if len(args) > 1:
        for item in items:
            current_dict = dict()
            for arg in args:
                if item.get(arg, None):
                    current_dict[arg] = item[arg]
            if len(current_dict) > 0:
                yield current_dict
    else:
        for item in items:
            if item.get(args[0], None):
                yield item[args[0]]


def print_generator_output(lst):
    size = len(lst)
    for counter in range(size):
        if counter < size - 1:
            print(lst[counter], end=', ')
        else:
            print(lst[counter])


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    field_gen = field(goods, 'title')
    print_generator_output([item for item in field_gen])

    field_gen = field(goods, 'title', 'price')
    print_generator_output([item for item in field_gen])
