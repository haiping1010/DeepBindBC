#! /bin/bash
export adtpy=/share/home/zhanghaiping/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24
export path=/share/home/zhanghaiping/MGLTools-1.5.6/bin
cd receptor

for f in *.pdb
do
grep -v "HETATM" $f  > $f"_tem"
mv $f"_tem"  $f
$path/pythonsh $adtpy/prepare_receptor4.py -r $f -o "$f"qt 

done

cd ..
cd  ligands

for i in *.mol2
 do
base=${i%.mol2}
$path/pythonsh $adtpy/prepare_ligand4.py -l $i -o  $base'.pdbqt'

done
cd ..

