class RouteSearch:
    def __init__(self):

        with open('input-file.csv', 'r') as file:
            self.dados = [f.rstrip().split(',') for f in file]

        self.origem = "GRU"
        self.destino = "CDG"

        self.routes = []
        self.temp = []
        self.index = -1
        self.min_value = 0.0
        self.min_index = -1
        self.sum_temp = 0.0

        origin_start = [x for x in self.dados if x[0] == self.origem]

        for route in origin_start:
            if route[1] == self.destino:
                self.index = self.index + 1
                if(self.min_value == 0.0 or float(route[2]) < self.min_value):
                    self.min_value = float(route[2])
                    self.min_index = self.index
                self.routes.append(route)
            else:
                self.sum_temp = self.sum_temp + float(route[2])
                self.temp.append(route)
                self.till_search(route[1])

        print(self.routes)
        print(self.routes[self.min_index])

    def till_search(self, leave_at):

        other = [y for y in self.dados if y[0] == leave_at]

        for ot in other:
            ori = ot[0]
            des = ot[1]

            for d in self.dados:
                if d[0] == ori and d[1] == des:
                    self.sum_temp = self.sum_temp + float(d[2])
                    self.temp.append(d)
                    if d[1] == self.destino:
                        self.index_min_value()
                        self.routes.append(self.temp)
                        self.temp = []
                        break
                    else:
                        self.till_search(d[1])

    def index_min_value(self):
        self.index = self.index + 1
        if(self.min_value == 0.0 or self.sum_temp < self.min_value):
            self.min_value = self.sum_temp
            self.sum_temp = 0.0
            self.min_index = self.index
