cd Docking

for d in `/bin/ls`
    do
    egrep "^   1" $d/*.txt | awk  -v n=$d 'BEGIN {N=n} { print N"  "$2" "}' > $d/$d.energies
    done
cd ..
touch all_energies.list
cd Docking
for d in `/bin/ls`
       do
    head -1 $d/$d.energies >> ../all_energies.list
   done
cd ..
sort -k2n all_energies.list > all_energies.sort
