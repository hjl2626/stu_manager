import sys

from stu_manager.student import Student
from stu_manager.utiy import init_write_file, print_menu, plot

FILENAME = 'student.txt'
title = ('学\t号', '姓\t名', '性别', '微积分', '英语', '\t数据结构', '总成绩', '平均分')
title_show = ('序号', '学\t号', '姓\t名', '性别', '微积分', '英语', '\t数据结构', '总成绩', '平均分')
title_dict = {'1': '学\t号', '2': '姓\t名', '3': '性别', '4': '微积分', '5': '英语', '6': '\t数据结构', '7': '总成绩', '8': '平均分'}
stu_list = []
stu_data = []


def _init(filename=FILENAME, num=1000, flag=False):
    init_write_file(filename, num, flag)
    stu_list.clear()


def _strip(s):
    return s.strip()


def _read_data(filename=FILENAME):
    def decorator(func):
        def wrapper(*args, **kw):
            if len(stu_list) == 0:
                print('read data')
                with open(filename, 'r+') as f:
                    global stu_data
                    stu_data = map(_strip, f.readlines())
                for stu in stu_data:
                    stu_list.append(Student(title, stu.split(',')))
            return func(*args, **kw)

        return wrapper

    return decorator


def _write_file(stus=stu_list, flag=False, filename=FILENAME):
    print('write')
    with open(filename, 'w+') as f:
        f.write('\n'.join([s.to_write_str(flag) for s in stus]))


def print_title(flag=False):
    if flag:
        print('\t\t\t'.join(title_show))
    else:
        print('\t\t\t'.join(title_show[:-2]))


def _exit():
    sys.exit(0)


def _to_3(s):
    if len(s) == 2:
        return s[0] + ' ' + s[1]
    return s


def _to_float(s):
    return '%.1f' % float(s)


@_read_data()
def _show(stus=stu_list, flag=False):
    print_title(flag)
    for k, v in enumerate(stus):
        print('%s\t\t\t%s' % (k + 1, v.to_show_str(flag)))


@_read_data()
def _add():
    pos = input('请输入插入位置,默认最后\n')
    if pos == '':
        tmp_list = []
        stu = Student(names=title, values=(input('请输入学号：\n'), _to_3(input('请输入姓名：\n')),
                                           input('请输入性别：\n'), _to_float(input('请输入sco_1：\n')),
                                           _to_float(input('请输入sco_2：\n')), _to_float(input('请输入sco_3：\n'))))
        tmp_list.append(stu)
        while True:
            if input('是否继续？（y/n)\n').lower() == 'y':
                stu = Student(names=title, values=(input('请输入学号：\n'), _to_3(input('请输入姓名：\n')),
                                                   input('请输入性别：\n'), _to_float(input('请输入sco_1：\n')),
                                                   _to_float(input('请输入sco_2：\n')), _to_float(input('请输入sco_3：\n'))))
                tmp_list.append(stu)
            elif input('是否写入（y/n)\n').lower() == 'y':
                stu_list.extend(tmp_list)
                _write_file(stu_list)
                break
            else:
                break
    else:
        stu = Student(names=title, values=(input('请输入学号：\n'), _to_3(input('请输入姓名：\n')),
                                           input('请输入性别：\n'), _to_float(input('请输入sco_1：\n')),
                                           _to_float(input('请输入sco_2：\n')), _to_float(input('请输入sco_3：\n'))))
        try:
            tmp_list = stu_list[:]
            tmp_list.insert(int(pos), stu)
            print('插入成功')
            if input('是否写入（y/n)\n').lower() == 'y':
                stu_list.clear()
                stu_list.extend(tmp_list)
                _write_file(stu_list)
            else:
                pass
        except:
            print('插入失败')


@_read_data()
def _select():
    def find():
        s = input('查询条件（逗号隔开 1=123456,2=李四)\n')
        tmp_list = []
        con = s.split(',')
        cons = [s.split('=') for s in con]
        for stu in stu_list:
            flag = True
            for k, v in cons:
                if int(k) > 3:
                    v = _to_float(v)
                if stu[title_dict[k]] != v:
                    flag = False
                    break
            if flag:
                tmp_list.append(stu)
        if len(tmp_list) == 0:
            print('没有找到!')
        else:
            _show(stus=tmp_list)
            if input('是否排序？（y/n)').lower() == 'y':
                _sort(stus=tmp_list, flag=True)
            else:
                pass

    find()
    while True:
        if input('是否继续查找？(y/n)\n').lower() == 'y':
            find()
        else:
            break


@_read_data()
def _sort(stus=stu_list, flag=False):
    tmp = []

    def sort():
        item = input('请输入排序字段(1-6)(升序(1)降序(2))\n')
        items = item.split(' ')
        rev = True
        if items[1] == '1':
            rev = False
        if int(items[0]) > 3:
            tmp_list = sorted(stus, reverse=rev, key=lambda x: float(x[title_dict[items[0]]]))
        else:
            tmp_list = sorted(stus, reverse=rev, key=lambda x: x[title_dict[items[0]]])
        _show(tmp_list)
        tmp.append(tmp_list)

    sort()
    while True:
        if input('是否继续？(y/n)\n').lower() == 'y':
            sort()
        else:
            break
    if flag:
        pass
    else:
        if input('是否写入？(y/n)\n').lower() == 'y':
            _write_file(tmp[-1])
            global stu_list
            stu_list.clear()
            stu_list.extend(tmp[-1])


