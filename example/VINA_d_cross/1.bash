#! /bin/bash
export PATH="/share/home/zhanghaiping/anaconda2/bin:$PATH"
cd receptor
export pdbtool=/share/home/zhanghaiping/program/pdbTools_0.2.1
for f in *.pdb
  do
a=`python $pdbtool/pdb_centermass.py $f`

echo -e "$a" >>../aa.txt 

 
done
