from sahi.model import Yolov5DetectionModel
from sahi.predict import get_sliced_prediction
detection_model = Yolov5DetectionModel(
   model_path="last.pt",
   confidence_threshold=0.3,
   device="cpu",)
result = get_sliced_prediction(
    "test_data/2.jpg",
    detection_model,
    slice_height = 256,
    slice_width = 256,
    overlap_height_ratio = 0.8,
    overlap_width_ratio = 0.8)
result.export_visuals(export_dir="demo_data/")
