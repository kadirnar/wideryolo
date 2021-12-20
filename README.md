<div align="center">
<h1>
  WIDER-YOLO : Yüz Tespit Uygulaması Yap
</h1>

<h4>
<img height="500" src="https://raw.githubusercontent.com/kadirnar/wideryolo/main/doc/images/yolov5n_sahi.png"/>
</h4> 
  
</div>

 ## Wider-Yolo Kütüphanesinin Kullanımı
 
#### 1. Wider Face Veri Setini İndir

- [Train Dataset](https://drive.google.com/u/0/uc?export=download&confirm=e3va&id=15hGDLhsx8bLgLcIRD5DhYt5iBxnjNF1M)
- [Val Dataset](https://drive.google.com/u/0/uc?export=download&confirm=FKYL&id=1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q)
- [Test Dataset](https://drive.google.com/u/0/uc?export=download&confirm=lfFX&id=1HIfDbVEWKmsYKJZm4lchTBDLW5N7dY5T)


Not: İndirilen veri setini ismini değiştirmeden wider_data klasörün içine atın.

#### 2. Dosyaları Düzeni:
```
datasets/ 
      wider_face_split/  
          - wider_face_train_bbx_gt.txt
          - wider_face_val_bbx_gt.txt
         
      WIDER_train/
         - images

      WIDER_train_annotations 

      WIDER_val
         - images

      WIDER_val_annotations
```      

Not: WIDER_train_annotations ve WIDER_val_annotations klasörleri oluşturmanıza gerek yoktur.

#### 3. Wider Veri Setini Voc Xml Formatına Çevir
```
python ./wider_to_xml.py -ap ./wider_data/wider_face_split/wider_face_train_bbx_gt.txt -tp ./wider_data/WIDER_train_annotations/ -ip ./wider_data/WIDER_train/images/
python ./wider_to_xml.py -ap ./wider_data/wider_face_split/wider_face_val_bbx_gt.txt -tp ./wider_data/WIDER_val_annotations/ -ip ./wider_data/WIDER_val/images/
```
#### 4. Voc Xml Veri Setini Yolo Formatına Çevir
```
python ./xml_to_yolo --path ./wider_data/WIDER_train_annotations/
python ./xml_to_yolo --path ./wider_data/WIDER_val_annotations/
```
#### 5. Yolo Modelini Eğit
```
!yolov5 train --data data.yaml --weights 'yolov5n.pt' --batch-size 16 --epochs 100 --imgs 512
```
#### 6. Yolo Modelini Test Et

Tek resim test etmek için:
```
!yolov5 detect --weights wider-yolo.pth --source  file.jpg  
```
Tüm resim dosyasını test etmek için
```
!yolov5 detect --weights wider-yolo.pth --source  path/*.jpg 
```
Not: Yeterli Gpu kaynağına sahip olamadığım için wider seti için düşük parametre değerleri verdim. Parametre Değerleri: 
```
batch-size: 256, epochs: 5, imgs 320
```
<img height="500" src="https://raw.githubusercontent.com/kadirnar/wideryolo/main/doc/images/yolov5sn.jpg"/>
 
 
 #### 6. Yolov5 + Sahi Algoritmasını Test Et
```
from sahi.model import Yolov5DetectionModel
from sahi.utils.cv import read_image
from sahi.predict import get_prediction, get_sliced_prediction, predict
from IPython.display import Image

detection_model = Yolov5DetectionModel(
   model_path="last.pt",
   confidence_threshold=0.3,
   device="cpu",
)

result = get_sliced_prediction(
    "test_data/2.jpg",
    detection_model,
    slice_height = 256,
    slice_width = 256,
    overlap_height_ratio = 0.8,
    overlap_width_ratio = 0.8
)
result.export_visuals(export_dir="demo_data/")
Image("demo_data/prediction_visual.png")
```
<img height="500" src="https://raw.githubusercontent.com/kadirnar/wideryolo/main/doc/images/yolov5n_sahi.png"/>

Sahi Algoritması ile ilgili Örnek Proje:
- [yolov5-pytorch-sahi](https://github.com/kadirnar/yolov5-pytorch-sahi)


Referanslar:
- [Fatih Cagatay Akyon](https://github.com/fcakyon)
- [Alexis Kofman](https://github.com/akofman/wider-face-pascal-voc-annotations)<br/>
- [yolov5-pip](https://github.com/fcakyon/yolov5-pip)
- [Sahi](https://github.com/obss/sahi)<br/>
