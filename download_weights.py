import gdown

url = "https://drive.google.com/uc?id=1f2GOZkwmFkZ-vsIiP40UKrcRFW-vGo0d"
output = "yolov3.weights"

print("Downloading yolov3.weights from Google Drive...")
gdown.download(url, output, quiet=False)