@_read_data()
def _del(stus=stu_list):
    tmp = stus[:]
    try:
        index = [x['学\t号'] for x in tmp].index(input('请输入学号：\n').strip())
        # print(index)
        print(tmp[index].to_show_str())
        if input('是否删除（y/n)') == 'y':
            del tmp[index]
            print('删除成功！')
            if input('是否写入（y/n)') == 'y':
                _write_file(tmp)
                stu_list.clear()
                stu_list.extend(tmp)
        else:
            pass
    except:
        print('未找到学号')


@_read_data()
def _edit(stus=stu_list):
    tmp = stus[:]
    try:
        index = [x['学\t号'] for x in tmp].index(input('请输入学号：\n').strip())
        print(tmp[index].to_show_str())
        tmp_stu = tmp[index]
        ed_str = input('请输入修改字段和值(1=123456,2=李四...)\n').split(',')
        ed_strs = [x.split('=') for x in ed_str]
        for k, v in ed_strs:
            if k == '2':
                v = _to_3(v)
            if int(k) > 3:
                v = _to_float(v)
            tmp_stu[title_dict[k]] = v
        if input('是否写入(y/n)：\n').lower() == 'y':
            _write_file(tmp)
            stu_list.clear()
            stu_list.extend(tmp)
        else:
            stu_list.clear()
    except:
        print('修改失败-----')
        stu_list.clear()


@_read_data()
def _stat():
    num_1 = {}
    num_2 = {}
    num_3 = {}
    nums = [num_1, num_2, num_3]
    data_1 = [float(x['微积分']) for x in stu_list]
    data_2 = [float(x['英语']) for x in stu_list]
    data_3 = [float(x['\t数据结构']) for x in stu_list]
    total_cou = [sum(data_1), sum(data_2), sum(data_3)]
    mean_cou = [s / len(stu_list) for s in total_cou]
    max_cou = [max(data_1), max(data_2), max(data_3)]
    min_cou = [min(data_1), min(data_2), min(data_3)]
    for x in stu_list:
        x['总成绩'] = _to_float(float(x['微积分']) + float(x['英语']) + float(x['\t数据结构']))
        x['平均分'] = _to_float(float(x['总成绩']) / 3)
    _show(stu_list, flag=True)
    print('总成绩:\t\t\t\t\t\t\t\t\t\t\t\t\t', '\t\t\t'.join(map(str, total_cou)))
    print('平均值:\t\t\t\t\t\t\t\t\t\t\t\t\t', '\t\t\t'.join(map(str, mean_cou)))
    print('最大值:\t\t\t\t\t\t\t\t\t\t\t\t\t', '\t\t\t'.join(map(str, max_cou)))
    print('最小值:\t\t\t\t\t\t\t\t\t\t\t\t\t', '\t\t\t'.join(map(str, min_cou)))
    for i, data in enumerate([data_1, data_2, data_3]):
        for n in data:
            if 0.0 <= n <= 10.0:
                if '0-10' in nums[i]:
                    nums[i]['0-10'] += 1
                else:
                    nums[i]['0-10'] = 1
            elif 11.0 <= n <= 20.0:
                if '11-20' in nums[i]:
                    nums[i]['11-20'] += 1
                else:
                    nums[i]['11-20'] = 1
            elif 21.0 <= n <= 30.0:
                if '21-30' in nums[i]:
                    nums[i]['21-30'] += 1
                else:
                    nums[i]['21-30'] = 1
            elif 31.0 <= n <= 40.0:
                if '31-40' in nums[i]:
                    nums[i]['31-40'] += 1
                else:
                    nums[i]['31-40'] = 1
            elif 41.0 <= n <= 50.0:
                if '41-50' in nums[i]:
                    nums[i]['41-50'] += 1
                else:
                    nums[i]['41-50'] = 1
            elif 51.0 <= n <= 60.0:
                if '51-60' in nums[i]:
                    nums[i]['51-60'] += 1
                else:
                    nums[i]['51-60'] = 1
            elif 61.0 <= n <= 70.0:
                if '61-70' in nums[i]:
                    nums[i]['61-70'] += 1
                else:
                    nums[i]['61-70'] = 1
            elif 71.0 <= n <= 80.0:
                if '71-80' in nums[i]:
                    nums[i]['71-80'] += 1
                else:
                    nums[i]['71-80'] = 1
            elif 81.0 <= n <= 90.0:
                if '81-90' in nums[i]:
                    nums[i]['81-90'] += 1
                else:
                    nums[i]['81-90'] = 1
            elif 91.0 <= n <= 100.0:
                if '91-100' in nums[i]:
                    nums[i]['91-100'] += 1
                else:
                    nums[i]['91-100'] = 1
    names = ['math', 'english', 'shujujiegou']
    for i, num in enumerate(nums):
        keys = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
        values = []
        for k in keys:
            values.append(num.get(k,0))
        plot(name=names[i], ydata=map(lambda x: x + '(' + str(num.get(x,0)) + 'p)', keys), xdata=values)


menu = {'0': _exit, '1': _init, '2': _show, '3': _edit, '4': _add, '5': _del, '6': _select, '7': _sort,
        '8': _stat}
if __name__ == '__main__':
    while True:
        print_menu()
        menu_id = input('请输入菜单编号: \n')
        try:
            menu[menu_id]()
        except KeyError as e:
            print(e)
            print('没有编号为%s这个菜单 请重输！' % e)
