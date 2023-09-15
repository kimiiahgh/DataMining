from scipy.io.arff import loadarff
import scipy as sp
from io import StringIO
import numpy as np
import random
totaldata=[]
dataset=loadarff(open('ThyroidData.arff','r'))
satr=[]
for i in range(0,1034):
    satr.append(i)
satr=random.sample(satr,len(satr))
tdata=satr[0:827]#  data train
testdata=satr[828:] # data test
f_e=[]
num=[]
nom=[]
e=[] #list error 
indnom=[1,2,3,4,5,6,7,8,9,10,11,12,13]
indnum=[0,14,15,16,17,18]
A=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
def numeric (ykm,indx):
    mini=0
    l_vc=[] #list of (value,class)
    avg=0
    l_h=[] 
    splt=[]#list split (avg,(maxx1,maxx2),error)
    for b in range(0,len(indx)):
        l_h.append(dataset[0][indx[b]][ykm])
        l_h.append(dataset[0][indx[b]][19])
        l_h.append(indx[b])
        l_vc.append(l_h)
        l_h=[]
    l_vc.sort(key=lambda l:l[0])
    hichi=True   
    for x in l_vc:
        if x[0]==l_vc[0][0]:
            hichi=True
        else:
            hichi=False
    if len(l_vc)==1:
        f_e.append((0,ykm))
    elif hichi==False:   

        c=0 #counter  0 to 1034
        flag=True 
        flag2=True
        while flag==True:
            if hichi ==True:
                break
           
            a=l_vc[c][0] 
            if l_vc[c][0]!=a:
                 if l_vc[c][0]==l_vc[len(l_vc)-1]:
                     flag2=False
            while l_vc[c][0]==a:
                c=c+1
                if c==len(l_vc)-1:
                    break   
               
            if flag==True:
                avg=(l_vc[c][0]+l_vc[c-1][0])/2
         
                i=0
                n1=0
                n2=0
                n3=0
                cmax=0
                error=0
        
                while i!=c:
                    if l_vc[i][1]==b'1':
                        n1=n1+1
                        i=i+1
                    elif l_vc[i][1]==b'2':
                        n2=n2+1
                        i=i+1
                    elif l_vc[i][1]==b'3':
                        n3=n3+1
                        i=i+1         
                cmax = max(n1 , n2, n3)
                if n1 == cmax :
                    maxx1 = b'1'
                    error=n2+n3
                elif n2 == cmax:
                    maxx1 = b'2'
                    error=n3+n1
                elif n3 == cmax:
                    maxx1 = b'3'
                    error=n1+n2
                i=c
                n1=0
                n2=0
                n3=0
                cmax=0
                while i!=len(l_vc):
                    if l_vc[i][1]==b'1':
                        n1=n1+1
                        i=i+1
                    elif l_vc[i][1]==b'2':
                        n2=n2+1
                        i=i+1
                    elif l_vc[i][1]==b'3':
                        n3=n3+1
                        i=i+1 
                if c==len(l_vc)-1:
                    cmax=1
                    maxx2=l_vc[c][1]
                else: 
                    cmax = max(n1 , n2, n3)
                    if n1 == cmax :
                        maxx2 = b'1'
                        error=error+n2+n3
                    elif n2 == cmax:
                        maxx2 = b'2'
                        error=error+n3+n1
                    elif n3 == cmax:
                        maxx2 = b'3'
                        error=error+n1+n2
                if flag2==False:
                    flag==False   
                h=[]
                h.append(error)
                h.append(avg)
                h.append(maxx1)
                h.append(maxx2)
                splt.append(h)
                h=[]
                if c==len(l_vc)-1:
                    flag=False           
        mini=min(x for x in splt)
        minim=mini[0]
        for j in range(0,len(splt)):
            if splt[j][0]==minim:
                index=j
                break
        num.append((ykm,splt[index][0],splt[index][1],splt[index][2],splt[index][3]))
        f_e.append((minim,ykm))
        e.append(minim)
        return minim
