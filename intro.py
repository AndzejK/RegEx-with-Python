# deepnote.com
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

some_str="Hey mate, i've got some news please write me back to this email @channel.com goodnews@channel.coom goodnews@channel.com but don't use this badnews@channel.com email!!"
# get the emails, the entire expression should match! 
email_pattern=re.compile("\\b[^ ]+@[^ ]+\.[a-z]{2,3}\\b") # [^ ] match any character but not SPACE/CR 
matches=email_pattern.findall(some_str)
print(matches)