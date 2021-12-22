# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.items_len = len(items)
        self.current_element = 0

        if len(kwargs) == 0:
            self.flag = False
        else:
            self.flag = kwargs['ignore_case']

        self.no_duplicates = list()

    def __next__(self):
        for i in range(self.current_element, self.items_len):
            if not(self.items[i] in self.no_duplicates or str(self.items[i]).lower() in self.no_duplicates and self.flag):
                self.no_duplicates.append(self.items[i])
                return self.no_duplicates[-1]
            self.current_element = i + 1

        if self.current_element == self.items_len:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    data_1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data_2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    for unique in Unique(data_1):
        print(unique, end=' ')
    print()

    for unique in Unique(data_2, ignore_case=False):
        print(unique, end=' ')
    print()

    for unique in Unique(data_2, ignore_case=True):
        print(unique, end=' ')
    print()
