# Quang Lam

def intpow(x, n):
    if n == 0:
        return 1
    else:
        return x * intpow(x, n - 1) 

def main():
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))
    print(intpow(x, n))

if __name__ == "__main__":
    main()