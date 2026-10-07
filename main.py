#Imports regular expression
import re
import tempfile
import shutil
import os

INPUT_FILE = "references.txt"

# Read function
def read_lines (filename):
    with open(filename, "r", encoding = "utf-8") as f:
        return f.readlines()

# Write function
def write_lines (filename, lines):
    with open(filename, "w", encoding = "utf-8") as f:
        f.writelines(lines)

def remove_square_brackets (lines):
    return 

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

# This is important
#Remove fancy quotes unreadable by Python            
def replaceQuotes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    #Replace fancy quotes with straight quotes
    content = content.replace('“', '"').replace('”', '"')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

#IEEE citation after help from Co-Pilot
def ieeeCitations(output_file, rearranged_file):
    count = 0
    #finds the text within "" and move infront
    with open(output_file, "r") as fin, open(rearranged_file, "w") as fout:
        for line in fin:
            match = re.search(r'"([^"]+)"', line)
            if match:
                title = match.group(1)
                rest = line.replace(f'"{title}"', '').strip()
                fout.write(f'{title} {rest}\n')
            else:
                fout.write(line)  
          
def ieeeCitations2 (output_file,titleOnly):
    with open(output_file, "r") as fin, open(titleOnly, "w") as fout:
        for line in fin:
            match = re.search(r'"([^"]+)"', line)
            if match:
                title = match.group(1).rstrip(',')    
                fout.write(title + "\n")    
            else:
                fout.write("\n")   

KEEP_INTERMEDIATE = False

if __name__ == "__main__":
    work_dir = "intermediate_files" if KEEP_INTERMEDIATE else tempfile.mkdtemp()
    os.makedirs(work_dir, exist_ok=True)

    def p(name):
        return os.path.join(work_dir, name)

    numbering('references.txt', p('NUMBERED.txt'))
    removequarebracket(p('NUMBERED.txt'), p('formatted.txt'))
    noNumbers(p('formatted.txt'), p('CLEAN.txt'))
    replaceQuotes(p('CLEAN.txt'), p('ieee.txt'))

    ieeeCitations(p('ieee.txt'), 'TITLEFRONT.txt')
    ieeeCitations2(p('ieee.txt'), 'TITLEONLY.txt'
    if not KEEP_INTERMEDIATE:
        shutil.rmtree(work_dir)

    with open('TITLEONLY.txt', encoding='utf-8') as f:
        titles = [line.strip() for line in f]

        found = sum(1 for t in titles if t)
        missing = [i for i, t in enumerate(titles, 1) if not t]

        print(f"Done: {found}/{len(titles)} titles found.")
    if missing:
        print(f"No title found on lines: {missing}")
        print("Saved to TITLEFRONT.txt and TITLEONLY.txt")


