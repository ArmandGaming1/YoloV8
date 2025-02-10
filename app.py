from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")

# Train the model
train_results = model.train(
    data="config.yaml",  # path to dataset YAML
    epochs=25,  # number of training epochs
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("images/sample.jpg")
results[0].show()
print(results[0].boxes)

# Export the model to ONNX format
path = model.export(format="onnx")  # return path to exported model