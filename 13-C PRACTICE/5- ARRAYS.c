#include <stdio.h>
#include <stdlib.h>

void input_numbers(int* array, int array_size){
    printf("\n");
    int input;
    int *array_copy = (int *) malloc(sizeof(int)*array_size);
    for (int i=0; i<array_size; i++){
        printf("Enter array[%d]: ", i);
        scanf("%d", &input);
        if (input < 0){
            printf("Error: Invalid value");
            return;
        }
        array_copy[i] = input;
    }

    for (int i=0; i<array_size; i++){
        array[i] = *(array_copy + i);
    }

}

void print_array(int* array, int array_size){
    printf("\n");
    for (int i=0; i<array_size; i++){
        printf("%d\n", array[i]);
    }
}

void fill_array(int *array, int array_size, int fill_no){
    for (int i=0; i<array_size; i++){
        array[i] = fill_no;
    }
}

void factor_finder(int *array, int array_size, int index){
    int flag = 0;
    printf("The factors of %d in the array are:", array[index]);
    for (int i=0; i<array_size; i++){
        if (i != index && array[index]%array[i] == 0){
            printf(" %d", array[i]);
            flag = 1;
        }
    }

    if (flag == 0){
        printf(" None");
    }

    printf("\n");
}

int nonempty_checker(int *array){
    if (*array != -1){
        return 0;
    } else{
        return -1;
    }
}

void all_factor_finder(int* array, int array_size){
    for (int i=0; i<array_size; i++){
        factor_finder(array, array_size, i);
    }
}


int main(){
    int array_size;
    int size_error = 0;
    int *array = (int *) malloc(sizeof(int)*array_size);
    printf("Enter size of array: ");
    scanf("%d", &array_size);
    if (array_size < 1){
        printf("Invalid array size");
        size_error = 1;
    }
    fill_array(array, array_size, -1);
    while (1){
        if (size_error == 1){
            break;
        }
        int index;
        int choice;
        printf("[0] Input Numbers\n");
        printf("[1] Factor of an element in an array\n");
        printf("[2] Factor of all elements in the array\n");
        printf("[3] Exit\n");
        printf("Enter your input: ");
        scanf("%d", &choice);
        if (choice == 0){
            print_array(array, array_size);
            input_numbers(array, array_size);
            print_array(array, array_size);
        } else if (choice == 1){
            if (nonempty_checker(array) == -1){
                printf("Array is empty!\n");
                continue;
            }
            printf("Enter the index of the element: ");
            scanf("%d", &index);
            if (index < 0 || index >= array_size){
                printf("Error: Invalid Index");
                continue;
            }
            factor_finder(array, array_size, index);
        } else if (choice == 2) {
            if (nonempty_checker(array) == -1){
                printf("Array is empty!\n");
                continue;
            }
            all_factor_finder(array, array_size);

        } else if (choice == 3){
            printf("BYE!\n");
            break;
        } else{
            printf("Invalid Input! ");
        }
    }
}