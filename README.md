# NER_Data_Preparation
Data preparation for NER model training

Please follow below instructions to prepare data for NER model training:

1. Once we receive the annotations data for an insurer (put respective insurer data folders inside __‘bucket’__ & __‘out’__ directory)
2. Place __combine_annotations_files.py__ file inside __‘out’__ folder and change the directory name inside the file.Now, open a terminal and run this file inside out folder to combine different files __(train_page1.txt, train_box_page1.txt, train_image_page1.txt)__ for each annotated pages into three files namely __(train.txt, train_box.txt, train_image.txt)__.
3. After that run the __train_test_split_script.py__ file to split data into train-test split.Inside the file you can change the number of examples you want in test files.This will create total 6 files __(train.txt, train_image.txt, train_box.txt, test.txt, text_image.txt, test_box.txt)__
4. Now, use __generate_labels.py__ file to generate labels or labels.txt file.Please change configuration according to use case (Motor/Health).

Note: 
If you want to combine multiple files __(train.txt, train_box.txt, train_image.txt)__ for different insurers, just place the respective annotated folder inside bucket & out and repeat the steps from 1-2.
