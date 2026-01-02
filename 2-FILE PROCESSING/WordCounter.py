import string

print("What is the filename?")
filename = input()

counter_dict={}
line_found=[]
translator = str.maketrans('', '', string.punctuation)

try:
    with open(str(filename), mode = 'r',) as file:
        for line in file:
            story = line.split()
            line_found.clear()
            for i in range(len(story)):
                word_init = str(story[i].lower())
                word = word_init.translate(translator)
                if word not in counter_dict:
                    counter_dict[word]=0
                if word not in line_found:
                    line_found.append(word)
                else:
                    continue
                for j in range(len(story)):
                    compare_word = str(story[j].lower())
                    if word == compare_word:
                        counter_dict[word] += 1
except FileNotFoundError:
    print("Error: The file " + filename + " was not found.")

First=[]
FirstValue=0
Second=[]
SecondValue=0
Third=[]
ThirdValue=0
Fourth=[]
FourthValue=0
Fifth=[]
FifthValue=0 

value_list_init = list(counter_dict.values())
value_list = list((dict.fromkeys(value_list_init)))
if value_list:
    FirstValue = max(value_list)
    value_list.remove(FirstValue)
if value_list:
    SecondValue = max(value_list)
    value_list.remove(SecondValue)
if value_list:
    ThirdValue = max(value_list)
    value_list.remove(ThirdValue)
if value_list:
    FourthValue = max(value_list)
    value_list.remove(FourthValue)
if value_list:
    FifthValue = max(value_list)
    value_list.remove(FifthValue)
for key, value in counter_dict.items():
    if value == FirstValue:
        First.append(key)
    elif value == SecondValue:
        Second.append(key)
    elif value == ThirdValue:
        Third.append(key)
    elif value == FourthValue:
        Fourth.append(key)
    elif value == FifthValue:
        Fifth.append(key)
    else:
        continue

if not First:
    print("Input file is empty!")
else:
    print("The following words appeared the most: ", end="")
    print(*First, sep = ", ", end ="")
    print(" with them appearing " + str(FirstValue) + " times.")

if not Second:
    print("There is no other words in the input file!")
else:
    print("The following words appeared the second most: ", end="")
    print(*Second, sep = ", ",end ="")
    print(" with them appearing " + str(SecondValue) + " times.")

if not Third:
    print("There is no other words in the input file!")
else:
    print("The following words appeared the third most: ", end="")
    print(*Third, sep = ", ",end ="")
    print(" with them appearing " + str(ThirdValue) + "times.")

if not Fourth:
    print("There is no other words in the input file!")
else:
    print("The following words appeared the fourth most: ", end="")
    print(*Fourth, sep = ", ",end ="")
    print(" with them appearing " + str(FourthValue) + " times.")

if not Fifth:
    print("There is no other words in the input file!")
else:
    print("The following words appeared the fifth most: ", end="")
    print(*Fifth, sep = ", ",end ="")
    print(" with them appearing " + str(FifthValue) + " times.")




