"""
Стек с поддержкой максимума
Реализовать стек с поддержкой операций push, pop и max.
Вход. Последовательность запросов push, pop и max .
Выход. Для каждого запроса max вывести максимальное
число, находящееся на стеке.
"""
n = int(input())
my_stack = []
max_in_stack = []
i = 0
while i < n:
    inp_command = list(map(str, input().split()))
    if inp_command[0] == "push":
        if not my_stack:
            my_stack.append(int(inp_command[1]))
            max_in_stack.append(int(inp_command[1]))
        else:
            my_stack.append(int(inp_command[1]))
            if int(inp_command[1]) >= max_in_stack[-1]:
                max_in_stack.append(inp_command[1])
            else:
                max_in_stack.append(max_in_stack[-1])
    if inp_command[0] == "max":
        print(max_in_stack[-1])
    if inp_command[0] == "pop":
        my_stack.pop()
        max_in_stack.pop()
    i += 1
