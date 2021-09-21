import os
import sys
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    args = 1
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    # print("asdasdfasdf : " + str(sys.argv[1]))
    if sys.argv[2] == "1":
        os.system('python linear.py')
    elif sys.argv[2] == "2":
        os.system('python logistic.py')
