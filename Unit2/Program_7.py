def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
            
        with open(destination_file, 'w') as dest:
            dest.write(content)
        
        print(f"File '{source_file}' copied successfully to '{destination_file}'.")
    
    except FileNotFoundError:
        print("Error: Source file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

source = "sample.txt"      
destination = "copy.txt"     
copy_file(source, destination)
