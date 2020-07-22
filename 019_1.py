import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

try:
    num = int(sys.argv[1])
    print(10/num)
except ZeroDivisionError:
    print("input not valid")
    sys.exit()
except ZeroDivisionError:
    print("0으로는 못나눠요")
    sys.exit()