def nominal(kmy,indx):
    lsefr=[]
    lyek=[]
    lnom=[]
    l_h=[]
    n1=0
    n2=0
    n3=0
    cmax=0
    error=0  
    for t in range(0,len(indx)):
        if dataset[0][indx[t]][kmy]==b'0':
            l_h.append(dataset[0][indx[t]][kmy])
            l_h.append(dataset[0][indx[t]][19])
            l_h.append(indx[t])
            lsefr.append(l_h)
            l_h=[]
        else:
            l_h.append(dataset[0][indx[t]][kmy])
            l_h.append(dataset[0][indx[t]][19])
            l_h.append(indx[t])
            lyek.append(l_h)
            l_h=[]
    if not not lsefr:
        maxx0=lsefr[0][1]      
        for i in range(0 , len(lsefr)):
            if lsefr[i][1]== b'1':
                n1 = n1 + 1
            elif lsefr[i][1]== b'2':
                n2 = n2 + 1
            elif lsefr[i][1]== b'3':
                n3 = n3 + 1
        cmax = max(n1 , n2, n3)
        if n1 == cmax :
            maxx0 = b'1'
            error=n2+n3
        elif n2 == cmax:
            maxx0 = b'2'
            error=n1+n3
        elif n3 == cmax:
            maxx0 = b'3'
            error=n2+n1
        h=[]
        h.append(lsefr[0][0])
        h.append(maxx0)
        h.append(error)
        lnom.append(h)
        h=[]
    n1=0
    n2=0
    n3=0
    cmax=0
    if not not lyek:
        maxx1=lyek[0][1]
        for i in range(0 , len(lyek)):
            if lyek[i][1]== b'1':
                n1 = n1 + 1
            elif lyek[i][1]== b'2':
                n2 = n2 + 1
            elif lyek[i][1]== b'3':
                n3 = n3 + 1
        cmax = max(n1 , n2, n3)
        if n1 == cmax :
            maxx1 = b'1'
            error=error+n2+n3
        elif n2 == cmax:
            maxx1 = b'2'
            error=error+n1+n3
        elif n3 == cmax:
            maxx1 = b'3'
            error=error+n1+n2
        h=[]
        h.append(lyek[0][0])
        h.append(maxx1)
        h.append(error)
        lnom.append(h)
        h=[]   
    f_e.append((error,kmy))
    e.append(error)
    if not lsefr:
        nom.append((kmy,error,lyek[0][0],maxx1))
    elif not lyek:
        nom.append((kmy,error,lsefr[0][0],maxx0))
    else: 
        nom.append((kmy,error,lyek[0][0],lsefr[0][0],maxx1,maxx0))
    return error        
def classmax(D):
    n1=0
    n2=0
    n3=0
    cmax=0
    for k in range(0,len(D)):
        if dataset[0][D[k]][19]==b'1':
            n1=n1+1
        elif dataset[0][D[k]][19]==b'2':
            n2=n2+1
        elif dataset[0][D[k]][19]==b'3':
            n3=n3+1
    cmax=max(n1,n2,n3)
    if n1 == cmax :
        maxx = b'1'
    elif n2 == cmax:
        maxx = b'2'
    elif n3 == cmax:
        maxx = b'3'
    return(maxx)   
d_org=[]
class Tree:
    label=None
    feature=None
    leftchild=None
    rightchild=None
    avg=0
count=[]  
def missclassification(D,A):
    ####
    for x in A:
        if x in indnum:
            numeric(x,D)
        else:
            nominal(x,D)       
    j=0
    flag=True
    while flag==True:
        if len(D)==0:
            break
        elif len(D)==1:
            flag=True
            break
        else:
            if dataset[0][D[j]][19]==dataset[0][D[j+1]][19]: #hamgen budn
                j=j+1
                if j==len(D)-1:
                    break
            else:
                flag=False
    if flag==True:
        f_e.clear()
        e.clear()
        leaf=Tree()
        leaf.feature=None
        leaf.label=dataset[0][D[0]][19]
        leaf.leftchild=None
        leaf.rightchild=None
        leaf.avg=None
        return leaf
    elif not A or not f_e :
        f_e.clear()
        e.clear()
        leaf=Tree()
        leaf.feature=None
        leaf.label=classmax(D)
        leaf.leftchild=None
        leaf.rightchild=None
        leaf.avg=None
        return leaf
    else :
        minf=min(f_e)
        bf=minf[1]
        Av=A.copy()
        Av.remove(bf)
        #print(bf)
        #print(f_e)
        d_org.append(D.copy())
        e.clear()
        f_e.clear()
        node=Tree()
        ####
        #####
        node.feature=bf
        node.label=None
        D1=[]
        D2=[]
        if bf in indnum:
            for i in range(0,len(num)):
                 if num[i][0]==bf:
                    andis=i
                    break
            avg=num[andis][2]
            node.avg=avg
            for g in range(0,len(D)):
                if dataset[0][D[g]][bf]<avg:
                    D1.append(D[g])
                else:
                    D2.append(D[g])
            if not not D1:
                node.leftchild=missclassification(D1,Av)
            if not not D2:
                node.rightchild=missclassification(D2,Av)
        else:
            for h in range(0,len(D)):
                if dataset[0][D[h]][bf]==b'0':
                    D1.append(D[h])
                else :
                    D2.append(D[h])
            if not not D1:
                node.leftchild=missclassification(D1,Av)
            if not not D2:
                node.rightchild=missclassification(D2,Av) 
        return node  
