from wideryolo.file_utils.file_utils import train_path
import shutil


def train_file():
    old_train_dir = './wider_data/WIDER_train/images/'
    new_train_dir = './wider_data/WIDER_train/'
    train_path(old_train_dir, new_train_dir)
    shutil.rmtree(old_train_dir)


def val_file():
    old_val_dir = './wider_data/WIDER_val/images/'
    new_val_dir = './wider_data/WIDER_val/'
    train_path(old_val_dir, new_val_dir)
    shutil.rmtree(old_val_dir)


def yolo_image_file():
    create_dir('./wider_data/images/')
    shutil.move('./wider_data/WIDER_train/', './wider_data/images/')
    shutil.move('./wider_data/WIDER_val/', './wider_data/images/')


def yolo_label_file():
    create_dir('./wider_data/labels/')
    shutil.move('./wider_data/WIDER_train_annotations/', './wider_data/labels/')
    shutil.move('./wider_data/WIDER_val_annotations/', './wider_data/labels/')
