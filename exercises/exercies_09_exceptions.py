try:
    number = int(input("Give a number between 0 - 10 > "))
    result = 100 / number
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)
finally:
    print("Done")


"""
try → everything that can fail
except → what to do when an error occurs
else → what to do if everything went well
finally → what must always happen
"""
