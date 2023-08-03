import sys

def collatz(n):
    if (n % 2 == 0):
        n = n / 2
    else:
        n = (3 * n) + 1

    return int(n) 

def main():
    n = int(sys.argv[1])
    showSequence = 0
    if len(sys.argv) > 2:
        showSequence = int(sys.argv[2])

    for i in range(1, n + 1):
        val = collatz(i)
        if(showSequence > 0): print(val)
        while(val != 1):
            val = collatz(val)
            if(showSequence > 0): print(val)

        print(f"Collatz({i}): TRUE")

    print("All done! <3")

main()