class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def user_info(self):
        print(f'id= {self.__id},Имя = {self.__name},Уровень доступа = {self.__access_level}')


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._User__access_level = 'admin'
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен!")

    def remove_user(self, user_id):
        for i, user in enumerate(self.__user_list):
            if user.get_id() == user_id:
                removed_user = self.__user_list.pop(i)
                print(f"Пользователь {removed_user.get_name()} удален!")
                return
        print("Пользователь не найден.")

    def list_of_users(self):
        print("Список пользователей:")
        for user in self.__user_list:
            print(f'id= {user.get_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()} \n')


user1 = User(1, 'John')
user2 = User(2, 'Ann')
user3 = User(3, 'David')
user4 = User(4, 'Ivan')

user1.user_info()
user2.user_info()
user3.user_info()
user4.user_info()

admin = Admin(1, 'Kate')
admin.user_info()
admin.list_of_users()

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)
admin.list_of_users()

admin.remove_user(1)
admin.remove_user(3)
admin.list_of_users()
