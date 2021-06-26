#include <iostream>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
using namespace std;
  
int main()
{
    // ftok to generate unique key
    key_t key = ftok("shmfile",65);
  
    // shmget returns an identifier in shmid
    int shmid = shmget(key,1024,0666|IPC_CREAT);
    if (shmid == -1)
    {
        perror("Could not get shared memory");
        return EXIT_FAILURE;
    }
    printf("Shared memory id: %i\n", shmid);
  
    // shmat to attach to shared memory
    char *str = (char*) shmat(shmid,(void*)0,0);
  
    cout<<"Write Data : ";
    fgets(str, 50, stdin);
  
    printf("Data written in memory: %s\n",str);
      
    //detach from shared memory 
    shmdt(str);
  
    return 0;
}