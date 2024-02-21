from ultralytics import YOLO
import torch

#SETUP GPU
device = "0" if torch.cuda.is_available() else "cpu"
if device == "0":
    torch.cuda.set_device(0)

###

print("Device:", device)
model =  YOLO("yolov8n.pt")
print("Before:", model.device.type)
results = model("sample.jpg")
print("After: ", model.device.type)