# Makefile for MA4
all:
	g++ -std=c++14 -c -fPIC person.cpp -o person.o
	g++ -std=c++14 -shared -o libperson.so  person.o	
clean:
	rm -fr *.o *.so __pycache__