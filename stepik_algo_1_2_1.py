"""
Формат входа.
Строка s[1 . . . n], состоящая из заглавных и прописных букв латинского алфавита, цифр,
знаков препинания и скобок из множества []{}().

Формат выхода.
Если скобки в s расставлены правильно, выведите
строку “Success". В противном случае выведите индекс (используя индексацию с единицы) первой закрывающей скобки, для
которой нет соответствующей открывающей. Если такой нет, выведите индекс первой открывающей скобки, для которой нет
соответствующей закрывающей.
"""


def br_check(test_string):
    my_stack = []
    op_br = ["(", "[", "{"]
    cl_br = [")", "]", "}"]
    # Кладём скобки на стек
    for ind in range(len(test_string)):
        if test_string[ind] in op_br:
            my_stack.append(ind)
        elif test_string[ind] in cl_br:
            # Если стек пуст и встретилась закрывающая скобка - выход
            if not my_stack:
                return ind + 1
            # Снимаем скобку со стека и проверяем элиминируются они. Если скобки не совпадают - выходим
            top_el = my_stack.pop()
            if test_string[top_el] == "(" and test_string[ind] != ")" or \
                    test_string[top_el] == "[" and test_string[ind] != "]" or \
                    test_string[top_el] == "{" and test_string[ind] != "}":
                return ind + 1
    # Если в стеке что-то осталось - возвращаем индекс последнего элемента
    if my_stack:
        return my_stack[-1] + 1
    else:
        return "Success"


print(br_check(input()))
