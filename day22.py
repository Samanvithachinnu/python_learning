# 1. Without exception handling
# Uncomment to test ZeroDivisionError
# print('1')
# print('2')
# a = 4 / 0
# print('3')
# print('4')


# 2. Exception handling using try and except
print("Example 1: try and except")

print('1')
print('2')

try:
    a = 4 / 0
except ZeroDivisionError:
    print("Message: Zero Division Error has occurred")

print('3')
print('4')


# 3. Runtime errors and multiple except blocks
print("\nExample 2: Runtime Errors")

try:
    print("Examples of runtime errors")

    x = 10 / 0
    print(y)
    a = [1, 2, 3]
    print(a[5])
    d = {"a": 1}
    print(d["b"])
    int("abc")
    print("a" + 10)
    import abcdef

except ZeroDivisionError:
    print("Zero Division Error")

except IndexError:
    print("Index Error")

except KeyError as ke:
    print("Key Error:", ke)

except ValueError:
    print("Value Error")

except TypeError:
    print("Type Error")

except ModuleNotFoundError:
    print("Module Not Found Error")

except Exception as e:
    print("Other Error:", e)


# 4. Handling unmatched exceptions
print("\nExample 3: Unhandled Exception")

try:
    a = 10 / 0

except IndexError:
    print("Index Error")

except ModuleNotFoundError:
    print("Module Not Found Error")

except ZeroDivisionError:
    print("Zero Division Error")

print("Program continues")


# 5. Using else and finally when no exception occurs
print("\nExample 4: Else and Finally")

try:
    a = 10 / 4
    print("Result:", a)

except ZeroDivisionError:
    print("Zero Division Error")

else:
    print("No exception occurred")

finally:
    print("Finally block executed")


# 6. Using else and finally when an exception occurs
print("\nExample 5: Exception with Finally")

try:
    a = 10 / 0

except ZeroDivisionError:
    print("Zero Division Error")

else:
    print("No exception occurred")

finally:
    print("Finally block executed")


# 7. Finally executes even when the exception is not handled
print("\nExample 6: Finally Block")

try:
    a = 10 / 0

except IndexError:
    print("Index Error")

except ModuleNotFoundError:
    print("Module Not Found Error")

finally:
    print("Finally block executed")

# The following line is reached only if the exception
# was handled or the exception does not occur.
# print("Program continues")


# 8. Parent and child exception classes
print("\nExample 7: Exception Hierarchy")

try:
    10 % 0

except ZeroDivisionError:
    print("Zero Division Error")

except ArithmeticError:
    print("Arithmetic Error")


# 9. User-defined exception: StudentAlreadyExists
print("\nExample 8: Simple User-Defined Exception")


class StudentAlreadyExists(Exception):
    pass


try:
    raise StudentAlreadyExists(
        "Student with roll number 23 already exists"
    )

except StudentAlreadyExists as e:
    print(e)


# 10. Parameterized user-defined exception
print("\nExample 9: Parameterized User-Defined Exception")


class StudentNotFound(Exception):

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

        super().__init__(
            f"Student roll number: {rollno} "
            f"with name {name} is not found"
        )


try:
    raise StudentNotFound(1, "rakesh")

except StudentNotFound as snf:
    print(snf)
    print("Roll Number:", snf.rollno)
    print("Student Name:", snf.name)


print("\nProgram completed successfully")