from time import time

def timedeco(f): #함수의 5회 실행시간 평균내는 데코레이터
    def wrapper():
        timelst = []
        for _ in range(5):
            s = time()
            f()
            e = time()
            timelst.append(e-s)
        return sum(timelst)/5
    return wrapper

@timedeco
def firstfunction():
    lst = list(range(20))
    SUM = 0
    for i in range(1<<20):
        sum = 0
        for j in range(i.bit_length()):
            if i & 1<<j:
                sum += lst[j]
        if sum > SUM:
            SUM = sum

@timedeco
def secondfunction():
    lst = list(range(20))
    SUM = 0
    sum = 0
    for i in range(1, 1<<20):
        for j in range(i.bit_length()):
            if i & 1<<j:
                sum += lst[j]
                break
            else:
                sum -= lst[j]
        if sum > SUM:
            SUM = sum

@timedeco
def thirdfunction():
    lst = list(range(20))
    WArr = [0] + lst[:]
    acc = lst[0]
    for i in range(2, 21):
        WArr[i] -= acc
        acc += lst[i-1]
    SUM = 0
    sum = 0
    for i in range(1, 1<<20):
        sum += WArr[(i ^ (i-1)).bit_length()]
        if sum > SUM:
            SUM = sum

print(firstfunction(), secondfunction(), thirdfunction())