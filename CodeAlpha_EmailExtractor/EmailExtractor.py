import re 

#Read the input file

with open("input.txt","r") as file:
           text= file.read()

#Regular expression pattern for email addresses

pattern =r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#Extract all emails addresses 

emails = re.findall(pattern,text)

#Write extracted emails to a new file 

with open("emails.txt","w") as file:
 
 for email in emails:  file. write(email+"\n")

print("Email addresses extracted successfully and saved to emails.txt ")
