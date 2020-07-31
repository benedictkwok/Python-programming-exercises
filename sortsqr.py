'''give a sorted list, print the sorted square of the list'''
ls1=[-9,-2,3,4,5]

def sortsql(ls1):
    left=0
    right=len(ls1) -1
    result = [0] * len(ls1)
    for x in range(right,-1,-1):
        print(x)
        if abs(ls1[left]) > abs(ls1[right]):
            result[x] = ls1[left] ** 2
            print('left', left)
            left=left+1
        else:
            result[x] = ls1[right] **2
            print('right', right)
            right=right-1
    return result
result = sortsql(ls1)
print(list(result))
