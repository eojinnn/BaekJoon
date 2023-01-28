"""cnt = int(input())
Page = [x for x in range(10000)] #가로부터 1~100
# 전체 페이지
for i in range(cnt):
    Rec = []
    R, L = map(int,input().split())
    #전체 페이지에서 채워진 부분 제외
    for j in range(L,L+11):
        Rec.append(x for x in range(100*j+R,100*j+R+11))
    for x in Page:
        if x in Rec:
            Page.remove(x)"""

cnt = int(input())
Rec = []
for i in range(cnt):
    R,L = map(int,input().split())
    for j in range(L,L+10):
        for k in range(100*j+R,100*j+R+10):
            if k not in Rec:
                Rec.append(k)
print(len(Rec))


    

