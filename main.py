from classes.Directory import Directory

contactList = []

print('Lista Telefonica')

while True:
    print('\nOpções:')
    print('1 • Novo | 2 • Lista Telefônica | 3 • Sair da Lista ')

    op = int(input('Escolha uma das opções: '))

    if op == 1:
        name = input('Nome: ')
        phone = int(input('Número: '))
        contactList.append(Directory.add_contact(name, phone))

    elif op == 2:
        Directory.get_all_contacts(contactList)

    elif op == 3:
        break

    else:
        print('Opção inválida!')



print('FIM')