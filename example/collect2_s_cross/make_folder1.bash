for name in ????_????out*1.mol2
do
foldbase=${name:0:9}
base=${name:0:4}
echo $foldbase
mkdir $foldbase'1'
cp -r ../$base/$base*.pdb  $foldbase'1'
cp -r ../$base/topol.top  $foldbase'1'
cp -r $name  $foldbase'1'


done



