import keyword
print(keyword.kwlist)
print(keyword.softkwlist)
print(keyword.softkwlist + keyword.kwlist)
#the command below will check if a certain word is a keyword or not
print(keyword.iskeyword("if"))