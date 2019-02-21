import csv
import sys
import os

if len(sys.argv) < 3:
    sys.exit('Usage: \npython %s [csv file] [root search dir]\n\nExample: \npython %s spam.csv "c:\search dir"'  % (sys.argv[0], sys.argv[0]))

# holds all of the replacement key pairs
replace_dict = {}

# construct file paths to the csv file and the root path of the target search directory
csv_file_path = os.path.abspath(sys.argv[1])
root_search_path = os.path.abspath(sys.argv[2])

# populate our replacement dictionary with the values from the csv file
csv_reader = csv.reader(open(csv_file_path, "r"))

for row in csv_reader:
    replace_dict[row[0]] = row[1]

# actually do the replacement
for dir, subdirs, names in os.walk(root_search_path):
    # itterate through every file name in the directory
    for name in names:
        # make sure that we only edit wwise files
        if name.lower().endswith(".wwu"):
            # keep track of if we've done a replacement on this text
            changed = False
            
            # create the path to the target file
            path = os.path.join( dir, name )
            
            # open the text to the target file
            text = open(path).read()
            
            #check to see if we need to do a replacement for each key in the replacement dictionary
            for key in replace_dict.keys():                
                if key in text:
                    text = text.replace(key, replace_dict[key])
                    changed = True
            
            #if we changed the file, write the changed file back
            if changed:
                open( path, 'w').write(text)