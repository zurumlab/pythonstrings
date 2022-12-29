print("This programm calculates the area of a rectangle of any dimension and draw the rectangle for you \n")

display = ("The area of the rectangle above is {}cm² \n")

length  = input("Enter length: \n")
width = input("Enter width: \n")

if (len(length)) and (len(width)) > 0:
    l = int(length)
    w = int(width)
    s_w = "."
    e_l =" "
    for i in range(l):
        print(s_w, end="")
    for j in range(w):
        print(s_w)
        print((s_w),end=e_l*(l))
    print(" ")

    for i in range(l):
        print(s_w, end="")
    print(" ")
area = (l * w)
print(display.format(area))
