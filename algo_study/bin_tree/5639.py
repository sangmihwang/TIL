# def postorder(root):
    



pre = []
for _ in range(100):
    N = int(input())
    pre.append(N)
left = [0] * len(N)
right = [0] * len(N)


for i in range(len(pre)-1):
    if left[pre[i]] == 0:
        left[pre[i]] = pre[i+1]
    else:
        right[pre[i]] = pre[i+1]




