#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define PORT 8580

char *pub_file(char *file_name)
{
  // Function for read pub clinet file
  // end return charsets in head

  char fname[100];

  size_t i;
  for (i = 0; i < strlen(file_name); i++)
  {
    fname[i] = file_name[i];
  }
  fname[i] = '\0';

  char *pub = "_privatekey";
  strcat(fname, pub);

  printf("%s\n", fname);

  FILE *fp = fopen(fname, "r");

  if (!fp)
  {
    printf("Can't open file with name %s\n", fname);
    return NULL;
  }

  char *text = malloc(45);

  fgets(text, 45, fp);

  fclose(fp);

  return text;
}

char *rname(char const *command)
{
  // returns the name from the command that comes into the buffer from the client

  int count = 0, flag = 0, j = 0;
  char *name_use = malloc(sizeof(command[0])*50);

  while (1)
  {
    if (flag)
    {
      if (command[count] == ' '){
        name_use[j] = '\0';
        break;
      }

      name_use[j++] = command[count];
    }

    if (command[count] == ' ') flag = 1;

    count++;
  }

  return name_use;
}

void server_up()
{
  int server_fd, new_socket;
  ssize_t valread;
  struct sockaddr_in address;

  socklen_t addrlen = sizeof(address);
  char buffer[1024] = { 0 };
  // char* hello = "Hello from server";

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
    
    // in buffer = command <userName> <ip_address_user>
    system(buffer);

    // get use name for pubkey
    char *names_use = rname(buffer);

    // get publick key user
    char *pubkey = pub_file(names_use);

    free(names_use);
    names_use = NULL;
    
    send(new_socket, pubkey, strlen(pubkey), 0);

    free(pubkey);
    pubkey = NULL;

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