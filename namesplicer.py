# slicing is when u create a substring after extracting it from another string 
#           slice() or index[]
#                      [start:stop:step]

string = "Ana conda"
new_string = string[0:4]
# 0 is the first letter and 4 is the space
newer_string = string[4:]
# 4 is the space character and everything after is printed regardless
funky_string = string[::2]
# 2 is an interval of the letter that is printed it is every other letter
reversed_string = string[::-1]
# the -1 interval will reverse the string
print(new_string)
print(newer_string)
print(funky_string)
print(reversed_string)

website = "http://www.wikipedia.com"
slice = slice(11,-4)
print(website[slice])