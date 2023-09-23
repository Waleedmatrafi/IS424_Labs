num_List = []
for i in range(10):
    print("Please enter a number")
    num = input()
    num_List.append(int(num))
num_List.sort()
print(num_List[9])