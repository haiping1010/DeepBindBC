mkdir -p problem

#wc  *aa2000.txt  > xxx.txt

wc  *aa1000_0.4.txt  > xxx.txt

##wc  *aa1000_noH0.4.txt  > xxx.txt
grep  -v "^    1000"  xxx.txt >xxx_sort.txt
cat  xxx_sort.txt | while read line
do
IFS=' ' read -r -a array <<<  $line
echo ${array[3]}
mv  ${array[3]}  problem/


done
