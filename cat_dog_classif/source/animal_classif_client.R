library(pacman)
p_load_current_gh("nfultz/grpc")
p_load(imager)

impl <- read_services('./../proto/cat_dog.proto')
client <- grpc_client(impl, "localhost:50051")

image <- load.image("./../data/bed-1284238_640.jpg")

message <- client$cat_or_dog$build(width = dim(image)[1], height = dim(image)[2], 
                                   image_red = as.raw(image[,,,1]*255),
                                   image_green = as.raw(image[,,,2]*255),
                                   image_blue = as.raw(image[,,,3]*255))

response <- client$cat_or_dog$call(message)

print(response)
print(as.list(response))
