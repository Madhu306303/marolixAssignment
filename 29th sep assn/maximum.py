list_a = [30, 36, 88, 45, 43]
def maxNum(a):
    res = a[0]
    for i in range(1,len(a)):
        if res < a[i]:
           res = a[i]
    print(res)
maxNum(list_a)