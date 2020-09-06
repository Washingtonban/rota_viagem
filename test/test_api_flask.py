import sys
sys.path.insert(1, '/home/washington/Documents/Desafios/bexs')
from model.route_search import *


class TestDataConnect:
    def test_read_csv(self):
        csv_file = './data/input-file.csv'
        first_line_csv = ['GRU', 'BRC', '10']

        data_connect = DataConnect()
        data = data_connect.readCsv(csv_file)
        assert data[0] == first_line_csv

    def test_update_csv(self):
        csv_file = './data/input-file.csv'
        update_line_csv = ['MAO', 'FTY', '100']

        data_connect = DataConnect()
        data_connect.updateCsv(csv_file, update_line_csv)
        data = data_connect.readCsv(csv_file)

        assert data[-1] == update_line_csv

    def test_update_repeted_origen_destiny(self):
        csv_file = './data/input-file.csv'
        update_line_csv = ['MAO', 'FTY', '100']

        data_connect = DataConnect()
        msg = data_connect.updateCsv(csv_file, update_line_csv)

        assert 'This route has already been registered' in msg

    def test_line_validator_exist(self):
        csv_file = './data/input-file.csv'
        line_validated = ['MAO', 'FTY', '100']

        data_connect = DataConnect()
        bool_return = data_connect.lineValidator(csv_file, line_validated)

        assert bool_return is True

    def test_line_validator_not_exist(self):
        csv_file = './data/input-file.csv'
        line_validated = ['CAS', 'GFD', '10']

        data_connect = DataConnect()
        bool_return = data_connect.lineValidator(csv_file, line_validated)

        assert bool_return is False

    def test_origen_destiny_exist(self):
        origen = ['GRU', 'BRC', 'GRU', 'GRU', 'GRU', 'ORL', 'SCL', 'MAO', 'MAO']
        destiny = ['BRC', 'SCL', 'CDG', 'SCL', 'ORL', 'CDG', 'ORL', 'REC', 'FTY']

        data_connect = DataConnect()
        ori, des = data_connect.origens_destinos()

        assert ori == origen and des == destiny

class TestRouteSearch:
    def test_route_many_options(self):
        origin = 'GRU'
        destiny = 'CDG'

        route_search = RouteSearch(origin, destiny)
        tuple_result = route_search.route_search()

        amount = 40
        route = ['GRU', 'BRC', 'SCL', 'ORL', 'CDG']

        assert tuple_result[0] == amount and tuple_result[1] == route

    def test_route_one_option(self):
        origin = 'GRU'
        destiny = 'BRC'

        route_search = RouteSearch(origin, destiny)
        tuple_result = route_search.route_search()

        amount = 10
        route = ['GRU', 'BRC']

        assert tuple_result[0] == amount and tuple_result[1] == route
