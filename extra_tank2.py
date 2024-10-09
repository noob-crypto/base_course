a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a + b < c or a + c < b or b + c < a:
    print("не существует")
elif a == b and b == c and c == a:
    print("равносторонний")
else:
    print("разносторонний ")