# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging
import sys
import grpc
import numpy as np
import cv2
from PIL import Image
sys.path.append("../proto_output")

import cat_dog_pb2
import cat_dog_pb2_grpc


def run():
    img = cv2.imread("./../data/bed-1284238_640.jpg")
    img_red_bytes = img[:,:,2].tobytes()
    img_green_bytes = img[:,:,1].tobytes()
    img_blue_bytes = img[:,:,0].tobytes()
    width = img.shape[1]
    height = img.shape[0]

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cat_dog_pb2_grpc.Animal_classifStub(channel)
        response = stub.cat_or_dog(cat_dog_pb2.ImageRequest(width=width, height=height, image_red=img_red_bytes,
                                                            image_green=img_green_bytes, image_blue=img_blue_bytes))
    print("Response: " + response.animal)


if __name__ == '__main__':
    logging.basicConfig()
    run()
