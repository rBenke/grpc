#' Example gRPC client
#'
#' Sends a message with a name and returns a message greeting the name.
#' @references \url{https://github.com/grpc/grpc/tree/master/examples/cpp/helloworld}

library(pacman)
p_load_current_gh("nfultz/grpc")


spec <- system.file('examples/helloworld.proto', package = 'grpc')
impl <- read_services(spec)
client <- grpc_client(impl, "localhost:50051")

hello <- client$SayHello$build(name='Robert')
message <- client$SayHello$call(hello)

print(message)
print(as.list(message))
