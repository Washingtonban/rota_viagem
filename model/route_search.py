
from model.data_connect import DataConnect


class RouteSearch:

    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino
        self.dados = [f for f in DataConnect().readCsv('./data/input-file.csv')]
        self.routes = []
        self.temp = []
        self.index = -1
        self.min_value = 0.0
        self.min_index = -1
        self.sum_temp = 0.0

    def route_search(self) -> tuple:
        '''
        method that finds the cheapest route among all possibilities
        :return: tuple with cheapest route and price
        '''

        origin_start = [x for x in self.dados if x[0] == self.origem]

        for route in origin_start:
            if route[1] == self.destino:
                self.index += 1
                if (self.min_value == 0.0 or float(route[2]) < self.min_value):
                    self.min_value = float(route[2])
                    self.min_index = self.index
                    self.routes.append(route)

            else:
                self.sum_temp += float(route[2])
                self.temp.extend(route)
                self.till_search(route[1])

        prices_routes = self.dict_with_routes()
        better_price = min(prices_routes)
        route_better_price = prices_routes[better_price]

        return better_price, route_better_price

    def till_search(self, leave_at):

        other = [y for y in self.dados if y[0] == leave_at]

        for ot in other:
            ori = ot[0]
            des = ot[1]

            for d in self.dados:
                if d[0] == ori and d[1] == des:
                    self.sum_temp = self.sum_temp + float(d[2])
                    self.temp.extend(d)
                    if d[1] == self.destino:
                        self.index_min_value()
                        self.routes.append(self.temp)
                        self.temp = []
                        break
                    else:
                        self.till_search(d[1])

    def index_min_value(self):
        self.index = self.index + 1

        if (self.min_value == 0.0 or self.sum_temp < self.min_value):

            self.min_value = self.sum_temp
            self.sum_temp = 0.0
            self.min_index = self.index


    def set_result(self, route) -> tuple:
        '''
        method receives a list representing a route and transforms and returns a tuple with a list, origin and
        destination, and the price
        :param route: list with [origin, destiny, price]
        :return: tuple ([origin, destiny], price)
        '''
        cheaper_route = route
        origins = cheaper_route[0::3]
        destin = cheaper_route[1::3]
        amount = cheaper_route[2::3]
        origins.append(destin[-1])

        total_amount = 0
        for price in amount:
            total_amount += int(price)

        return origins, total_amount

    def dict_with_routes(self) -> dict:
        '''
        method that organizes routes in dictionaries, key = price and value = list with origin,
        destination and all scales
        :return: dict
        '''
        all_routes = {}
        for route in self.routes:
            list_route, total_amount = self.set_result(route)
            all_routes[total_amount] = list_route

        return all_routes