def errornode(instance,node):
    if(node==None):
        return
    if node!=None and node.feature==None:
        if dataset[0][instance][19]==node.label:
            return True
        else:
            return False
    elif node!=None:
        f=node.feature
        if f in indnum:
            avge=node.avg
            if dataset[0][instance][f]<avge:
                return errornode(instance,node.leftchild)
            else:
                return errornode(instance,node.rightchild)
        else:
            if dataset[0][instance][f]==b'0':
                return errornode(instance,node.leftchild)
            else:
                return errornode(instance,node.rightchild)
ee=0
root=missclassification(tdata,A)
for i in range(0,len(testdata)):
    if errornode(testdata[i],root)==False:
        ee=ee+1
print(ee/len(testdata))
print("error test missclassification")
print(1-(ee/len(testdata)))
print("accuracy test missclassification")
for i in range(0,len(tdata)):
    if errornode(tdata[i],root)==False:
        ee=ee+1
print(ee/len(tdata))
print("error train missclassification")
print(1-(ee/len(tdata)))
print("accuracy train missclassification")
avglst=[]
AIG=[]            
import math
def entropy(D): #D = instance ha
    n1=0
    n2=0
    n3=0
    for i in range(0 , len(D)):
        if dataset[0][D[i]][19]== b'1':
            n1 = n1 + 1
        elif dataset[0][D[i]][19]== b'2':
            n2 = n2 + 1
        else :
            n3 = n3 + 1
    p = []
    p.append(n1/len(D))
    p.append(n2/len(D))
    p.append(n3/len(D))
    sument = 0
    for i in range(0,3):
        if p[i] != 0:
            sument = sument - (p[i]*(math.log2(p[i])))
        else:
            continue
    return sument
D = [9 , 62 , 364,631,632,767,794,1025,899]  
enti= entropy(D)
AIG=[]

def IGnom(D , f):
    D1=[]
    D2=[]
    if f in indnom:
        for i in range(0 , len(D)):
            if dataset[0][D[i]][f] == b'0':
                D1.append(D[i])
            elif dataset[0][D[i]][f] == b'1':
                D2.append(D[i])
        if not not D1 and not not D2:       
            IG = entropy(D) - ((len(D1)/len(D))*entropy(D1)) - ((len(D2)/len(D))*entropy(D2))
            AIG.append((IG,f))
            
def IGnum(D,f):
    c=0
    l_vc=[]
    l_h=[]
    for b in range(0,len(D)):
        l_h.append(dataset[0][D[b]][f])
        l_h.append(dataset[0][D[b]][19])
        l_h.append(D[b])
        l_vc.append(l_h)
        l_h=[]
    l_vc.sort(key=lambda l:l[0])
    a = l_vc[c][0]
    split=[]
    flagmosavi = True
    for x in l_vc:
        if x[0]== l_vc[0][0]:
            flagmosavi=True
        else:
            flagmosavi = False
            break
    while c != len(l_vc):
        if l_vc[c][0]==a :
            c = c+1
            if c== len(l_vc) and flagmosavi == True:
                break
        else:
            a = l_vc[c][0]
            avg =( l_vc[c][0]+ l_vc[c-1][0])/2
            D1=[]
            D2=[]
            for i in range (0,len(l_vc)):
                if l_vc[i][0]< avg:
                    D1.append(l_vc[i][2])
                else:
                    D2.append(l_vc[i][2])
            IG = entropy(D) - ((len(D1)/len(D))*entropy(D1)) - ((len(D2)/len(D))*entropy(D2))
            split.append((IG , avg))
            if c == len(l_vc)-1:
                break
    if flagmosavi!= True:
        split.sort(key=lambda l:l[0])
        bestsplit = split[len(split)-1]
        AIG.append((bestsplit[0],f))
        avglst.append((f,bestsplit[1]))
