#include <stdio.h>

float recursive(float init_population, float growth_rate, int years){
    if (years == 0){
        return init_population;
    } else {
        float computed_population = init_population + (init_population*(growth_rate/100));
        recursive(computed_population, growth_rate, years-1);
    }
}



int main(){
    while (1){
        int choice;
        float init_population;
        float growth_rate ;
        int years;
        printf("============================\n");
        printf("POPULATION GROWTH CALCULATOR\n");
        printf("[1] COMPUTE\n");
        printf("[2] EXIT\n");
        printf("SELECT INPUT: ");
        scanf("%d", &choice);
        if (choice == 1){
            printf("ENTER POPULATION (n): ");
            scanf("%f", &init_population);
            printf("ENTER GROWTH RATE (y%%): ");
            scanf("%f", &growth_rate);
            printf("ENTER YEARS (x)): ");
            scanf("%d", &years);
            float population = recursive(init_population, growth_rate, years);
            printf("After %d year(s) at %.0f%% growth rate, the population will be %.2f\n", years, growth_rate, population);
            printf("\n");
        } else if (choice == 2){
            printf("Bye");
            break;
        } else{
            printf("Invalid Input");
            continue;
        }

    }
}