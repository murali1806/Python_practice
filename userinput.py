##input while triggering the job
## Save this in a separate Python file and give "python userinput.py Murali" in the terminal
import sys 
name = sys.argv[1]


##format the name 
email= name.lower().replace(" ",".")+"@gmail.com"

print("\n--profile--")
print("full name:",name)
print("email:",email)

##lastname=sys.argv[2] ## if 2 sys defined, we need to give 2 inputs in the terminal, else query fails then give this "python userinput.py Murali km" 

##input murali 1 2 3
##name = sys.argv[1]  
##print(name) --> ['murali', '1', '2', '3']
##if you need in a single statement
##name =" ".join(sys.argv[1:])
##print(name) --> [murali 1 2 3]