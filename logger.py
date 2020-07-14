
from datetime import datetime


def logger(parameter):

    def time(old_foo):

        date = datetime.utcnow()

        def new_foo(*args, **kwargs):

            result = old_foo(*args, **kwargs)

            with open(parameter, 'a', encoding='utf-8') as fo:

                fo.write(f'Вызвана функция "{old_foo.__name__}"\n'
                         f'Аргументы: "{args}", "{kwargs}"\n'
                         f'Старт программы: {date}\n'
                         f'Результат: {result}\n'
                         f'____________________________________\n')

                return result

        return new_foo

    return time
