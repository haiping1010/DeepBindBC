#for name in ????
for name in   ????
   do
cd $name

babel  -imol ligand.mol  -omol2  ligand.mol2
antechamber -i  'ligand.mol2'  -fi mol2  -o $name'_ligand_n.mol2' -fo mol2   -pf y

cp -r ../test1.leapin    .

bash ../part1_1000_0.4.bash $name 

##> log.txt &

##bash ../part1.bash $name

sleep 0.5s
##################pdb2gmx  -f $name'_protein.pdb'  -o $name'_processed.pdb' -water spce -ignh -ff amber99sb

###############python  ../python2_L_col.py   $name'_processed.pdb' 

## $name'ligand_n.mol2'  $name'_ligand_n.mol2'

cd ..
done

