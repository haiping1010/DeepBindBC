
for name in *2.mol2
do
foldbase=${name:0:9}
base=${name:0:4}
echo $foldbase
mkdir $foldbase'2'
cp -r /share/home/zhanghaiping/work/refined_set/VINA_d/receptor/$base*.pdb  $foldbase'2'

cp -r $name  $foldbase'2'


done


