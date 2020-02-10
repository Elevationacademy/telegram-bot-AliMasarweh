from collections import Counter
import json


class DataBase:
    @classmethod
    def read_data(cls):
        with open('db.json') as json_file:
            cls.data = Counter(json.load(json_file))

        return cls.data

    @classmethod
    def write_data(cls):
        with open('db.json', 'w') as outfile:
            json.dump(cls.data, outfile)

        return 'successful'
