def wlc_counter(file_name): 

    total_characters = 0
    total_words = 0

    with open(file_name, "r") as file:
        lines_list = file.readlines()
        total_lines = len(lines_list)

        for line in lines_list:
            total_characters += len(line)

        for line in lines_list:
            for word in line.split():
                total_words += 1

    return total_lines, total_characters, total_words

if __name__ == "__main__":
    file_path = input("Please insert the path of the .txt file you want to run this script with.\n")
    total_lines, total_characters, total_words = wlc_counter(file_path)

    print(f"Total lines: {total_lines}")
    print(f"Total characters: {total_characters}")
    print(f"Total words: {total_words}")

# C:\Users\Len\Documents\andrei-python-onboarding\tests\test_document.txt