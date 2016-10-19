# Grab the output you get, and assign it to a string variable
L = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# Take your personal email as a second string
mail = 'andrey.lomako@homecredit.net'

# and concatenate it with L
C = (L+mail)

# Print the length of L
print('Length of L: ', len(L))

# Print the count all the vowels in L
count = 0
vowels = set("aeiouAEIOU")
for letter in L:
    if letter in vowels:
        count += 1

print ('Count of vowels in L: ', count )

# Print each 18th symbol of the string, but do it in case opposite to the original (print A if the letter is a,
# print a if A etc.) adding the position of that letter in the string in format like

u = L[::18]
print('Each 18th characters are: ', u)
print('Each 18th character in opposite case: ', u.swapcase())

#for c in u:
 #       print (u.index(c), c)

'''index = 0
for letter in L:
    if letter in
index +=1'''

position = 18
for letter in L[17::18]:
    position += 18
    if letter == '\n':
        letter = 'NEWLINE detected!!'
    print(str(position) + letter.swapcase())
