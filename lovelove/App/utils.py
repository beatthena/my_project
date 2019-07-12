#工具类
import random

#颜色函数
def get_color():
    return random.randrange(256)


def generate_code():
    source = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm'
    code = ''

    for i in range(4):
        code += random.choice(source)

    return code