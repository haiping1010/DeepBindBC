cat tem.txt | while read lowLINE
do
LINE=${lowLINE^^}
IFS='  ' read -r -a array <<< "$lowLINE"

#cp -r ../${array[0]}/${array[0]}'_protein.pdb'  receptor
#cp -r ../${array[0]}/${array[0]}'_pocket.pdb'  receptor

cp -r ../${array[1]}/${array[1]}'_ligand.mol2'  ligands
echo $lowLINE


done
