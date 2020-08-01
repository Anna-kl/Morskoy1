import pickle

import pandas as pd
import numpy as np
import random
import os
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

class Play():
    zeors_array = np.zeros( (10, 10) )
    massive = [[1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1], [1], [1], [1]]
    string_ru = 'АБВГДЕЖЗИЙ'
    reponse=[]
    def __init__(self):
        pass

    def generate_position(self):

            for a in self.massive:
              flag=True
              while flag:
                position=[]
                b=random.randint(0,9)
                c = random.randint(0, 9)
                if (b+len(a)<=10 and check(self.zeors_array,b,c,a)):
                    flag=False
                    count=a.__len__()
                    for i in range (0,10):
                        if i>=b and i<=b+len(a) and count>0 :
                            self.zeors_array[c][i]=1
                            position.append(self.string_ru[i]+str(c))
                            count-=1

                elif (c+len(a)<10 and check2(self.zeors_array,b,c,a)):
                    flag=False

                    count=len(a)
                    for i in range(0,10):
                        if i>=c and i<=c+len(a) and count>0 :
                            self.zeors_array[i][b]=1
                            position.append(self.string_ru[b] + str(i))
                            count-=1
                elif (b-len(a)>=0 and check1(self.zeors_array,b,c,a)):
                    flag=False
                    count=len(a)
                    for i in range(9,0,-1):
                        if i<=b and i>=b-len(a) and count>0 :
                            self.zeors_array[c][i]=1
                            position.append(self.string_ru[i] + str(c))
                            count-=1


                if flag == False:
                    self.reponse.append(position)

    def save_file(self):
        data = pd.DataFrame(data=self.zeors_array, columns=['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й'])
        name_file='file_'
        for i in range(0,5):
            name_file+=str(random.randint(0,9))
        name_file+='.txt'
        data.to_csv('D://data//Morskoy1//'+name_file, sep=';', index=None)
        with open('D://data//Morskoy2//'+name_file, 'wb') as f:
                      pickle.dump(self.reponse, f)
        return name_file

    def step_add(self, position, file):
        data=pd.read_csv('D://data//Morskoy1//'+file, sep=';')
        with open('D://data//Morskoy2//'+file, 'rb') as f:
            self.reponse = pickle.load(f)
        try:
            word=position.split(',')[0]
            temp = data[word][int(position.split(',')[1])]
            data[word][int(position.split(',')[1])]=-1
            if temp == 1:
                position=position.replace(',','')
                for aa in self.reponse:
                    if position in aa:
                        aa.remove(position)
                        if aa.__len__() == 0:
                            send= 'Убил'
                            break
                        else:
                            send= 'Ранил'
                            break
                data.to_csv('D://data//Morskoy1//' + file, sep=';', index=None)
                with open('D://data//Morskoy2//' + file, 'wb') as f:
                    pickle.dump(self.reponse, f)
            else:
                return  'мимо'
        except Exception as e:
            send= 'error'
        return send
