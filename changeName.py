import os
import re

def changeFileName():
    pattern = r'[0-9][0-9]'
    for filename in os.listdir('./'):
        if 'day' in filename:
            match = re.search(pattern, filename)
            if match:
                new_name = filename.replace(match.group(0), '0'+match.group(0))
                os.rename(filename, new_name)

def changeReadme():
    pattern = r'day_([0-9][0-9])\.py'
    file = open('README.md', 'r')

    data = file.read()
    file.close()
    file = open('README.md', 'w')
    data = data.split('\n')
    
    for line in data:
        match = re.search(pattern, line)
        if match:
            file_name = match.group(0)
            new_file_name = file_name.replace(match.group(1), '0'+match.group(1))
            line = line.replace(match.group(0), new_file_name)
        file.write(line + '\n')
    file.close()