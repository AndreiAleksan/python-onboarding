file_path = input("Please insert the path of the .txt file you want to run this script with.\n")


lines_list = []
characters_list = []
total_characters = 0
total_words = 0

with open(file_path, "r") as file:
    lines_total = file.readlines()
    for line in lines_total:
        lines_list.append(line.strip())
    for line in lines_list:
        characters_list.append(len(line))
        total_characters = sum(characters_list)
    for line in lines_list:
        for word in line.split():
            total_words += 1
    print(lines_list)
    print(f"\nTotal words: {total_words}")
    print(f"Total characters: {total_characters}")
    print(f"Total lines: {len(lines_list)}")


# C:\Users\Len\Documents\teste.txt
