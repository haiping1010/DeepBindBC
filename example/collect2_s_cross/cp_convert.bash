cd ../../
for folder in  VINA_d*
do
for name in  $folder/Docking/*
do
cp -r  $name/*.pdbqt   $folder/collect2_s/


done

done


