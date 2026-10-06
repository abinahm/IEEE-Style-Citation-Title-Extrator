#Imports regular expression
import re
#Authors: Ahmad Faizuddin bin Ahmad Shahrir, Nidhi Krishna Kumar, Madeeha Iman Sohai Sadiq
#Purpose of code: Make our life easier with Elements


#This makes the raw citations have numbers preceding them
def numbering(input_file,output_file):
    #Opens and reads file
    with open(input_file, "r") as file:
        lines = file.readlines()
    
    #Prepares the numbers 
    numbered_lines = []
    for i, line in enumerate(lines, start=1):
        #To not have spaces in between numbers
        if line.strip():  
            numbered_lines.append(f"{i}. {line.strip()}\n")
    
    #Output file with numbers
    with open(output_file, "w") as file:
        file.writelines(numbered_lines)

#Solving citations with numbers in [] for their citations by removing them       
def removequarebracket(input_file, output_file):
    #Opens and reads file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    reformatted = []

    for line in lines:
        stripped = line.strip()
        if stripped:
            # Replace the [number] with 1.
            cleaned = re.sub(r'^\[\d+\]\s*', '1. ', stripped)
            reformatted.append(cleaned)
        else:
            #Keeps the spaces
            reformatted.append('')  

    #Prints the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(reformatted))
'''
#Removes the numbers in front
def noNumbers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    #Split based on new lines that start with a number and a dot
    entries = re.split(r'\n(?=\d+\.\s)', content)

    cleaned_entries = []
    for entry in entries:
        #removes numbers and dots
        entry = re.sub(r'^(?:\s*\d+\.\s*)+', '', entry)
        #removes [numbers] if there still are any 
        entry = re.sub(r'\[\d+\]', '', entry) 
        #removes the []
        entry = re.sub(r"\[.*?\]", "", entry)
        #joins so no spaces and on one line
        entry = ' '.join(entry.splitlines())  
        #append to the list/array
        cleaned_entries.append(entry.strip())

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in cleaned_entries:
            outfile.write(entry + '\n')
'''

# This is important
#Remove fancy quotes unreadable by Python            
def replaceQuotes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    #Replace fancy quotes with straight quotes
    content = content.replace('“', '"').replace('”', '"')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

# This is also important
#IEEE citation after help from Co-Pilot
def ieeeCitations(output_file, rearranged_file):
    count = 0
    #finds the text within "" and move infront
    with open(output_file, "r") as fin, open(rearranged_file, "w") as fout:
        for line in fin:
            match = re.search(r'"([^"]+)"', line)
            if match:
                title = match.group(1)
                #Remove the title including the quotes from the original line
                rest = line.replace(f'"{title}"', '').strip()
                fout.write(f'{title} {rest}\n')
            else:
                #No title found so the citation stays the same
                fout.write(line)  
          
def ieeeCitations2 (output_file,titleOnly):
    
    #Only outputs titles
    with open(output_file, "r") as fin, open(titleOnly, "w") as fout:
        for line in fin:
            #Find the first thing inside quotes
            match = re.search(r'"([^"]+)"', line)
            if match:
                #only saves the title
                title = match.group(1).rstrip(',')    
                #saves to output file
                fout.write(title + "\n")    
            else:
                #If no matches leave blank
                fout.write("\n")                

'''To use START HERE'''
numbering('references.txt','NUMBERED.txt')
removequarebracket('NUMBERED.txt', 'formatted.txt')
noNumbers('formatted.txt', 'CLEAN.txt')
replaceQuotes('CLEAN.txt', 'ieee.txt')
ieeeCitations('ieee.txt','TITLEFRONT.txt')
ieeeCitations2('ieee.txt','TITLEFONLY.txt')

'''
How to use (if you didn't read the manual):
1. Input raw one line per citation into references.txt
2. Use numbered.txt to send to Co-Pilot and ask to change citation style to IEEE style
3. Copy from Co-Pilot, and paste to references.txt 
4. Use TITLEFRONT.txt to compare and contrast in Elements by sorting A-Z, by pasting the results in the excel sheet
'''


