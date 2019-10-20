import person

def menu():
    while True:
        print('MENU')
        choice = int(input(('''
        1- cadastrar
        2- listar
        3- sair
        ''')))
        if choice == 1:
            name = str(input('digite o nome: ')).strip()
            while True:
                try:
                    age = int(input('digite a idade: '))
                except Exception:
                    print('valor irregular, digite novamente!')
                else:
                    break
            person.add_person(name, age)
            print('cadastro realizado!')
        elif choice == 2:
            person.read_list()
            print('listagem realizada!')
        else:
            print('logout realizado!')
            break