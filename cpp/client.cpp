/**
  *run with ./client localhost 33001
  */

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>

int main()
{
  int sock;
  struct sockaddr_in server_addr;
  struct hostent *host;
  char send_data[1024]; //creates send_data array in stack

  host= (struct hostent *) gethostbyname((char *)"127.0.0.1");


  if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1)
  {
    perror("could not open socket");
    exit(1);
  }

  server_addr.sin_family = AF_INET;
  server_addr.sin_port = htons(33001);
  server_addr.sin_addr = *((struct in_addr *)host->h_addr);
  memset(&(server_addr.sin_zero),0,sizeof(server_addr.sin_zero));

   while (1)
   {

    printf("Type Something (q or Q to quit):");
    fgets(send_data, sizeof(send_data), stdin);

    if ((strcmp(send_data , "q\n") == 0) || strcmp(send_data , "Q\n") == 0)
       break;

    else
       // specify socket, data, length, 0, struct, size (bytes)
       sendto(sock, send_data, strlen(send_data), 0,
              (struct sockaddr *)&server_addr, sizeof(struct sockaddr));
     
   }

}