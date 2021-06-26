# Generate code
Makefile is provided:
	
	make

# Run the code

writer creates shared memory segment and writes to memory. dettaches before program exits:

	./ipc_writer

to see the shared memory segment that has been created open a new terminal and run:

	ipcs -a

you can see the shared memory segmet with its shmid, permissions 666 ,size 1024, and how many programs are attached

read from the shared memory segment and then destroy it:

	./ipc_reader
