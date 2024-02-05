import re

text = "The rain in Spain"

# Find all the lowercase letters alphabetically between "a" and "m"
a = re.findall("[a-n]", text)
print(a)

text2="Bangladesh Is bautifuL"
pattern="[a-z]"
b= re.findall(pattern,text2)
print(b)

text3="I am Going to bandarban in 7 th feb"
pattern="7"
c=re.findall(pattern,text3)
print(c)

text4="7 th feb is my date to go to bandarban"#starts with use ^ no need for others words
pattern="^7"
d=re.findall(pattern,text4)
print(d)

text5="I am Going to bandarban in 7 th feb"
pattern="7"
f=re.findall(pattern,text3)
if f:
     print("yes,7 is special character")
else:
    print("No,1 is not special character")

text6="7 th feb is my date to go to bandarban"
pattern="^7"
g=re.findall(pattern,text6)
if g:
     print("yes,7 is special character")
else:
    print("No,1 is not special character")
###########################

    # Search the string to see if it starts with "The" and ends with "Spain"
txt="The train in Rajshahi"
x=re.search("^The.*Rajshahi$",txt) #stars with ^The,ends with Rajshahi$
print(x)
if x:
    print("Yes!We have a Match")
else:
    print("No match")

##################################

#	Signals a special sequence (can also be used to escape special characters
txt1="That will be 59 dollars"

y=re.findall("\d",txt1)
print (y)

#####################################
txt44 = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
#*	Zero or more occurrences	"he.*o"
ee = re.findall("he.*o", txt44)

print(ee)

########################################
# +	One or more occurrences	"he.+o"

txt33="hello planet"

xx=re.findall("he.+o",txt33)
print(xx)

########################################
# ?	Zero or one occurrences	"he.?o"
txt = "hello planet"
x = re.findall("he.?o", txt)

print(x)

####################################

# {}	Exactly the specified number of occurrences	"he.{2}o"
txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)


####################################
# |	Either or	"falls|stays"

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
