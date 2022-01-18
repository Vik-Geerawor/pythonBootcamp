import sys

print("*** Size of Data types ***")

a: int = 2
print("\nNumber " + str(a) + ": " + str(sys.getsizeof(a)) + " bytes")
a = 2 * 10 ** 30
print("Number " + str(a) + ": " + str(sys.getsizeof(a)) + " bytes")

b: float = 10.0
print("\nNumber " + str(b) + ": " + str(sys.getsizeof(b)) + " bytes")
b = 2.0 * 10 ** 30
print("Number " + str(b) + ": " + str(sys.getsizeof(b)) + " bytes")

flag: bool = True
print("\nBool " + str(flag) + ": " + str(sys.getsizeof(flag)) + " bytes")
flag = False
print("Bool " + str(flag) + ": " + str(sys.getsizeof(flag)) + " bytes")


c: str = ""
print("\nString [empty] " + c + ": " + str(sys.getsizeof(c)) + " bytes")
c = "abc"
print("String " + c + ": " + str(sys.getsizeof(c)) + " bytes")


