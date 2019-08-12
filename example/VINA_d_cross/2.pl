#system("bash 1.bash");
system("grep '_poc' aa.txt >aaa.txt");
open(FN, "<aaa.txt");
open(FD,"<tem1.txt");
@arrpair=<FD>;
chomp(@arrpair);
#for linename in @arrpair{
#@arrname=split(" ",$linename);
#$receptorToligand{$arrname[0]} = $arrname[1]
#}


@a=<FN>;
chomp(@a);

foreach $linename ( @a){
@arrname=split(" ",$linename);

#print $arrname[0]."\n";
$pdbcode=substr($arrname[0],0,4);
$receptocord_x{$pdbcode} = $arrname[1];
$receptocord_y{$pdbcode} = $arrname[2];
$receptocord_z{$pdbcode} = $arrname[3];
}

#system("bash run.bash");
#system("rm -rf Docking");
#system("mkdir Docking");



foreach $s (@arrpair){
@vv=split(/ +/, $s);
#print $s;
#print $vv[0]."\n";
#print $vv[1]."\n";
#print  $receptocord_z{$vv[0]}."\n";
#print @vv[3];

#$xxx=@vv[0];
##$base =~ s/\.pdb//g;
#$name=@vv[0]."qt";
#$xxx=~s/\.pdb//;

system("mkdir Docking/".$vv[0]."_".$vv[1]);
system("vina    --num_modes 3   --config conf.txt --ligand ligands/".$vv[1]."_ligand_n.pdbqt --receptor receptor/".$vv[0]."_ww.pdbqt --center_x ".$receptocord_x{$vv[0]}." --center_y ".$receptocord_y{$vv[0]}." --center_z ".$receptocord_z{$vv[0]}." --out Docking/".$vv[0]."_".$vv[1]."/".$vv[0]."_".$vv[1]."out.pdbqt  --log Docking/".$vv[0]."_".$vv[1]."/".$vv[0]."_".$vv[1]."log.txt\n")

}
close(FN);

