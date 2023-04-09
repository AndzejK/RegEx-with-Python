import re
"""
    ###  Meta characters ###

\ -> escape of meta characters    
The dot (.) represents any character.
The caret (^) represents the beginning of a line.
The dollar sign ($) represents the end of a line.
The asterisk (*) represents zero or more occurrences of the previous character or group.
The plus sign (+) represents one or more occurrences of the previous character or group.
The question mark (?) represents zero or one occurrences of the previous character or group.
The brackets ([ ]) represent a character set, the order of characters does not MATTER!
The curly braces {M,N} - matches the preceeding element at least M and not more than N times
\b \b - to include a word boundary \b at the beginning and end of the pattern.
The vertical bar/pipe -  logical OR operator, e.x. (?:com|net)+
() - Matches an optional expression
"""

# Get the .com links from a file 
with open('urls.txt','r') as file:
    content=file.read()
# think of the pattern
pattern=re.compile("https?://(?:www.)?[^ \n]+\.com") # https? - we don't have always "s", 
                                        # (?:www.)? we don't always have these characters, optional part!
                                        # [^ \n] - ignore space, carriage/space 
matches=pattern.findall(content)
print(matches)

