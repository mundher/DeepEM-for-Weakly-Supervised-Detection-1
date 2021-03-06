config = {'train_data_path':['../../luna16/subset9/',
                             '../../luna16/subset1/',
                             '../../luna16/subset2/',
                             '../../luna16/subset0/',
                             '../../luna16/subset3/',
                             '../../luna16/subset5/',
                             '../../luna16/subset4/',
                             '../../luna16/subset7/',
                             '../../luna16/subset8/'],
          'val_data_path':['../../luna16/subset6/'], 
          'test_data_path':['../../luna16/subset6/'], 
          
          'train_preprocess_result_path':'../../luna16/preprocess/',
          'val_preprocess_result_path':'../../luna16/preprocess/',  
          'test_preprocess_result_path':'../../luna16/preprocess/',
          
          'train_annos_path':'../../luna16/CSVFILES/newannotations.csv',
          'val_annos_path':'../../luna16/CSVFILES/newannotations.csv',
          'test_annos_path':'../../luna16/CSVFILES/newannotations.csv',

          'weaktrain_data_path':'../../NLST/preprocessnp/',
          'weaktrain_annos_path':'../../NLST/calibweaklabelallsmall.csv',

          'black_list':[],
          
          'preprocessing_backend':'python',
         } 