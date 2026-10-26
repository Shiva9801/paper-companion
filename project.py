import re
import json
from pathlib import Path
import pymupdf

def main():
    name = input("Enter the PDF or TXT file path: ").strip().strip('"') #using '"' to remove the quotes in the path
    content = load_paper(name)

    if content is None:
        print("Error- file not found")
    else:
        while True:
            print("1. Search for a word")  # this is the first MENU user sees
            print("2. Read a section")
            print("3. Manage glossary")
            print("4. Manage Notes" )
            print("5. Exit" + "\n")

            choice = input("Enter your choice : ")
            match choice:
                case "1":
                    print("Search fo a word")
                    q=input("Enter the word to find : ")
                    if not q.strip():
                        print("PLease give a non-empty search query")
                        
                    else:                            

                        pos = 0
                        found = False
                
                        while True:
                            pos = content.lower().find(q.lower(), pos)
                
                            if pos == -1:
                                break
                
                            start = max(0, pos - 10)
                            end = min(len(content), pos + len(q) + 10)
                
                            print(content[start:end].strip())
                            print("-" * 30)
                
                            pos += len(q)
                            found = True
                
                        if not found:
                            print("Word not found.")
                        
                case "2":
                    print("Read a section")

                    lines=content.splitlines(keepends=True)
                    headings=[]
                    
                    position=0
                    for line in lines:
                        if re.match(r'^\d{1,2}\s+[A-Z][A-Za-z\- ]{2,60}$', line.strip()):  #regex for pattern with numbers and capital letter follwing it 
                            headings.append((line.strip(),position))
                        position += len(line)

                    if not headings:
                        print("No recognizable section headings found in this paper.")
                        print("-" * 30)
                    else:
                        
                        for heading, position in headings:
                            print(heading)
                        x=input("Enter the Section you want : ")
                        found=False
                        for i, (heading, start) in enumerate(headings):
                            parts=heading.split()
                            if parts[0]==x:
                                if i+1 < len(headings):
                                    end=headings[i+1][1]
                                else:
                                    end=len(content)
                                print(content[start:end])
                                found=True
                                break
                        if not found:
                            print("Section not found.")
                            print("-" * 30)

                case "3":
                    manage_glossary()

                case "4":
                    manage_notes(name)
                case "5":
                    break   
                case _:
                    print("Invalid Choice")
                    print("-" * 30)

        
# def load_paper(name): //old code only for txt files
#     try:
#         with open(name, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         return None
def load_paper(name):
    name=Path(name)
    try:
        if name.suffix.lower()==".pdf":  # handles PDF files
            content = ""

            with pymupdf.open(name) as pdf:
                for page_number, page in enumerate(pdf, start=1):
                    content += f"\n{'=' * 20} Page {page_number} {'=' * 20}\n\n"
                    content += page.get_text("text", sort=True) + "\n"

            output_path = Path("extracted_text") / f"{Path(name).stem}.txt" # stem is used to get the filename without extension and then save the extracted text in a folder called "extracted_text" with the same name as the PDF file but with a .txt extension
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w", encoding="utf-8") as file:
                file.write(content) # used to write the extracted text to the output file

            print(f"Extracted text saved to: {output_path}")
            return content

        with open(name, "r", encoding="utf-8") as file:  # handles TXT files
            return file.read() 

    except (FileNotFoundError, OSError):
        print("File could not be opened.")
        return None

def manage_glossary():
    try:
        with open("glossary.json",'r')as file:
            glossary=json.load(file)

    except FileNotFoundError:
        glossary={}
    except json.JSONDecodeError:
        print("Invalid JSON file")
        print("-" * 30)
        return
    while True:
        
        
        print("1. Add a term")
        print("2.View all saved terms")
        print("3. Exit "+"\n")
        option=input("Enter your option : ")
        match option:
            case "1":
                key=input("Enter the term: ")
                if key in glossary:
                    print("The key Exists in the glossary")
                else:
                    value=input("Enter the meaning: ")
                    glossary[key] =value
                    
                    with open("glossary.json",'w')as file:
                        json.dump(glossary, file, indent=4)
                    print("saved Successfully!")
                
            case "2":
                for key,value in glossary.items():
                    print(f"{key}: {value}")
                          
            case "3":
                print("Bye BYe !")
                break


def manage_notes(name):
    try:
        with open("notes.json", "r")as file:
            notes=json.load(file)
    except FileNotFoundError:
        notes={}
    except json.JSONDecodeError:
            print("Invalid JSON file")
            return
    if name not in notes:
        notes[name]=[]
    
    while True:
        print("1. Add Note")
        print("2. View Saved notes")
        print("3. Return to main menu"+"\n")
        choice=input("Enter choice: "+"\n")
        match choice:
            case "1":
                note=input("enter you note: ")
                notes[name].append(note)

                with open("notes.json","w")as file:
                    json.dump(notes, file, indent=4)
            case "2":
                if not notes[name]:
                    print("No notes saved for this paper yet. ")
                else:
                    print("Saved Notes.")
                    for i, note in enumerate(notes[name], start=1):
                        print(f"{i}. {note}")
                print("-" * 30)
            case "3":
                return




if __name__ == "__main__":
    main()


