def process_numbers_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
            numbers = list(map(float, content.split()))
        
            total = sum(numbers)
            maximum = max(numbers)
            minimum = min(numbers)
            
            # Display results
            print("Numbers in file:", numbers)
            print("Total of all numbers:", total)
            print("Maximum number:", maximum)
            print("Minimum number:", minimum)
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except ValueError:
        print("Error: File contains non-numeric data.")
    except Exception as e:
        print("An error occurred:", e)

filename = "numeric.txt"
process_numbers_file(filename)
