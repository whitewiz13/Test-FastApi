from fastapi import FastAPI, File, UploadFile
from classifier import Classifier

image_classify = Classifier()

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        with open(file.filename, "wb") as temp_file:
            temp_file.write(file.file.read())

        # Use the classifier to classify the uploaded file
        result = image_classify.classify_img(file.filename)

        # Return the result
        return {"filename": file.filename, "classification_result": result,"isAccepted":result[file.filename]['safe']*100 >= 89}
    finally:
        # Remove the temporary file
        import os
        os.remove(file.filename)
