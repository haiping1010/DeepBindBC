for name in *.pdb
   do
##cd $name
base=${name%out.pdb}


babel -ipdb  $name  -osdf  $name".sdf" -h
antechamber -i  $name".sdf"  -fi sdf -o $name'_ligand_n.mol2' -fo mol2   -pf y

####babel -ipdb    -osdf 2nqg_3l4uout.sdf -h

## $name'ligand_n.mol2'  $name'_ligand_n.mol2'

##cd ..
done

