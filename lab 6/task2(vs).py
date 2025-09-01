def print_multiples_forloop(num):
    for i in range(1, 11):
        print(i * num)
def print_multiples_whileloop(num): 
    i = 1
    while i <= 10:
        print(i * num)
        i += 1  
print("for loop:")
print_multiples_forloop(10)
print("while loop:")
print_multiples_whileloop(10)