from concurrent import futures
import logging
from PIL import Image
import tensorflow as tf
import numpy as np
import grpc
import sys
sys.path.append("../proto_output")
import cat_dog_pb2_grpc
import cat_dog_pb2

model_path = "./../model/cats_vs_dogs_cnn"

class Animal_classif(cat_dog_pb2_grpc.Animal_classifServicer):
    def __init__(self):
        self.model = tf.keras.models.load_model(model_path)


    def cat_or_dog(self, request, context):
        image_red = np.array(Image.frombytes('L', (request.width, request.height), request.image_red, 'raw'))
        image_green = np.array(Image.frombytes('L', (request.width, request.height), request.image_green, 'raw'))
        image_blue = np.array(Image.frombytes('L', (request.width, request.height), request.image_blue, 'raw'))
        image = np.dstack((image_blue,image_green,image_red))/255
              
        open_cv_image = tf.image.resize(image, size=(150, 150))
        prediction = self.model.predict(np.expand_dims(open_cv_image, 0))[0][0]

        animal = "dog"
        if prediction>0.5:
            animal = 'cat'

        return cat_dog_pb2.AnimalResponse(animal = animal)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cat_dog_pb2_grpc.add_Animal_classifServicer_to_server(Animal_classif(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
