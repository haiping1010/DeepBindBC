import shutil, random, os
dirpath='/share/home/zhanghaiping/work2/extra_test/astex_diverse_set'
#filenames = random.sample(os.listdir(dirpath), 4000)
import glob
os.chdir(dirpath)
aa=glob.glob("????")
##filenames = random.sample(os.listdir(dirpath), 3)
#filenames = random.sample(aa, 3)
os.chdir(dirpath+'/VINA_d_cross')
fw=open("tem.txt", "w")
print (fw.name)
for pname in aa:
  filenames = random.sample(aa, 1)
  for lname in filenames:
      while pname == lname:
          tem=random.sample(aa, 1)
          lname=tem[0]      
      fw.write(pname+"  "+ lname+"\n")
#      fw.write(str(pname))
#      fw.write("1")
   #srcpath = os.path.join(dirpath, fname)
   #disfile=os.path.join(destDirectory, fname)
   #shutil.copyfile(srcpath, disfile)

fw.close()
