a = 100
# 建议
g_a = 100


def test():
    a = 200  # 在函数中 如果对一个和全局变量名相同的变量进行=value的时候,默认是定义一个变量
    # 只不过这个变量的名字和全局变量的名字相同罢了
    #
    # 如果想在执行a=value时,不是定义局部变量,而是对全局变量修改,那么可以添加global进行声明
    print("a=%d" % a)


def test2():
    print("a=%d" % a)  # 如果这里打印了100就声明了test函数没有对全局变量修改,而是定义了一个局部变量


test()
test2()
