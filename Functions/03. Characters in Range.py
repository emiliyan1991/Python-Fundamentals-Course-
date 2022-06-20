def characters(n1, n2):
    for num in range(ord(n1)+1, ord(n2)):
        print(chr(num), end=" ")


n1, n2 = input(), input()
characters(n1, n2)



