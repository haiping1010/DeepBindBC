import os
import os
import shutil
if (len(os.sys.argv)<2):

    print ("usage: python compare.py file1 file2")


nf=open(os.sys.argv[1], 'r')
old=[]
oldvalue=[]
oldline=[]

#print (os.sys.argv[1])
newlines=nf.readlines()

f=open(os.sys.argv[2], 'r')

lines=f.readlines()
for newname in newlines:
    old=[]
    oldvalue=[]
    oldline=[]
    #print newname
    for name in lines:
         index=0         
         # print name
         #print newname[0:4].upper(),name[0:4].upper()

         if newname[0:4] == name[0:4]:
                  print (name[0:4])
