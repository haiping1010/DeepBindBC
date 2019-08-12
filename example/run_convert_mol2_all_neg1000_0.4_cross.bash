#for name in ????
cd collect2_s_cross
for name in ????_?????
   do
cd $name
##antechamber -i  $name'_ligand.sdf' -fi sdf -o $name'_ligand_n.mol2' -fo mol2   -pf y

base=${name:0:4}
#cp -r ../../test1.leapin    .

##bash ../../part2.bash $name

###bash ../../part2_1000_noh.bash $name

##bash ../../part2_1000_0.4.bash $base

nohup bash ../../part2_1000_0.4.bash $base> log.txt &


#####bash ../../part2_1000_0.4.bash $base
sleep 0.5s
###########pdb2gmx  -f $base'_protein.pdb'  -o $base'_processed.pdb' -water spce -ignh -ff amber99sb
################
#############python  ../../python2_L_col.py   $base'_processed.pdb' 

## $name'ligand_n.mol2'  $name'_ligand_n.mol2'

cd ..
done

