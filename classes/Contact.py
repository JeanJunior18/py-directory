class Contact():

    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return self.__name

    def __str__(self):
        return '-------------\n\nNome: {} \nNúmero: {} \n'.format(self.__name, self.__phone)
