"""Demo CLI for the `calc` module.

Usage examples:
  python main.py add 3 4
  python main.py sub 10 7
  python main.py demo
"""
import sys
from calc import create, add, subtract, multiply, divide

def usage():
    print("Usage:")
    print("  python main.py add 3 4")
    print("  python main.py sub 10 7")
    print("  python main.py demo")

def main(argv):
    if len(argv) < 2:
        usage()
        return 1
    cmd = argv[1]
    try:
        if cmd == "add" and len(argv) >= 4:
            a = float(argv[2]); b = float(argv[3])
            print(add(create(a), create(b)))
        elif cmd in ("sub", "subtract") and len(argv) >=4:
            a = float(argv[2]); b = float(argv[3])
            print(subtract(create(a), create(b)))
        elif cmd in ("mul", "multiply") and len(argv) >=4:
            a = float(argv[2]); b = float(argv[3])
            print(multiply(create(a), create(b)))
        elif cmd in ("div", "divide") and len(argv) >=4:
            a = float(argv[2]); b = float(argv[3])
            print(divide(create(a), create(b)))
        elif cmd == "demo":
            print("Demo:")
            print("  add(1,2) ->", add(create(1), create(2)))
            print("  subtract(5,3) ->", subtract(create(5), create(3)))
            print("  multiply(3,4) ->", multiply(create(3), create(4)))
            print("  divide(10,2) ->", divide(create(10), create(2)))
        else:
            usage()
            return 1
    except ValueError:
        print("Error: numeric arguments required")
        return 2
    except ZeroDivisionError as e:
        print("Math error:", e)
        return 4
    except TypeError as e:
        print("Type error:", e)
        return 3
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
