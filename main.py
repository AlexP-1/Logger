
import requests
import json
from logger import logger


URL = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&limit=1&search='


@logger('logs_2.0.txt')
def open_json():
    """
    Получаем список стран
    """
    with open('countries.json', 'r', encoding='utf-8') as fi:
        data = json.load(fi)
    country_list = []
    for country in data:
        country_list.append(country['name']['common'])
    return country_list


class WikiSearch:

    def __init__(self):
        self.session = requests.Session()
        self._index = 0
        self.country = [str(country) for country in open_json()]

    def __iter__(self):
        return self

    def __next__(self):
        """
        Перебираем страны в списке и подставляем каждую в get_url
        """
        if self._index < len(self.country):
            country_name = self.country[self._index]
            self._index += 1
            return self.get_url(country_name)
        else:
            raise StopIteration

    @logger('logs_2.0.txt')
    def get_url(self, country_name):
        result = self.session.get(f'{URL}{country_name}')
        return result.json()


if __name__ == '__main__':

    @logger('logs_2.0.txt')
    def get_file():
        country_url = []
        for url in WikiSearch():
            country_url.append(f'{url[0]}: {url[3]}')
        with open('countries_url.txt', 'w', encoding='utf-8') as fo:
            for pair in country_url:
                print('Writing . . .')
                fo.write(f'{str(pair)}\n')

    get_file()
