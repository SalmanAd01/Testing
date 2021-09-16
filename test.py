# from dotenv import load_dotenv
import os
os.environ['TEST']='TESTING'
# load_dotenv()
user_name=os.environ.get('TOKEN')
print(user_name)
print(os.environ['TEST'])
# a file named "geek", will be opened with the reading mode.
# file = open('test1.txt', 'r')
# This will print every line one by one in the file

# Python code to illustrate split() function
with open("test1.txt", "r") as file:
    data = file.readlines()
    str1=data[0]
    str2=data[1]
    print (str1,str2)