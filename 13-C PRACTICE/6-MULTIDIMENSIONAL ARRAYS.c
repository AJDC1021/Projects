#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* to_lower_translator(char *name){
    int length = strlen(name);
    char* translated = (char*) malloc(sizeof(char)*length+1);
    for (int i = 0; i< length; i++){
        translated[i] = tolower(name[i]);
    }
    translated[length] = '\0';
    return translated;
}


void name_printer(char *name){
    for (int i = 0; i < strlen(name); i++){
        printf("%c", name[i]);
    }
    printf("\n");
}

void newline_remove(char *name){
    int length = strlen(name);
    if (length > 0 && name[length - 1] == '\n'){
        name[length-1] = '\0';
        length--;
    }
}

char* static_to_dynamic(char *name){
    int length = strlen(name);
    char *name_dynamic = (char*) malloc(sizeof(char)*length+1);
    for (int i = 0; i < length; i++){
        name_dynamic[i] = name[i];
    }
    name_dynamic[length] = '\0';
    return name_dynamic;
}


void compare_names(char* name, char* crush_name, int *flames_count){
    char* copy_name = (char*) malloc(sizeof(char)*strlen(name)+1);
    strcpy(copy_name, name);
    char* copy_crush = (char*) malloc (sizeof(char)*strlen(crush_name)+1);
    strcpy(copy_crush, crush_name);

    int length_name = strlen(copy_name);
    int length_crush = strlen(copy_crush);
    for (int i = 0; i < length_name; i++){
        for (int j = 0; j < length_crush; j++){
            if (copy_name[i] == copy_crush[j] && copy_name[i] != ' ' && copy_name[i] != '0' && copy_crush[j] != ' ' && copy_crush[j] != '0'){
                copy_name[i] = '0';
                copy_crush[j] = '0';
                break;
            }
        }
    }

    for (int i = 0; i < length_name; i++){
        if (copy_name[i] != '0' && copy_name[i] != ' '){
             (*flames_count)++;
        }
    }

    for (int i = 0; i < length_crush; i++){
        if (copy_crush[i] != '0' && copy_crush[i] != ' '){
            (*flames_count)++;
        }
    }

    free(copy_crush);
    free(copy_name);
}

char flame_counter(int flames_count){
    char flames[7] = "flames\0";

    int count_copy = flames_count;

    for (int i = 0; i < 5; i++){
        int flames_length = 6-i;
        int count = flames_count-flames_length;
        while (count > flames_length){
            count = count - flames_length;
        }
        count--;

        for (int j = 0; j < count+1; j++){
            if (flames[j] == '0'){
                count++;
            }
        }

        flames[count] = '0';

    }
    
    char result = ' ';
    
    for (int i = 0; i < strlen(flames); i++){
        if (flames[i] != '0'){
            result = flames[i];
        }
    }

    return result;
}

void decider(char result, int flames_count, char* name){
    name_printer(name);
    printf("REMAINING CHARACTER COUNT: %d\n", flames_count);
    if (result=='f'){
        printf("FLAMES RESULT: FRIENDS\n");
    } else if (result=='l'){
        printf("FLAMES RESULT: LOVE\n");
    } else if (result=='a'){
        printf("FLAMES RESULT: AFFECTION\n");
    } else if (result=='m'){
        printf("FLAMES RESULT: MARRIAGE\n");
    } else if (result=='e'){
        printf("FLAMES RESULT: ENEMY\n");
    } else if (result == 's'){
        printf("FLAMES RESULT: SIBLINGS\n");
    }
}

void free_function(char** array, int names_amount){
    for (int i=0; i<names_amount; i++){
        free(array[i]);
    }

    free(array);
}

void input_names(char** array_of_crushes, char *crush_name_static, int names_amount, int *empty_flag){
    for (int i = 0; i < names_amount; i++){
        *empty_flag = 0;
        printf("Enter crush name: ");
        fgets(crush_name_static, 50, stdin);
        newline_remove(crush_name_static);
        char* crush_name = static_to_dynamic(crush_name_static);
        array_of_crushes[i] = crush_name;
    }
}

void lister(char** array_of_crushes, char* name, int flames_count, int names_amount){
    for (int i = 0; i < names_amount; i++){
        printf("Crush #%d: ", (i+1));
        flames_count = 0;
        char* lowered = to_lower_translator(array_of_crushes[i]);
        compare_names(name, lowered, &flames_count);
        free(lowered);
        char result = flame_counter(flames_count);
        decider(result, flames_count, array_of_crushes[i]);
    }
}

int main(){
    char name_static[50];
    char crush_name_static[50];
    int flames_count = 0;
    int x = 10;
    int names_amount;
    int empty_flag = 1;
    

    printf("Enter name: ");
    fgets(name_static, 50, stdin);
    newline_remove(name_static);
    char* name_orig = static_to_dynamic(name_static);
    char* name = to_lower_translator(name_orig);
    free(name_orig);

    printf("Enter the number of your crushes: ");
    scanf("%d", &names_amount);
    getchar();
    char** array_of_crushes = (char**) malloc(sizeof(char*) * names_amount);

    while (1){
        int choice;
        printf("MENU\n");
        printf("[1] INPUT NAMES\n");
        printf("[2] COMPUTE FLAME RESULTS\n");
        printf("[0] EXIT\n");
        printf("ENTER INPUT: ");
        scanf("%d", &choice);
        getchar();
        if (choice==1){
            input_names(array_of_crushes, crush_name_static, names_amount, &empty_flag);
        } else if (choice==2){
            if (empty_flag==1){
                printf("ARRAY IS EMPTY\n");
                continue;
            }
            lister(array_of_crushes, name, flames_count, names_amount);
        } else if (choice==0){
            printf("BYE!\n");
            free(name);
            free_function(array_of_crushes, names_amount);
            break;
        } else {
            printf("INVALID CHOICE\n");
        }
    }
}