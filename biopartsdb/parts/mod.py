# 3WJ-2.html
# apFAB5
import os

for file in os.listdir('.'):
    filename = os.fsdecode(file)
    if filename.endswith(".html"):
        print(filename)
    
        with open(filename, "r+") as f:
            data = f.readlines()
            print(filename)
            for i, line in enumerate(data):
                if 'id="fasta"' in line:
                    print(i)
                    data[i] = "\n"
                    f.seek(0)
                    f.writelines(data)
        
        f.close()
