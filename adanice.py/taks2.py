name = ["adanielle","venice","rhea","ereca","aiza"]

for get_name in name:
    print(get_name)

lastname = [["sabaria","paculba"],["paculba","cabrera"],["briones","opaon"]]


print("['sabaria','paculba'],['paculba','cabrera'],['briones','opaon']")
print("          1                     2                     3")
user = int(input("choose which array to display : "))
print()


for i in range(user):
    if user == 1:
        print(lastname[0])
    elif user == 2:
        print(lastname[1])
    elif user == 3:
        print(lastname[3])
    else:
        print("Invalid Choices")
