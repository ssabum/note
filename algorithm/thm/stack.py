class stack:
    # 리스트를 사용하여 stack 생성
    def __init__(self):
        self.top = []
    def __len__(self):
        return len(self.top)
    def __str__(self):
        return str(self.top[::1])

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()

    def clear(self):
        self.top = []

    def isContain(self, item):
        return item in self.top

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()

    def isEmpty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)

s = stack()
s.push("hi")
s.push("hi")
s.push("hi")
s.pop()
print(s)

# stack = []
#
# input_string = "()()(())()()()"
#
# for s in input_string:
#     if s == "(":
#         stack.append(s)
#     else:
#         if not len(stack):
#             result = False
#             break
#         stack.pop()
#
# if len(stack):
#     result = False
# else:
#     result = True
#
# print(result)
