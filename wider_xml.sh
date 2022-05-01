python3 wider_to_xml.py -ap ./wider_data/wider_face_split/wider_face_train_bbx_gt.txt -tp ./wider_data/WIDER_train_annotations/ -ip ./wider_data/WIDER_train/images/
python3 wider_to_xml.py -ap ./wider_data/wider_face_split/wider_face_val_bbx_gt.txt -tp ./wider_data/WIDER_val_annotations/ -ip ./wider_data/WIDER_val/images/
python3 ./xml_to_yolo.py --path ./wider_data/WIDER_train_annotations/
python3 ./xml_to_yolo.py --path ./wider_data/WIDER_val_annotations/