def word_count(file):
    counter = 0
    words = file.split()
        
    for i in words:
        counter += 1
        
    
    return counter

def character_count(file):
    lower_case = file.lower()
    
    count = {}
    for character in lower_case:
        if character not in count:
            count[character] = 1
        elif character in count:
            count[character] += 1            
            
    return count
            
def report_generator(count):
    sorted_list = []
    for letter, freq in count.items():
        if letter.isalpha():
            sorted_list.append({"letter": letter, "num": freq})
    
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
        
    print("--- Begin report ---")
    for item in sorted_list:
        report = f"The '{item['letter']}' character was found {item['num']} times"
        print(report)
    print("--- End report ---")
            

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count(file_contents)
    character_count(file_contents)
    report_generator(character_count(file_contents))
        

main()