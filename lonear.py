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

    # 排泄函数，生成一个排泄物文件，文件名为随机的Base64编码
    def excrete(self):
        import base64
        import random
        import string
        import os

        # 生成随机文件名
        def random_filename():
            return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # 生成随机文件名
        filename = random_filename()
        with open(filename, 'w') as f:
            f.write(base64.b64encode(os.urandom(1024)).decode('utf-8'))
        return filename


def main():
    Lonear = lonear()

    while True:
        # 询问lonear的名字
        # input fron line
        query = input('你好: ')
        if query == 'What is your name?':
            print(Lonear.__name__())
            Lonear.excrete()
            break

if __name__ == '__main__':
    main()
