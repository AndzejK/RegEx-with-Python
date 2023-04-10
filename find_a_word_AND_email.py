import re
data=[
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com", 
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants"
]
video='.*Delhi.*[^ ]+@[^ ]+\.[a-z]+'
my='.*Delhi.*[^ ]+@[^ ]+\.[a-z]+'
the_pattern=re.compile(my,re.IGNORECASE)
email_pattern=re.compile("\\b[^ ]+@[^ ]+\.[a-z]{2,3}\\b")
pattern_word=re.compile(".*Delhi*.", re.IGNORECASE)
result=[]
for email in data:
    if (email_pattern.findall(email) and pattern_word.findall(email)):
        result.append(email)

matches=[match for match in data if the_pattern.findall(match)]

