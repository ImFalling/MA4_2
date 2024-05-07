#include "./person.cpp"
#include <stdio.h>

int main(int argc, char const *argv[])
{
    Person x = Person(51);
    long f = x.fib();
    printf("%ld\n", f);
    /* code */
    return 0;
}
