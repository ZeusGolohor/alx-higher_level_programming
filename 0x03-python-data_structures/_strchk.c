#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int *tab;
    tab = malloc(sizeof(*tab) * 3);
    printf("%ld\n", sizeof(tab));
}
