import shutil
from file_utils import zip_export, wider_create_dir
import gdown


def download(url: str, save_path: str):
    gdown.download(url, save_path, quiet=True)
    zip_export(save_path)


def face_split_download():
    face_split_url = 'http://shuoyang1213.me/WIDERFACE/support/bbx_annotation/wider_face_split.zip'
    face_split_url_download = 'wider_face_split.zip'
    download(face_split_url, face_split_url_download)


def train_download():
    train_url = 'https://drive.google.com/uc?id/15hGDLhsx8bLgLcIRD5DhYt5iBxnjNF1M'
    train_url_download = 'WIDER_train.zip'
    download(train_url, train_url_download)


def val_download():
    val_url = 'https://drive.google.com/u/0/uc?export=download&confirm=ODkl&id=1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q'
    val_url_download = 'WIDER_val.zip'
    download(val_url, val_url_download)


def test_download():
    test_url = 'https://drive.google.com/u/0/uc?export=download&confirm=aptm&id=1HIfDbVEWKmsYKJZm4lchTBDLW5N7dY5T'
    test_url_download = 'WIDER_test.zip'
    download(test_url, test_url_download)


def download_run(data):
    face_split_download()
    # Yakında bu özellik aktif hale getirilecek.
    """ 
    train_download()
    val_download()
    test_download()
    """
    wider_create_dir(data + './WIDER_train_annotations', data + './WIDER_val_annotations')
    shutil.move("wider_face_split", data)
