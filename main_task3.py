import types
from functools import wraps
import datetime


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        with open("main_task3.log", "a+") as file:
            file.write("---------------------------------------------------------------------------------------------" + "\n")
            file.write(f"Дата и время вызова функции: {start}" + "\n")
            file.write(f"Имя функции {old_function} и вызываемые аргументы {args} и {kwargs}" + "\n")
            file.write(f"Возвращаемое значение {result}" + "\n")
            file.write("\n\n\n")
        file.close()

        return result
    return new_function


@logger
def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item



def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()