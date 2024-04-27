# 写开头的文档，表示这是一个叫做lonear的生物，因为只有他一个，所以叫lonear
'''
lonear是一个生物
'''


class lonear():
    def __init__(self):
        self.name = 'lonear'
        self.character = {}
        self.age = 0
        self.__self_known__()

    def __name__(self):
        return self.name

    def __self_known__(self):
        self.character['name'] = self.__name__()
    
    def get_name(self):
        return self.character['name']


def main():
    Lonear = lonear()

    while True:
        # 询问lonear的名字
        # input fron line
        query = input('你好: ')
        if query == 'What is your name?':
            print(Lonear.__name__())
            break

if __name__ == '__main__':
    main()
