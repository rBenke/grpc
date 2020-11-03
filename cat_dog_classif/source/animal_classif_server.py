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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import sys
sys.path.append("../proto_output")
import cat_dog_pb2_grpc
import cat_dog_pb2



class Animal_classif(cat_dog_pb2_grpc.Animal_classifServicer):

    def ImageRequest(self, request, context):
        return cat_dog_pb2.AnimalResponse(message= "cat")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cat_dog_pb2_grpc.add_Animal_classifServicer_to_server(Animal_classif(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
