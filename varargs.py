import operator

def multiply(*args):
    val = 1
    
    for i in map(int, args):
        val *= i

    return val

if __name__ == "__main__":
    import sys
    print sys.argv[0]
    
    print multiply(*sys.argv[1:])
