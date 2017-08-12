'''
Problem 7: Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end of the slug.

>>> make_slug("hello world")
'hello-world'
>>> make_slug("hello  world!")
'hello-world'
>>> make_slug(" --hello-  world--")
'hello-world'''

import re

def makeSlug(text):
    name = r'\w+'
    result = '-'.join(re.findall(name,text))
    return result

print(makeSlug('hello-- world!'))
    
