def safe_divide(a, b):
    try:
        return a/b
    except Exception as error:
        print(error, '\"Cannot divide by zero.\"')
    finally:
        print("Division printed completed")
              
print(safe_divide(3, 0))