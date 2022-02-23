input_str = input()
target_str = input()

def index_str(index_order):
    s1, s2 = len(input_str), len(target_str)

    if index_order + s2 - 1 >= s1:
        return False
    for k in range(s2):
        if input_str[index_order + k] != target_str[k]:
            return False
    return True



def find_index():
    n = len(input_str)
    for i in range(n):
        if index_str(i):
            return i
    return -1

print(find_index())