1. the native complexes in the main folder ????/ are known protein-ligand complex, which will be used as positive

2, the cross docked structure(collect2_s_cross) are used as negative. And the docking is taken at VINA_d_cross folder.

tt python2_L_col_1000_0.4.py   run_convert_mol2_all_1000_0.4.bash   run_convert_mol2_all_neg1000_0.4_cross.bash  files were used to generate the input matrix files(neg_cross  and positive_test)

4. deep_learn_rob_residual_zhpxxx_n_test_0.2.py  is the file used to load the model and data for final prediction.
