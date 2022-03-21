import pdb      # python debugger

if __name__ == '__main__':
    print(f"*** Python DeBugger ***")
    x = 1
    y = 2
    z = 'c'

    print(f"x + y {x + y}")
    pdb.set_trace()             # q to quit
    print(f"y + z {y + z}")
