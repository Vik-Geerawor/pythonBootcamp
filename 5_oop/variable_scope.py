import builtins

x = 'global x'


def func():
    x = 'local x'
    print(x)

    print(f"locals = {locals()}")


func()
print(x)

print(f"__name__ = {__name__}")
print(f"builtins attributes = {dir(builtins)}")
print(f"global dictionary = {globals()}")
