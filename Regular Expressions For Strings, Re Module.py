import re
pattern1="Is"
text1="My Name Is Mahad Shahnawaz"
print(re.search(pattern1,text1))   # "re.search" works only for 1st occurence. It will tell whether text is present or not and also it's range where it is present.
pattern2=r"[A-Z]+urricane" # It will search for just "urricane" and the starting letter should be anything b/w [A-Z].
text2='''Hurricane was the third tropical storm and first Hurricane of the 2003 Atlantic Durricane season.
A fairly long-lived July Atlantic Zurricane.'''
match=re.finditer(pattern2,text2)  # It will search till the last occurence.
for i in match:
   print(i)
# You can study further on "GOOGLE".