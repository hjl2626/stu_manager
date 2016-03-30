import json


class Student(dict):
    # __slots__ = ('学号', '姓名', '性别', '微积分', '英语', '数据结构', '总成绩', '平均分')
    title = ('学\t号', '姓\t名', '性别', '微积分', '英语', '\t数据结构', '总成绩', '平均分')

    def __init__(self, names=(), values=(), **kw):
        super(Student, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Student' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def __str__(self):
        return json.dumps(self).replace(':', '=')

    def __cmp__(self, other):
        pass

    def to_show_str(self, flag=False):
        if flag:
            return '\t\t\t'.join([self[t] for t in self.title])
        else:
            return '\t\t\t'.join([self[t] for t in self.title[:-2]])

    def to_write_str(self, flag=False):
        if flag:
            return ','.join([self[t] for t in self.title])
        else:
            return ','.join([self[t] for t in self.title[:6]])
