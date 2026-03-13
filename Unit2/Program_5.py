def read_and_count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            print("File Contents:\n")
            print(content)
            
            words = content.split()
            word_count = len(words)
            
            print("\nTotal number of words in file:", word_count)
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print("An error occurred:", e)


filename = "sample.txt"
read_and_count_words(filename)
