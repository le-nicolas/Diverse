import io
import zipfile
import pickle
import numpy as np
from PIL import Image, ImageOps
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

# Load the model
with open('mnist_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post("/predict-images/")
async def predict_images(file: UploadFile = File(...)):
    contents = await file.read()
    with zipfile.ZipFile(io.BytesIO(contents)) as zip_ref:
        predictions = {}
        for zip_info in zip_ref.infolist():
            if zip_info.filename.endswith('.png') or zip_info.filename.endswith('.jpg') or zip_info.filename.endswith('.jpeg'):
                with zip_ref.open(zip_info.filename) as image_file:
                    pil_image = Image.open(image_file).convert('L')
                    pil_image = ImageOps.invert(pil_image)
                    pil_image = pil_image.resize((28, 28), Image.ANTIALIAS)
                    img_array = np.array(pil_image).reshape(1, -1)
                    prediction = model.predict(img_array)
                    predictions[zip_info.filename] = int(prediction[0])
    return {"predictions": predictions}
