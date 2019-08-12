for name in *3.mol2
do
foldbase=${name:0:9}
base=${name:0:4}
echo $foldbase
mkdir $foldbase'3'
cp -r /share/home/zhanghaiping/work/refined_set/VINA_d/receptor/$base*.pdb  $foldbase'3'

cp -r $name  $foldbase'3'


done


