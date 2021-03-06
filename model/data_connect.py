import csv

class DataConnect:

    def readCsv(self, data:str) -> list:

        '''
        This method read csv file and return list of lists
        :param data: String
        :return: List
        '''

        with open(data) as csv_file:
            route_list = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                route_list.append(row)
        return route_list

    def updateCsv(self, data:str, line:list):

        '''
        This method write new line on input-file.csv
        :param data: String
        :param line: List
        :return:
        '''

        with open(rf'{data}', 'a') as file:
            writer = csv.writer(file)
            if not self.lineValidator(data, line):
                msg = 'route successfully registered'
                writer.writerow(line)
                print(msg)
                return msg
            else:
                msg = 'This route has already been registered'
                print(msg)
                return msg


    def lineValidator(self, data:str, line:list) -> bool:

        '''
        This method validates if an equal line already exists
        :param data: String
        :param line: List
        :return: Bool
        '''

        db = self.readCsv(data)
        line_validator = line[:2]

        for row in db:
            if row[:2] == line_validator:
                return True

        return False

    def origens_destinos(self):
        origens = []
        destinos = []

        list = self.readCsv('./data/input-file.csv')

        for item in list:
            origens.append(item[0])
            destinos.append(item[1])

        return origens, destinos
