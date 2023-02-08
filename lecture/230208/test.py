li = ['A','B','C','D','A']
print(li[3:0])


def reverse(list):
    r_list = []
    for i in range(len(list)):
        r_list.append(list[-(i+1)])
    return r_list

print(reverse(li))
