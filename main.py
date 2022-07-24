import shutil

from wideryolo.utils.data_utils import train_file, val_file, yolo_image_file, yolo_label_file


def file_path():
    train_path = train_file()
    val_path = val_file()
    image_path = yolo_image_file()
    label_path = yolo_label_file()
    shutil.rmtree("./wider_data/wider_face_split/")


file_path()