def issame(D):
    a = dataset[0][D[0]][19]
    flag = True
    for i in range(1 ,len(D)):
        if a != dataset[0][D[i]][19]:
            flag = False
            break
    if flag == True:
        return True
    else:
        return False
def BFIG(D,A):  
    for x in A:
        if x in indnum:
            IGnum(D,x)
        else:
            IGnom(D,x)          
    if issame(D)== True:
        leaf = Tree()
        leaf.feature = None
        leaf.leftchild=None
        leaf.rightchild=None
        leaf.label=dataset[0][D[0]][19]
        leaf.avg=None
        return leaf
    elif not A or not AIG:
        leaf = Tree()
        leaf.feature = None
        leaf.leftchild=None
        leaf.rightchild=None
        leaf.avg=None
        leaf.label= classmax(D)
        return leaf
    else:
        maxi=max(AIG)
        bf=maxi[1]
        AIG.clear()
        Av=A.copy()
        Av.remove(bf)
        node = Tree()
        node.feature= bf
        node.label=None
        D1=[]
        D2=[]
        if bf in indnom:
            for h in range(0,len(D)):
                if dataset[0][D[h]][bf]==b'0':
                    D1.append(D[h])
                else :
                    D2.append(D[h])
            if not not D1:
                node.leftchild=BFIG(D1,Av)
            if not not D2:
                node.rightchild=BFIG(D2,Av) 
        else:
            for i in range(0 , len(avglst)):
                if bf == avglst[i][0]:
                    andiss=i
            node.avg=avglst[andiss][1]
            avglst.clear()
            for j in range(0 , len(D)):
                if dataset[0][D[j]][bf] < node.avg:
                      D1.append(D[j])
                else:
                      D2.append(D[j])
            node.leftchild = BFIG(D1 , Av)
            node.rightchild = BFIG(D2 , Av)           
        return node               
ee=0   
root=BFIG(tdata,A)
for i in range(0,len(testdata)):
    if errornode(testdata[i],root)==False:
        ee=ee+1
print(ee/len(testdata)) 
print(" error test IG")
print(1-(ee/len(testdata))) 
print(" accuracy test IG")
for i in range(0,len(tdata)):
    if errornode(tdata[i],root)==False:
        ee=ee+1
print(ee/len(tdata)) 
print(" error train IG") 
print(1-(ee/len(tdata)))
print(" accuracy train IG")      
AGINI=[]
def gini(D):
    n1=0
    n2=0
    n3=0
    for i in range(0 , len(D)):
        if dataset[0][D[i]][19]== b'1':
            n1 = n1 + 1
        elif dataset[0][D[i]][19]== b'2':
            n2 = n2 + 1
        else :
            n3 = n3 + 1
    p = []
    p.append(n1/len(D))
    p.append(n2/len(D))
    p.append(n3/len(D))
    s=0
    for j in range(0,3):
        s=s+(p[j]*p[j])
    g=1-s
    return g
def Gininom(D , f):
    D1=[]
    D2=[]
    if f in indnom:
        for i in range(0 , len(D)):
            if dataset[0][D[i]][f] == b'0':
                D1.append(D[i])
            elif dataset[0][D[i]][f] == b'1':
                D2.append(D[i])
        if not not D1 and not not D2:
            alfa = gini(D) - ((len(D1)/len(D))*gini(D1)) - ((len(D2)/len(D))*gini(D2))
            AGINI.append((alfa,f))
avglst=[]   
def Gininum(D , f):
    c=0
    l_vc=[]
    l_h=[]
    for b in range(0,len(D)):
        l_h.append(dataset[0][D[b]][f])
        l_h.append(dataset[0][D[b]][19])
        l_h.append(D[b])
        l_vc.append(l_h)
        l_h=[]
    l_vc.sort(key=lambda l:l[0])
    a = l_vc[c][0]
    split=[]
    flagmosavi = True
    for x in l_vc:
        if x[0]== l_vc[0][0]:
            flagmosavi=True
        else:
            flagmosavi = False
            break
    while c != len(l_vc):
        if l_vc[c][0]==a :
            c = c+1
            if c== len(l_vc) and flagmosavi == True:
                break
        else:
            a = l_vc[c][0]
            avg =( l_vc[c][0]+ l_vc[c-1][0])/2
            D1=[]
            D2=[]
            for i in range (0,len(l_vc)):
                if l_vc[i][0]< avg:
                    D1.append(l_vc[i][2])
                else:
                    D2.append(l_vc[i][2])
            alfa = gini(D) - ((len(D1)/len(D))*gini(D1)) - ((len(D2)/len(D))*gini(D2))
            split.append((alfa , avg))
            if c == len(l_vc)-1:
                break
    if flagmosavi!= True:
        split.sort(key=lambda l:l[0])
        bestsplit = split[len(split)-1]
        AGINI.append((bestsplit[0],f))
        avglst.append((f,bestsplit[1]))
