import re
from pathlib import Path

downloads=Path('/Users/rock/Downloads')
file_names=downloads.iterdir() # Type - PosixPath
file_names_str=[file_name.name for file_name in file_names]
#print(file_names_str)
# create a pattern that finds the bills' names for November
pattern=re.compile('nov[a-z]*-(1-9|1[0-9]|2[0-9]|30).txt',re.IGNORECASE)
# Since we have now the List we need to do this
matches=[filename for filename in file_names_str if pattern.findall(filename)]
print(matches)