
#tem=$1'_ww.pdb'
#grep "^ATOM\|^TER\|^END" $1'_w.pdb' >$1'_ww.pdb'
#sed -i "s/XXXXX/$tem/g" test1.leapin
#tleap -f  test1.leapin

#sed -i "s/HID/HIS/g"  protein.pdb

#sed -i "s/HIE/HIS/g"  protein.pdb


#pdb2gmx  -f  protein.pdb  -o $1'_processed.pdb' -water spce -ignh -ff amber99sb  -merge all


python  ../../python2_L_col_1000_0.4.py   $1'_processed.pdb'
