#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void main()
{
    char *ptr;
    char *dptr;
    // clrscr();
    ptr = (char *)malloc(10 * sizeof(char));
    dptr = (char *)malloc(10 * sizeof(char));
    printf("Address of ptr: %d\n", ptr);
    printf("Address of dptr: %d\n", dptr);
    printf("Enter The String:\n");
    // gets(ptr);
    fgets(ptr, 10, stdin); 
    system(dptr);
}