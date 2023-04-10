import re
# Task: Get IP addressess which beging with 12 in the 3rd octet

# Le's the content of the file
with open('ips.txt','r') as file:
    content=file.read()
# Let's create a pattern that can find these IPS, e.x. 192.168.120.111
pattern=re.compile('[0-9]{3}\.[0-9]{3}\.12[0-9]{1}\.[0-9]{3}')
matches=pattern.findall(content)
print(matches)