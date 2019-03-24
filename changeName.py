
import os
import re

pattern = r'[0-9][0-9]'
for filename in os.listdir('./'):
    if 'day' in filename:
        match = re.search(pattern, filename)
        if match:
            new_name = filename.replace(match.group(0), '0'+match.group(0))
            os.rename(filename, new_name)
            