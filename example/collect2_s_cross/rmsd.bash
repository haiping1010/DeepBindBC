for name in  *.pdbqt
do
base=${name%.pdbqt}
babel -ipdbqt $name -opdb  $base'.pdb'


done

rm summary.txt
for name in *out.pdb
do
base=${name:0:4}
echo -e "0\n0\n" | g_rms -s $base'_ligand_n.pdb' -f $base'_'$base'out.pdb'  -o $base'.xvg'

grep -v "@\|#"  $base'.xvg' > $base'_n.xvg'

echo -e  $base'_'$base'out'"\c" >>summary.txt
sort -nk2   $base'_n.xvg' | head -n 1 >> summary.txt

done
