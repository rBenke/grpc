
#' Example gRPC service
#'
#' Reads a message with a name and returns a message greeting the name.
#' @references \url{https://github.com/grpc/grpc/tree/master/examples/cpp/helloworld}

library(pacman)
p_load_current_gh("nfultz/grpc")


## reading the service definitions
spec <- system.file('examples/helloworld.proto', package = 'grpc')

impl <- read_services(spec)

impl$SayHello$f <- function(request){
  newResponse(message = paste('Hello,', request$name))
}

## actually running the service handlers
start_server(impl, "0.0.0.0:50051")
