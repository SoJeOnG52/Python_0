#일반함수르 람다함수로 바꾸기
def avg(data):
    return sum(data)/len(data)

d=[20,15,18,20]
print(avg(d))
s1=tuple(map(str,d))
print(s1)
avg1=lambda data : sum(data)/len(data)
print(avg1(d))
