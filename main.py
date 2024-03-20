def in_for_func(el):
    """
    Help to unpuk element
    el - element from sp
    """
    return [int(el[0][5]), int(el[0][6]), len(el[1])]

def func(el):
    """
    Given function
    xd, yd - vector coords
    el = element from sp 
    """
    xd, yd = list(map(lambda x: int(x), el[2].split()))
    n = in_for_func(el)
    if n[0] > 5:
        x = n[0] + xd
    elif n[0] <= 5:
        x = -1*(n[0] + xd) * 4 + n[2]
    if n[1] > 3:
        y = n[1] + n[2] + yd
    elif n[1] <= 3:
        y = -1 * (n[0] + yd) * n[1]
    return [x, y]


with open('space.txt', encoding='utf-8') as file:
    _ = file.readline()
    sp = [i.split('*') for i in file.readlines()]
    for i in range(len(sp)):
        if sp[i][-2] == '0 0':
            sp[i] = sp[i][:-2] + func(sp[i]) + list(map(lambda x: int(x), sp[i][-1].split()))
        else:
            sp[i] = sp[i][:-2] + list(map(lambda x: int(x), sp[i][-2].split())) + list(map(lambda x: int(x), sp[i][-1].split()))
    print(sp[3])
        
    