class Item:
    id=1
    def __init__(self,name,price,quantity=1):
        self.__name=name
        self.__price=price
        self.__quantity=quantity
        self.__id=Item.id
        Item.id+=1
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity
    def get_id(self):
        return self.__id
    def set_name(self,new_name):
        self.__name=new_name
    def set_price(self,newprice):
         self.__price=newprice
    def set_quantity(self,newquantity):
         self.__quantity=newquantity
    def increment_quantity(self):
        self.__quantity+=1
    def get_info(self):
        return (f"{self.__name} id is {self.__id} it's quantity is {self.__quantity} and its price is {self.__price}")
    def sell_quant(self,amount):
        self.amount=amount
        self.__quantity-=self.amount
   

class Seller:

    def __init__(self,name,email,maxitems,items:list[Item]):
        self.__name=name
        self.__maxitems=maxitems
        self.__items=items
        self.__email=email

    def info(self):
        print(f"Seller name is {self.__name}, his email is {self.__email}, his maximum capacity is {self.__maxitems}")
    def add_item(self,item:Item):
        self.item=item
        mwgod=True
        for i in range(len(self.__items)):
            if(self.item==self.__items[i]):
                mwgod=False
                self.__items[i].increment_quantity()
                print("Item's quantity has increased")
        if(mwgod and (len(self.__items)<=self.__maxitems-1)):
            self.__items.append(self.item)
            print("Item has been added succesfully")
        else:
            if(mwgod):
                print("You have reached your max cant add that item")

    def print(self):
        z=True
        for i in range(len(self.__items)):
           print(self.__items[i].get_info())
           z=False
        if(z):
            print('NONE')

    def find_item_byname(self,name):
        self.itemname=name
        for i in range(len(self.__items)):
            if self.__items[i].get_name()==self.itemname:
                return self.__items[i]
    
    def sell_item(self,itemname,itemquant):
        self.itemname=itemname
        self.itemquant=itemquant
        item=self.find_item_byname(self.itemname)
        if self.itemquant>item.get_quantity():
            print(f"There is only {item.get_quantity()} left for this item")
        else:
            item.sell_quant(self.itemquant)
            if item.get_quantity()==0:
                self.__items.remove(item)

    def find_by_id(self,id):
        self.id=id
        for i in range(len(self.__items)):
            if(self.__items[i].get_id()==self.id):
                print( self.__items[i].get_info())
                break
            elif i==len(self.__items)-1:
                print("No such item with this id")
    def show_items_for_sell(self):
        if len(self.__items)>0:
            print("choose an item to sell:")
            for i in range(len(self.__items)):
                print(int(i+1),'.',self.__items[i].get_name())
            x=int(input())
            return self.__items[x-1].get_name()
        else:
            print('no enough items')
            

    


        
