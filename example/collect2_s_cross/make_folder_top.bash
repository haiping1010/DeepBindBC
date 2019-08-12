
cat summary.txt| while read LINE


do
first=${LINE:0:12}
second=${LINE:15:1}


base=${LINE:0:4}

mkdir $first''$second
cp -r $base'_'$base'out_ligand_n'$second'.mol2'  $first''$second

cp -r  /share/home/zhanghaiping/program/mol2vec/examples/extra_test/astex_diverse_set/$base/$base'_w.pdb'  $first''$second



done



