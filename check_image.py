from fastapi import FastAPI
from classifier import Classifier

# image_classify = Classifier()

# result = image_classify.classify_img('images/Image1.jpg')

# print('Image 1 :- {0}'.format(result))
# print(result['images/Image1.jpg']['safe']*100 >= 89)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}