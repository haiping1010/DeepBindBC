for name in    *.pdbqt
   do
##cd $name
export PYTHONPATH=/share/home/zhanghaiping/MGLTools-1.5.6/MGLToolsPckgs
export adtpy=/share/home/zhanghaiping/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24
export path=/share/home/zhanghaiping/MGLTools-1.5.6/bin

base=${name%.pdbqt}

echo $base
echo $name

###python  $adtpy/pdbqt_to_pdb.py  -f  $name  -o  $base'.pdb'

babel -ipdbqt  $name -osdf  $base'.sdf' -h -m
#obabel   $name -o   $base'.sdf' -h
sed -i "s/ Ca / C  /g"  $base?'.sdf'
sed -i "s/ Hg / H  /g"  $base?'.sdf'
sed -i "s/ Cd / C  /g"  $base?'.sdf'
#####antechamber -i  $base".sdf"  -fi sdf -o $base'_ligand_n.mol2' -fo mol2   -pf y

for i in {1..3}
do
antechamber -i  $base""$i".sdf"  -fi sdf -o $base'_ligand_n'$i'.mol2' -fo mol2   -pf y
done



###antechamber -i  $base"2.sdf"  -fi sdf -o $base'_ligand_n2.mol2' -fo mol2   -pf y
###antechamber -i  $base"3.sdf"  -fi sdf -o $base'_ligand_n3.mol2' -fo mol2   -pf y
done

