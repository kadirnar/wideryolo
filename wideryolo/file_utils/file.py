from zipfile import ZipFile
import shutil
import glob
import os


def create_dir(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def zip_export(save_path):
    with ZipFile(save_path, "r") as zip:
        zip.extractall()
    os.remove(save_path)


def wider_create_dir(train_annotations, val_annotations):
    root_path = os.getcwd()
    folders = [train_annotations, val_annotations]
    for folder in folders:
        os.makedirs(os.path.join(root_path, folder))


def file_move(root_dir, move_dir):
    for file in glob.glob(root_dir + "/*"):
        for main_file in glob.glob(file + "/*"):
            print(main_file)
            shutil.move(main_file, move_dir)


def train_path(old_train_dir, new_train_dir):
    create_dir(new_train_dir)
    file_move(old_train_dir, new_train_dir)


def file_move(file_path, describe_path):
    for file in glob.glob(file_path + "*"):
        for i in glob.glob(file + "/*"):
            shutil.move(i, describe_path)
        os.rmdir(file)
