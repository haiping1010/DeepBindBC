import shutil, random, os
dirpath='/share/home/zhanghaiping/program/mol2vec/examples/extra_test/astex_diverse_set/VINA_d_cross/receptor'
#filenames = random.sample(os.listdir(dirpath), 4000)
import glob
os.chdir(dirpath)
aa=glob.glob("????_w.pdb")
##filenames = random.sample(os.listdir(dirpath), 3)
#filenames = random.sample(aa, 3)
os.chdir('/share/home/zhanghaiping/program/mol2vec/examples/extra_test/astex_diverse_set')
fw=open("tem.txt", "w")
print (fw.name)
####destDirectory='/share/home/zhanghaiping/work/Zdock/docking_complex/random1'
for pname in aa:
  filenames = random.sample(aa, 1)
  for lname in filenames:
      while pname == lname:
          tem=random.sample(aa, 1)
          lname=tem[0]      
      fw.write(pname[0:4]+"  "+ lname[0:4]+"\n")
#      fw.write(str(pname))
#      fw.write("1")
   #srcpath = os.path.join(dirpath, fname)
   #disfile=os.path.join(destDirectory, fname)
   #shutil.copyfile(srcpath, disfile)

fw.close()
