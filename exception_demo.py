#define fucntion
def safe_divide(a, b):
    #use try & exception to avoid error
    try:
        return a/b
    except Exception as error:
        print(error, '\"Cannot divide by zero.\"')
    #this is to execute regardless of anything
    finally:
        print("Division printed completed")

#print and invocate the function result              
print(safe_divide(3, 9))