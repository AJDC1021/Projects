#include <stdio.h>
#include <string.h>

int get_input(int *x, int *y){
    printf("Enter x: ");
    scanf("%d", x);

    printf("Enter y: ");
    scanf("%d", y);

    if (*x < 2 && *y < 2){
        printf("Invalid Range!\n");
        return -1;
    }

    return 1;
}

void swap_values(int *x, int *y){
    if (*x > *y){
        int temp = *x;
        *x = *y;
        *y = temp;
    }
}

/*
int primeChecker(int num){
    for (int i = 2; i < num; i++){
        if (num % i == 0){
            return -1;
        }
    }
    return 1;
}*/


int primeChecker(int num, int num_copy){
    if (num <= 1){
        return -1;
    }

    int dividor = num_copy - 1;
    if (dividor == 1){
        return 1;
    } else{
        if (num % dividor == 0){
            return -1;
        }
        return primeChecker(num, dividor);
    }
}

void printLargest(int *first, int *second, int *third){
    if (*first == 0){
        printf("No prime numbers found\n");
    } else if (*second == 0){
        printf("There is one prime number: %d\n", *first);
    } else if (*third == 0){
        printf("The two prime numbers are: %d %d\n", *first, *second);
    } else{
        printf("The three prime numbers are: %d %d %d\n", *first, *second, *third);
    }
}

void getLargest(int *x, int *y, int *first, int *second, int *third){
    if (get_input(x, y) == 1){
        swap_values(x, y);

        for (int i = *x; i<=*y; i++){
            if (primeChecker(i,i) == 1){

                if (i > *first){
                    int temp = *second;
                    *second = *first;
                    *third = temp;
                    *first = i;
                    
                } else if (i > *second){
                    *third = *second;
                    *second = i;
                } else if (i > *third){
                    *third = i;
                }
            }
        }
        printLargest(first, second, third);
    }

}


void main(){
    while (1){
        int x, y, first = 0, second = 0, third = 0;
        getLargest(&x, &y, &first, &second, &third);
    }
}