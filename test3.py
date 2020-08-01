import pandas as pd
import numpy as np
import random
zeors_array = np.zeros( (10, 10) )
print(zeors_array)

massive=[[1,1,1,1],[1,1,1],[1,1,1],[1,1],[1,1],[1,1], [1],[1],[1],[1]]


def check(zeors_array,b,c,a):
    if b==0:
        bb=0
    else:
        bb=1
    if b==9:
        cc=0
    elif b==8:
        cc=1
    else: cc=2
    if c==0:
        aa = zeors_array[c:c + 2, b - bb:b + len(a) + cc]
    elif c==9:
        aa = zeors_array[c-1:c, b - bb:b + len(a) + cc]
    else:
        aa = zeors_array[c - 2:c+2, b - bb:b + len(a) + cc]
    # print(aa)
    if aa.sum()>0:
        return False
    else:
        return True

def check2(zeors_array,b,c,a):
    if b==0:
        bb=0
    else:
        bb=1
    if b==9:
        cc=0
    elif b==8:
        cc=1
    else: cc=2
    if c==0:
        aa = zeors_array[c:c+ len(a) + 2,b:b + cc]
    elif c==9:
        aa = zeors_array[c - 1:c, b-bb:b+cc ]
    else:
        aa = zeors_array[c - 1:c + len(a) + 2, b - bb:b+cc]
    # print(aa)
    if aa.sum()>0:
        return False
    else:
        return True
def check1(zeors_array,b,c,a):
    if b==0:
        bb=0
    else:
        bb=1
    if b==9:
        cc=0
    elif b==8:
        cc=1
    else: cc=2
    if c==0:
        aa = zeors_array[c:c + 2, b - len(a)-bb:b  + cc]
    elif c==9:
        aa = zeors_array[c-1:c, b - len(a)-bb:b  + cc]
    else:
        aa = zeors_array[c - 2:c+2, b - len(a)-bb:b  + cc]
    # print(aa)
    if aa.sum()>0:
        return False
    else:
        return True

string_ru='АБВГДЕЖЗИЙ'
reponse=[]
for a in massive:
  flag=True

  while flag:
    position=[]
    b=random.randint(0,9)
    c = random.randint(0, 9)
    if (b+len(a)<=10 and check(zeors_array,b,c,a)):
        flag=False
        aa=[]
        count=a.__len__()
        for i in range (0,10):
            if i>=b and i<=b+len(a) and count>0 :
                zeors_array[c][i]=1
                position.append(string_ru[i]+str(c))
                count-=1

    elif (c+len(a)<10 and check2(zeors_array,b,c,a)):
        flag=False

        count=len(a)
        for i in range(0,10):
            if i>=c and i<=c+len(a) and count>0 :
                zeors_array[i][b]=1
                position.append(string_ru[b] + str(i))
                count-=1
    elif (b-len(a)>=0 and check1(zeors_array,b,c,a)):
        flag=False
        count=len(a)
        for i in range(9,0,-1):
            if i<=b and i>=b-len(a) and count>0 :
                zeors_array[c][i]=1
                position.append(string_ru[i] + str(c))
                count-=1

    print(zeors_array)
    if flag == False:
        reponse.append(position)
    print('\n')

data=pd.DataFrame(data=zeors_array, columns=['А','Б','В','Г','Д','Е','Ж','З','И','Й'])
# print(data)
# ход пользователя
print('Введите позицию')



flag=True
while True:
    step = input()
    if (step.__len__() > 3):
        print('Вы ввели неверную позицию')
        continue
    try:
        temp=data[step.split(',')[0]][int(step.split(',')[1])]
        if temp==1:
            for aa in reponse:
                if step.replace(',','') in aa:
                    aa.remove(step.replace(',',''))
                    if aa.__len__()==0:
                        print('Убил')
                        reponse.remove(aa)
                        if (reponse.__len__()==0):
                            flag=False
                            print('Вы выиграли')
                    else:
                        print('Ранил')
        else:
            print('мимо')
    except Exception as e:
        print('error')
