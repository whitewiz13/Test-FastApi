from fastapi import FastAPI, File, UploadFile
from classifier import Classifier

image_classify = Classifier()

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        with open("temp_file.jpg", "wb") as temp_file:
            temp_file.write(file.file.read())

        # Use the classifier to classify the uploaded file
        result = image_classify.classify_img("temp_file.jpg")

        # Return the result
        return {"filename": file.filename, "classification_result": result,"isAccepted":result['temp_file.jpg']['safe']*100 >= 89}
    finally:
        # Remove the temporary file
        import os
        os.remove("temp_file.jpg")
