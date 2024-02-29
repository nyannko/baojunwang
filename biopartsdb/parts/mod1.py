import os

for file in os.listdir('.'):
    filename = os.fsdecode(file)
    if filename.endswith(".html"):
        print(filename)
    
        with open(filename, "r+") as f:
            data = f.readlines()
            print(filename)
            for i, line in enumerate(data):
                if 'id="referencing"' in line:
                    print(i)
                    fn = filename.split('.')[0]
                    st = '<div class="full_column" id="download"><h3>Download</h3><p><a href="' + fn + '.fasta" id="fasta">FASTA</a></p></div>' + '<div class="full_column" id="referencing">'
                    print(st)
                    data[i] = st 
                    f.seek(0)
                    f.writelines(data)
        
        f.close()
