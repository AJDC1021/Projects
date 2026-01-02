import csv

while True:
    print("MENU")
    print("[1] START")
    print("[2] STOP")
    select = input("Select your choice: ")
    if select == str(1):
        filename= input("Input the filename: ")
        info_dict = {}
        rating_dict = []
        genre_dict_init = []
        highest_rated = []
        rating_per_genre = {}
        try:
            with open(str(filename), "r") as file:
                reader = csv.reader(file)
                next(reader)
                for line in reader:
                    info_dict[line[0]] = [line[1],float(line[2])]
        except FileNotFoundError:
            print("Please input an existing file")
        if info_dict:
            for value in info_dict.values():
                rating_dict.append(value[1])
                genre_dict_init.append(value[0])
            genre_dict = list(dict.fromkeys(genre_dict_init))
            for key,value in info_dict.items():
                if value[1] == max(rating_dict):
                    highest_rated.append(key)
            for value in info_dict.values():
                if value[0] in rating_per_genre:
                    rating_per_genre[value[0]].append(value[1])
                else:
                    rating_per_genre[value[0]] = [value[1]]
            print()
            for genre,rating in rating_per_genre.items():
                print("The average rating in this genre of " + genre + " " + str(sum(rating)/len(rating)))
                for key,value in info_dict.items():
                    if (genre == value[0]) and (max(rating) == value[1]):
                        print("The highest rated in the genre of " + genre + " is " + key + " with a rating of " + str(value[1]))
                        print()
            print("The highest rated film is ", end="")
            print(*highest_rated,sep=", ", end="")
            print(" with a rating of " + str(max(rating_dict)))
            print("The average rating of the film in the file is " + str(sum(rating_dict)/len(rating_dict)))
            print()
        else:
            print("The file you selected is empty!")
            continue
    elif select == str(2):
        break
    else:
        print("Invalid input, please select a choice between 1 and 2 ")