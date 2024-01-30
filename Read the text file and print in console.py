'''write a python function to read from a text file.
The function will take the name of the text file
and display the content of the file into the console '''

#Import date time Module

from datetime import datetime

# get current date and time
current_datetime = datetime.now().strftime("Date- %Y-%m-%d Time-%H-%M-%S")
print("Current date & time : ", current_datetime)

# create a file object along with extension
file_name = current_datetime+".txt"

#write date
file = open(file_name, 'w')
file.write(current_datetime)
print("File created : ", file_name)
file.close()

# Open and read text file
file = open("Date- 2024-01-30 Time-13-39-36.txt", 'r')
data=file.read()

#Print content of text file
print("Content in text file:" ,data)
