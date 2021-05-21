# regular expression -important topic

import re

# r string
# print("\n") # blank
# print(r"\n") # \n

mystr="i am jerry...396510..i am leaving in village,,__" \
      "i am programmer,,it's match..oww 3576l[;'/;][;]0 ,"
pat=re.compile(r'\Z,')
matches=pat.sub(mystr)
# print(matches)
# <callable_iterator object at 0x00F4FCD0>
for match in matches:
     print(match)
# <re.Match object; span=(13, 15), match='39'>


