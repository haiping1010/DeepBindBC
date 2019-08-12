import sys
import numpy as np
from sklearn.cluster import KMeans
import numpy as np
from sklearn.cluster import KMeans
import glob
def one_hot(i):
    m = np.zeros(41, 'uint8')
    m[i] = 1
    return m

def one_hot_atom(i):
    m = np.zeros(84, 'uint8')
    m[i] = 1
    return m

def MapResToOnehot(atom1,atom2):
   code={}
   codelig={}
   seq=('C','CA','CB','CC','CK','CM','CN','CQ','CR','CT','CV','CW','C*','F','H','HC','H1','H2','H3','HA','H4','H5','HO','HS','HW','HP','N','NA','NB','NC','N2','N3','N*','O','OW','OH','OS','O2','P','S','SH')
##   seqatom=("c","c1","c2","c3","ca"," n","n1","n2","n3","n4","na","nh","no","f","cl","br","i","h1","h2","h3","h4","h5","n","nb","nc","nd","sx","sy","o","oh","os","s2","sh","ss","s4","s6","hc","ha","hn","ho","hs","hp","p2","p3","p4","p5","cc","cd","ce","cf","cp","cq","cu","cv","cx","cy","pb","pc","pd","pe","pf","px","py")
   seqatom=("c","cs","c1","c2","c3","ca","cp","cq","cc","cd","ce","cf","cg","ch","cx","cy","cu","cv","cz","h1","h2","h3","h4","h5","ha","hc","hn","ho","hp","hs","hw","hx","f","cl","br","i","n","n1","n2","n3","n4","na","nb","nc","nd","ne","nf","nh","no","ns","nt","nx","ny","nz","n+","nu","nv","n7","n8","n9","o","oh","os","ow","p2","p3","p4","p5","pb","pc","pd","pe","pf","px","py","s","s2","s4","s6","sh","ss","sx","sy","B")
   

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
   ######
   ##codelig['DU']="00000000000000000000000000000000000000000000000000000000000000000000000000000000000"       
   return (np.concatenate((code[atom1],codelig[atom2])))
#print (MapResToOnehot("ARG","VAL"))

#-------------------------------------------------
#################read  topology
f=open('topol.top', 'r')
hash={}
lines=f.readlines()
index=0
for line in lines:
    if line.startswith('[ atoms ]') :
         #print (line.strip()) 
          index=1

    if line.startswith('[ bonds ]') :
          index=0
    if index==1 and line[0] != '[' and  line.find('[')<0 and line[0] != ';'  and line != '\n':
          arr=line.split()
          atom_name=arr[4]
          ############atom name in the pdb and toplogy has slightly difference       
          if len(arr[4])==4 and atom_name[0]=='H':
              arr[4] = atom_name[-1] + atom_name[0:3]
              print arr[4],atom_name[-1:]
