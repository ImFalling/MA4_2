#include "./person.cpp"
#include <stdio.h>

int main(int argc, char const *argv[])
{
    Person x = Person(40);
    long f = x.fib();
    long y = x.fib_mem();
    printf("%ld\n", f);
    printf("%ld\n", y);
    /* code */
    return 0;
}
