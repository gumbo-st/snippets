###############################################################################
#
#
###############################################################################

CC = g++
CFLAGS = -g -Wall

#OBJS = utils.o


ALL: main

%.o : %.cpp Makefile
	$(CC) $(CFLAGS) -c $< -o $@


main: main.cpp $(OBJS)
	$(CC) $(CFLAGS) $(INCS) $(OBJS) main.cpp -o main

clean:
	$(RM) main $(OBJS)
