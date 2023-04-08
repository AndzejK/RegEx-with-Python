# deepnote.com
import re
some_str="Hey mate, i've got some news please write me back to this email goodnews@channel.com but don't use this badnews@channel.com email!!"
# get the emails
email_pattern=re.compile("[a-z]@[a-z].[a-z]") # thisis  a regular expression object <class 're.Pattern'>
matches=email_pattern.findall(some_str)
