import csv

genre_list = []
ratings_dict = {}
amount = 0
total = 0
all_ratings = []
all_lines = []

while True:
    print("===MENU===")
    print("[1] START")
    print("[2] EXIT")
    try:
        select = int(input("Select input: "))
    except ValueError:
        print("Error: Invalid input! Please input integer.")
        continue
    if select == 1:
        filename = input("Please input filename: ")
        print()
        try:
            try:
                with open(filename, mode='r', newline='') as reader:
                    csv_reader = csv.reader(reader, delimiter=',')
                    next(csv_reader)
                    for line in csv_reader:
                        amount += 1
                        total += float(line[2])
                        all_ratings.append(float(line[2]))
                        all_lines.append(line)
                        if line[1] in ratings_dict:
                            ratings_dict[line[1]]['amount'] += 1
                            ratings_dict[line[1]]['total'] += float(line[2])
                            ratings_dict[line[1]]['film_titles'].append(line[0])
                            ratings_dict[line[1]]['film_scores'].append(line[2])
                        else:
                            ratings_dict[line[1]] = {}
                            ratings_dict[line[1]]['amount'] = 1
                            ratings_dict[line[1]]['total'] = float(line[2])
                            ratings_dict[line[1]]['film_titles'] = []
                            ratings_dict[line[1]]['film_titles'].append(line[0])
                            ratings_dict[line[1]]['film_scores'] = []
                            ratings_dict[line[1]]['film_scores'].append(line[2])
            except StopIteration:
                print("File is empty")
                continue
        except FileNotFoundError:
            print("Error: File not found.")
            continue
        highest_rating = max(all_ratings)
        lowest_rating = min(all_ratings)
        highest_grade_list = {}
        lowest_grade_list = {}
        for key, value in ratings_dict.items():
            ratings_dict[key]['average_rating'] = float(value['total']/value['amount'])
            highest_grade = max(ratings_dict[key]['film_scores'])
            lowest_grade = min(ratings_dict[key]['film_scores'])
            for i in range(len(ratings_dict[key]['film_scores'])):
                if ratings_dict[key]['film_scores'][i] == highest_grade:
                    if key in highest_grade_list:
                        highest_grade_list[key]['titles'].append(ratings_dict[key]['film_titles'][i])
                    else:
                        highest_grade_list[key]={}
                        highest_grade_list[key]['titles'] = []
                        highest_grade_list[key]['titles'].append(ratings_dict[key]['film_titles'][i])
                        highest_grade_list[key]['grade'] = ratings_dict[key]['film_scores'][i]
                if ratings_dict[key]['film_scores'][i] == lowest_grade:
                    if key in lowest_grade_list:
                        lowest_grade_list[key]['titles'].append(ratings_dict[key]['film_titles'][i])
                    else:
                        lowest_grade_list[key]={}
                        lowest_grade_list[key]['titles'] = []
                        lowest_grade_list[key]['titles'].append(ratings_dict[key]['film_titles'][i])
                        lowest_grade_list[key]['grade'] = ratings_dict[key]['film_scores'][i]
        total_rating = float(total/amount)


        print("===AVERAGE RATING PER GENRE===")
        for key,value in ratings_dict.items():
            avg_rate = str(value['average_rating'])
            print("The average rating for the genre of " + key + " is " + avg_rate)
        print()

        print("===HIGHEST RATING PER GENRE===")
        for key,value in highest_grade_list.items():
            high_grade = str(value['grade'])
            print("The highest rating per genre is/are ", end='')
            for i in range(len(value['titles'])):
                if i == len(value['titles']) - 1:
                    print(value['titles'][i], end=' ')
                else:
                    print(value['titles'][i], end=', ')
            print("with the grade of " + str(high_grade))
        print()

        print("===LOWEST RATING PER GENRE===")
        for key,value in lowest_grade_list.items():
            low_grade = str(value['grade'])
            print("The lowest rating per genre is/are ", end='')
            for i in range(len(value['titles'])):
                if i == len(value['titles']) - 1:
                    print(value['titles'][i], end=' ')
                else:
                    print(value['titles'][i], end=', ')
            print("with the grade of " + str(low_grade))
        print()

        print("The total rating of all films in the list is " + str(total_rating))
        for items in all_lines:
            if float(items[2]) == highest_rating:
                print("The highest rating of all films in the list is " + str(items[0]) + " with the rating of " + str(highest_rating))
            if float(items[2]) == lowest_rating:
                print("The lowest rating of all films in the list is " + str(items[0]) + " with the rating of " + str(lowest_rating))
        print()
    elif select == 2:
        print("Bye!")
        break
    else:
        print("Invalid input.")
