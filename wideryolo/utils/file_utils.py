import glob
import os
import shutil
from zipfile import ZipFile

import gdown


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


def download(url: str, save_path: str):
    gdown.download(url, save_path, quiet=True)
    zip_export(save_path)


def face_split_download():
    face_split_url = "https://github.com/kadirnar/wideryolo/releases/download/widerface/wider_face_split.zip"
    face_split_url_download = "wider_face_split.zip"
    download(face_split_url, face_split_url_download)


def train_download():
    train_url = "https://github.com/kadirnar/wideryolo/releases/download/widerface/WIDER_train.zip"
    train_url_download = "WIDER_train.zip"
    download(train_url, train_url_download)


def val_download():
    val_url = "https://github.com/kadirnar/wideryolo/releases/download/widerface/WIDER_val.zip"
    val_url_download = "WIDER_val.zip"
    download(val_url, val_url_download)


def test_download():
    test_url = "https://drive.google.com/u/0/uc?export=download&confirm=aptm&id=1HIfDbVEWKmsYKJZm4lchTBDLW5N7dY5T"
    test_url_download = "WIDER_test.zip"
    download(test_url, test_url_download)


def download_run(data):
    face_split_download()
    val_download()
    wider_create_dir(data + "./WIDER_train_annotations", data + "./WIDER_val_annotations")
    shutil.move("wider_face_split", data)
