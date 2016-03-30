import random


def _get_name():
    num = random.randint(2, 3)
    name = ''.join([chr(random.randint(0x4E00, 0x8377)) for i in range(num)])
    if num == 2:
        return name[0] + ' ' + name[1]
    return name


def _get_id():
    return ''.join(random.sample('0123456789', 6))


def _get_sco():
    return '%.1f' % (random.randint(10, 100))


def _get_sex():
    return ['男', '女'][random.randint(0, 1)]


def init_write_file(filename, num=50, flag=False):
    result = []
    for i in range(num):
        if flag:
            tmp = ','.join([_get_id(), _get_name(), _get_sex(), _get_sco(), _get_sco(), _get_sco(), '0.0', '0.0'])
        else:
            tmp = ','.join([_get_id(), _get_name(), _get_sex(), _get_sco(), _get_sco(), _get_sco()])
        result.append(tmp)
    with open(filename, 'w+') as f:
        f.write('\n'.join(result))


def print_menu():
    print('*************************************************************************************************')
    print('\t\t1.创建文件 \t\t\t\t 2.显示记录 \t\t\t\t 3.编辑记录')
    print('\t\t4.增加记录 \t\t\t\t 5.删除记录 \t\t\t\t 6.查询记录')
    print('\t\t7.排序记录 \t\t\t\t 8.统计记录 \t\t\t\t 0.退出')
    print('*************************************************************************************************')


def plot(name, xdata, ydata):
    """
    Simple demo of a horizontal bar chart.
    """
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,6))
    import matplotlib.pyplot as plt
    y_pos = range(1, 11)
    plt.barh(y_pos, xdata, align='center', alpha=0.9)
    plt.yticks(y_pos, ydata)
    plt.xlabel('人数')
    plt.title(name)
    plt.show()
