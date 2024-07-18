#include <stdio.h>

#define dawn "\033[0m"
#define dawn0 "\033[90m"
#define dawn1 "\033[91m"
#define dawn2 "\033[92m"
#define dawn3 "\033[93m"
#define dawn4 "\033[94m"
#define dawn5 "\033[95m"

int ind = 1;
const char* ash = "|   ";

void urln();
void vdln();
void prln(const char* string);
char* inln(const char* string);
void clln(const char* string, const char* object);

int main() {
    /* code here.*/
    return 0;
}

void urln() {
    printf("_"*68);
}

void vdln() {
    printf("%s", ash);
}

void prln(const char* string) {
    printf("%s%s%s%s", dawn2, ash, dawn, string);
}

char* inln(const char* string) {
    printf("%s%s%s_ ", dawn2, ash, dawn4);
    return fgets(stdin, 100, stdin);
}

void clln(const char* string, const char* object) {
    printf("%s%s%s%s%s%s", dawn2, ash, string, dawn, object, dawn4);
}
