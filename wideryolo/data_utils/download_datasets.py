import shutil
from file_utils import zip_export, wider_create_dir
import gdown


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
    """
    Model map hesabı yaparken bu özellik kulanılacak.
    """
    test_url = "https://drive.google.com/u/0/uc?export=download&confirm=aptm&id=1HIfDbVEWKmsYKJZm4lchTBDLW5N7dY5T"
    test_url_download = "WIDER_test.zip"
    download(test_url, test_url_download)


def download_run(data):
    face_split_download()
    # train_download()
    val_download()
    # test_download() bu özellik daha sonra aktif edilecektir.
    wider_create_dir(
        data + "./WIDER_train_annotations", data + "./WIDER_val_annotations"
    )
    shutil.move("wider_face_split", data)
