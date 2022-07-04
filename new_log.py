from log_decorator import log_decorator

# Применение декоратора к домашке

class Stack:
    def __init__(self):
        self.mylist = []

    def isEmpty(self):
        if len(self.mylist) == 0:
            print('True')
        else:
            print('False')

    def push(self, element):
        self.mylist.append(element)

    def pop(self):
        if len(self.mylist) == 0:
            pass
        else:
            popped = self.mylist.pop()
            return popped

    def peek(self):
        return self.mylist[-1]


    def size(self):
        if len(self.mylist) <= 0:
            pass
        else:
            length = len(self.mylist)

            return length

# f = Stack()
# f.isEmpty()
# f.push(5)
# f.push(8)
# f.push(10)
# f.push(11)
# f.push(25)
# f.push(100)
# print(f.mylist)
# #
# print(f.pop())
# print(f.mylist)
#
# print(f.peek())
# print(f.size())
# f.isEmpty()
@log_decorator
def check(symbols):
    round_l = Stack()
    round_r = Stack()
    sq_l = Stack()
    sq_r = Stack()
    fig_l = Stack()
    fig_r = Stack()
    for el in symbols:
        if el == '(':
            round_l.push(el)
        elif el == ')':
            round_r.push(el)
        elif el == '[':
            sq_l.push(el)
        elif el == ']':
            sq_r.push(el)
        elif el == '{':
            fig_l.push(el)
        elif el == '}':
            fig_r.push(el)

    if round_r.size() == round_l.size() and sq_r.size() == sq_l.size() and fig_r.size() == fig_l.size():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

check('(((([{}]))))')
# print(check('(((([{}]))))'))
# print(check('[([])((([[[]]])))]'))
# print(check('{()}'))
# print(check('{{[()]}}'))
# print(check('}{}'))
# print(check('{{[(])]}}'))
# print(check('[[{())}]'))

