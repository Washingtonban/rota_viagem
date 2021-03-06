from model.data_connect import DataConnect
from model.route_search import RouteSearch


class AppConsole:

    def __init__(self):
        self.introApp()

    def introApp(self):

        '''
        Function that starts the application and has the navigation menu
        :return:
        '''

        print('############################################################')
        print('#           ESCOLHA UMA OPÇÃO PARA CONTINUAR               #')
        print('############################################################')
        print()
        print('1 - Procurar vôos')
        print('2 - Cadastrar vôos')
        print('3 - Sair da aplicação')
        opcao = input('Digite sua opção: ')

        if opcao == '1':
            self.search_voo()
        elif opcao == '2':
            self.update_voo()
        elif opcao == '3':
            print('Obrigado por escolher nossa aplicação, volte sempre!')
        else:
            print('Valor digitado incorreto. Tente novamente!')
            self.introApp()


    def search_voo(self):

        '''
        function that executes the query at the base and prints the cheapest route on the console
        :return:
        '''

        print('############################################################')
        print('#             APLICATIVO DE ROTA DE VIAGEM                 #')
        print('############################################################')
        print()
        valor = input('Digite uma rota! Ex: GRU-CDG: ')

        if len(valor) == 7 and valor[3] == '-':
            origem = valor[:3]
            destino = valor[4:]

            origens, destinos = DataConnect().origens_destinos()

            if (origem.upper() in origens) and (destino.upper() in destinos):
                result = RouteSearch(origem=origem, destino=destino).route_search()
                prt = ''
                for item in result[1]:
                    if item == result[1][-1]:
                        prt += f' {item}'
                    prt += f' {item} -'

                print(f'{prt} > {result[0]}')
            elif (origem.upper() not in origens) or (destino.upper() not in destinos):
                print('Origem ou Destino não encontrados na base de dados!')
                print('Cadastre sua nova rota na opção 2 ou pesquise novamente na opção 1')
                AppConsole()

        else:
            print('Valor digitado errado, Tente novamente!')
            AppConsole()

    def update_voo(self):

        '''
        function that writes new routes to the database
        :return:
        '''

        print('############################################################')
        print('#              CADASTRO DE ROTA DE VIAGEM                  #')
        print('############################################################')
        print()
        new_route = input('Digite uma nova rota, ex: GRU-CFT-100: ')
        if new_route[3] == '-' and new_route[7] == '-' and len(new_route) >= 9 and len(new_route) <= 11:
            origem = new_route[:3]
            destino = new_route[4:7]
            custo = new_route[8:]
            line = [origem, destino, custo]
            model_update = DataConnect()
            data = './data/input-file.csv'
            model_update.updateCsv(data=data, line=line)
        else:
            print('Rota digitada de forma incorreta, tente novamente')
            AppConsole()


if __name__ == '__main__':
    AppConsole()