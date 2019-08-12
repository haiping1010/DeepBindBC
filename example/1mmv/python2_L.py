import sys
import numpy as np
from sklearn.cluster import KMeans
import numpy as np
from sklearn.cluster import KMeans
def one_hot(i):
    m = np.zeros(20, 'uint8')
    m[i] = 1
    return m

def one_hot_atom(i):
    m = np.zeros(83, 'uint8')
    m[i] = 1
    return m

def MapResToOnehot(residue1,atom2):
   code={}
   codelig={}
   seq=("ALA","ARG", "ASN", "ASP", "CYS", "GLU", "GLN", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL")
##   seqatom=("c","c1","c2","c3","ca"," n","n1","n2","n3","n4","na","nh","no","f","cl","br","i","h1","h2","h3","h4","h5","n","nb","nc","nd","sx","sy","o","oh","os","s2","sh","ss","s4","s6","hc","ha","hn","ho","hs","hp","p2","p3","p4","p5","cc","cd","ce","cf","cp","cq","cu","cv","cx","cy","pb","pc","pd","pe","pf","px","py")
   seqatom=("c","cs","c1","c2","c3","ca","cp","cq","cc","cd","ce","cf","cg","ch","cx","cy","cu","cv","cz","h1","h2","h3","h4","h5","ha","hc","hn","ho","hp","hs","hw","hx","f","cl","br","i","n","n1","n2","n3","n4","na","nb","nc","nd","ne","nf","nh","no","ns","nt","nx","ny","nz","n+","nu","nv","n7","n8","n9","o","oh","os","ow","p2","p3","p4","p5","pb","pc","pd","pe","pf","px","py","s","s2","s4","s6","sh","ss","sx","sy")
   

   index=0
   for name in seq:
              #print (name)
              code[name]=one_hot(index)
              index=index+1
   index=0
   for name in seqatom:
              #print (name)
              codelig[name]=one_hot_atom(index)
              index=index+1         
            
   return (np.concatenate((code[residue1],codelig[atom2])))
#print (MapResToOnehot("ARG","VAL"))

#-------------------------------------------------


visited = {}
Pposition={}
Lposition={}
ResinameP={}
ResinameL={}
Interface=[]
residuePair=[]
if len(sys.argv) <1 :
   print("python python2_L.py xxx")
filebase=sys.argv[1]
##filebase=file.replace(".pdb","")

#filebase="1flr"
#print(file)
print(filebase)
for line in open(filebase+'_pocket.pdb'):
    tem_B=' '
    if len(line)>16:
       tem_B=line[16]
       line=line[:16]+' '+line[17:]
    #print(line)
    list = line.split()
    id = list[0]
    if id == 'ATOM' and tem_B !='B':
        type = list[2]
        #if type == 'CA' and list[3]!= 'UNK':
        if  list[3]!= 'UNK':
            residue = list[3]
            type_of_chain = line[21:22]
            tem1=line[22:26].replace("A", "")
            tem2=tem1.replace("B", "")
            tem2=tem2.replace("C", "")

            #tem2=filter(str.isdigit, list[5])
            atom_count = tem2+line[21:22]
            list[6]=line[30:38]
            list[7]=line[38:46]
            list[8]=line[46:54]
            position = list[6:9]
            Pposition[atom_count]=position
            ResinameP[atom_count]=residue
index_nn=0            
for line in open(filebase+'_ligand_n.mol2'):
    tem_B=' '
    line=line.strip()
    #print(line)
    if line == "@<TRIPOS>ATOM":
        index_nn=1
        #print(line)
    if line == "@<TRIPOS>BOND":
        index_nn=0 
    if index_nn==1 and line != "@<TRIPOS>ATOM":
            list = line.split()
            #tem2=filter(str.isdigit, list[5])
            atom_count = list[0]+list[5]
            position = list[2:5]
            Lposition[atom_count]=position
            ResinameL[atom_count]=list[5]
			
			
#-------------------------------------------------

for key1, value1 in Pposition.items():
   #print ( key1)
   for key2, value2 in Lposition.items():
           #print (ResinameE[key], 'corresponds to', value)
           ##distance=pow(value1[0]-value2[0])
            #print (value2)
            a = np.array(value1)
            a1 = a.astype(np.float)
            b = np.array(value2)
            b1 = b.astype(np.float)
            xx=np.subtract(a1,b1) 
            tem=np.square(xx)
            tem1=np.sum(tem)
            out=np.sqrt(tem1)
            #print (tem1)
            if out<6 :
                #print (ResinameHL[key1],ResinameHL[key2])
                #print (a,b,out)
                fo = open("ceshi.txt", "wb")
                fo.write(a)
                fo.write(b)
                #print (a1)              
                residuePair.append([ResinameP[key1],ResinameL[key2]])
                Interface.append(a1)
                #print (a1)  
#---------------------------------------------------------------------                
#print (antiface)              
kmeans = KMeans(n_clusters=5, random_state=0).fit_predict(Interface)
#print (kmeans)
indexx=0
kmeans1=kmeans.tolist()
foo = open(filebase + "_learn.txt", "w")

index_n=0
for i in range(5):
   #print(kmeans)
   g=np.argwhere(kmeans==i)
   ##g=kmeans.where(q==i) 
   ##print (g)
   g1=g.reshape(-1)

   for groupid in g1:
      index_n=index_n+1
      if index_n<=300:
           print(residuePair[groupid][0],residuePair[groupid][1])
		   
		   
#------------------------------------------------------
#print (antiface)              
kmeans = KMeans(n_clusters=5, random_state=0).fit_predict(Interface)
#print (kmeans)
indexx=0
kmeans1=kmeans.tolist()
foo = open(filebase + "_learn.txt", "w")

index_n=0
for i in range(5):
   #print(kmeans)
   g=np.argwhere(kmeans==i)
   ##g=kmeans.where(q==i) 
   ##print (g)
   g1=g.reshape(-1)

   for groupid in g1:
      index_n=index_n+1
      if index_n<=300:
           writout=MapResToOnehot(residuePair[groupid][0],residuePair[groupid][1])
           # foo = open("3HFM_learn.txt", "a")
           arr_tem=np.array_str(writout)
           for code in  writout:
              #print (str(code))
              foo.write(str(code))
              # print(code)
              #foo.write(code)
           foo.write('\n')
while index_n<300:
         index_n=index_n+1
         foo.write("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n")


