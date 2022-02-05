color_list1 = input("Enter the color list 1: ").split()
color_list2 = input("Enter the color list 2: ").split()

difference = set(color_list1) - set(color_list2)

print(difference)
