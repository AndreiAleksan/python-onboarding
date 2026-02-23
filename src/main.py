

def wlc_counter(file_name): 

    lines_list = []
    characters_list = []
    total_characters = 0
    total_words = 0

    with open(file_name, "r") as file:
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

def main():
    file_path = input("Please insert the path of the .txt file you want to run this script with.\n")
    wlc_counter(file_path)

if __name__ == "__main__":
    main()
    # C:\Users\Len\Documents\teste.txt
