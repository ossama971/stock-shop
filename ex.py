from maain import Item, Seller
item1=Item('juice',5)
item2=Item('apple',8)
item3=Item('tmatm',3)
item4=Item('chips',10)
name=input("Please enter you name: ")
email=input("Please enter you email: ")
maxcap=int(input("Please enter you maximum capacity: "))
person=Seller(name,email,maxcap,[])
x=True
while x==True:
    n=int(input("Please select from the menu below : \
        1. Print My Info. \
        2. Add An Item.\
        3. Sell An Item.\
        4. Print Items.\
        5. Find an Item by ID\
        6. Exit    "))

    if n==1:
        person.info()
    elif n==2:
        new=int(input("please select an item from the menu:\
            1-Juice\
            2-apple\
            3-tmatm\
            4-chips         "))
        if new==1:
            new=item1
        elif new==2:
            new=item2
        elif new==3:
            new=item3
        elif new==4:
            new=item4
        person.add_item(new)
    elif n==3:
        person.sell_item(person.show_items_for_sell(),int(input("Enter the quantity:   ")))
    elif n==4:
        person.print()
    elif n==5:
        person.find_by_id(int(input("Please enter the ID of the item you want to search for       ")))
    elif n==6:
        x=False
        
    