def BFGini(D , A):
    for x in A:
        if x in indnum:
            Gininum(D,x)
        else:
            Gininom(D,x)            
    if issame(D)== True:
        leaf = Tree()
        leaf.feature = None
        leaf.leftchild=None
        leaf.rightchild=None
        leaf.label=dataset[0][D[0]][19]
        leaf.avg=None
        return leaf
    elif not A or not AGINI:
        leaf = Tree()
        leaf.feature = None
        leaf.leftchild=None
        leaf.rightchild=None
        leaf.avg=None
        leaf.label= classmax(D)
        return leaf
    else:
        maxi=max(AGINI)
        bf=maxi[1]
        AGINI.clear()
        Av=A.copy()
        Av.remove(bf)
        node = Tree()
        node.feature= bf
        node.label=None
        D1=[]
        D2=[]
        if bf in indnom:
            for h in range(0,len(D)):
                if dataset[0][D[h]][bf]==b'0':
                    D1.append(D[h])
                else :
                    D2.append(D[h])
            if not not D1:
                node.leftchild=BFGini(D1,Av)
            if not not D2:
                node.rightchild=BFGini(D2,Av) 
        else:
            for i in range(0 , len(avglst)):
                if bf == avglst[i][0]:
                    andiss=i
            node.avg=avglst[andiss][1]
            avglst.clear()
            for j in range(0 , len(D)):
                if dataset[0][D[j]][bf] < node.avg:
                      D1.append(D[j])
                else:
                      D2.append(D[j])
            node.leftchild = BFGini(D1 , Av)
            node.rightchild = BFGini(D2 , Av)           
        return node               
ee=0
root=BFGini(tdata,A)
for i in range(0,len(testdata)):
    if errornode(testdata[i],root)==False:
        ee=ee+1
print(ee/len(testdata)) 
print("error test gini") 
print(1-(ee/len(testdata))) 
print("accuracy test gini")
for i in range(0,len(tdata)):
    if errornode(tdata[i],root)==False:
        ee=ee+1
print(ee/len(tdata)) 
print("error train gini")         
print(1-(ee/len(tdata)) )
print("accuracy train gini")    
print("##############")         
root=missclassification(tdata,A)
print(root.feature,"root")
lch=root.leftchild
print(lch.feature,"root leftchild")
rch=root.rightchild
print(rch.feature,"root rightchild")
lch_lch=lch.leftchild
print(lch_lch.feature,"leftchild of",lch.feature)
lch_rch=lch.rightchild
print(lch_rch.feature,"rightchild of",lch.feature)
rch_rch=rch.rightchild
print(rch_rch.feature,"rightchild of",rch.feature)
rch_lch=rch.leftchild
print(rch_lch.feature,"leftchild of",rch.feature)
print("################")
root=BFIG(tdata,A)
print(root.feature,"root")
lch=root.leftchild
print(lch.feature,"root leftchild")
rch=root.rightchild
print(rch.feature,"root rightchild")
lch_lch=lch.leftchild
print(lch_lch.feature,"leftchild of",lch.feature)
lch_rch=lch.rightchild
print(lch_rch.feature,"rightchild of",lch.feature)
rch_rch=rch.rightchild
print(rch_rch.feature,"rightchild of",rch.feature)
rch_lch=rch.leftchild
print(rch_lch.feature,"leftchild of",rch.feature)
print("######################")
root=BFGini(tdata,A)
print(root.feature,"root")
lch=root.leftchild
print(lch.feature,"root leftchild")
rch=root.rightchild
print(rch.feature,"root rightchild")
lch_lch=lch.leftchild
print(lch_lch.feature,"leftchild of",lch.feature)
lch_rch=lch.rightchild
print(lch_rch.feature,"rightchild of",lch.feature)
rch_rch=rch.rightchild
print(rch_rch.feature,"rightchild of",rch.feature)
rch_lch=rch.leftchild
print(rch_lch.feature,"leftchild of",rch.feature)        
        
