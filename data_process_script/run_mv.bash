
cat  out.txt | while read line
do
IFS=' ' read -r -a array <<<  $line
echo ${array[0]}
mv  ${array[0]}  moveout/


done
