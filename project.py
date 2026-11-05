class User:
    def __init__(self,id,name,password,isadmin):
        self.id=id
        self.name=name
        self.password=password
        self.isadmin=isadmin

    def user_details(self):
        return f"{self.id},{self.name},{self.password},{self.isadmin}\n"

class Auth:
    def registration(self):
        id=input("enter your user id:")
        name=input("enter your user name: ")
        password=input("enter your user password:")
        isadmin=input("enter Yes if you are admin else enter No:")
        new_user=User(id,name,password,isadmin)

        with open("users.txt","r") as file:
            lines=file.readlines()

            is_found=False
            for line in lines:
                details=line.strip().split(",")
                if details[1]==name:
                    is_found=True
                    break

            if is_found:
                print("user already exist.")
            else:
                with open("users.txt","a") as file:
                    file.write(new_user.user_details())

    def login(self):
        name=input("enter your user name for login: ")
        password=input("enter your password for login: ")

        with open("users.txt","r") as file:
            lines=file.readlines()

            is_found=False
            userid=None
            isadmin=None
            for line in lines:
                line=line.strip().split(",")
                if line[1]==name:
                    if line[2]==password:
                        is_found=True
                        isadmin=line[-1]
                        userid=line[0]
                        break

            if is_found:
                print("login successful.")
                return [userid,isadmin]
            else:
                print("Invalid Credentails.")


class Item:
    def __init__(self,id,item_name,price):
        self.id=id
        self.item_name=item_name
        self.price=price
        self.quantity=1

    def item_details(self):
        return f"{self.id},{self.item_name},{self.price},{self.quantity}\n"


class ItemsHandling:
    def add_item(self):
        id=input("enter Item id: ")
        item_name=input("enter Item name: ")
        price=input("enter Item price: ")
        new_item=Item(id,item_name,price)

        with open("items.txt","r") as file:
            lines=file.readlines()

            is_found=False
            for line in lines:
                details=line.strip().split(",")
                if details[1]==item_name:
                        is_found=True
                        break

            if is_found:
                with open("items.txt","w") as file:
                    for line in lines:
                        details=line.strip().split(",")
                        if details[1]==item_name:
                                q=int(details[3])+1
                                file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                        else:
                            file.write(line)
            else:
                with open("items.txt","a") as file:
                    file.write(new_item.item_details()+"\n")


    def decrease_quantity(self):
        item_name=input("enter the Item name to decrease quantity: ")
        with open("items.txt","r") as file:
            lines=file.readlines()

        is_found=False
        for line in lines:
            details=line.strip().split(",")
            if details[1]==item_name:
                is_found=True
                break

        if is_found:
            with open("items.txt","w") as file:
                for line in lines:
                    details=line.strip().split(",")
                    if details[1]==item_name:
                        if int(details[3])>1:
                            q=int(details[3])-1
                            file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                    else:
                        file.write(line)
        else:
            print("item not found.")


    def delete_item(self):
        item_name=input("enter the Item name to delete:")
        with open("items.txt","r") as file:
            lines=file.readlines()
        is_found=False
        for line in lines:
            details=line.strip().split(",")
            if details[1]==item_name:
                is_found=True

        if is_found:
            with open("items.txt","w") as file:
                for line in lines:
                    details=line.strip().split(",")
                    if details[1]!=item_name:
                        file.write(line)
        else:
            print("Item not found.")


    def update_item(self):
        id=input("enter Item ID to update:")
        with open("items.txt","r") as file:
            lines=file.readlines()

        is_found=False
        for line in lines:
            details=line.strip().split(",")
            if details[0]==id:
                is_found=True

        if is_found:
            with open("items.txt","w") as file:
                for line in lines:
                    details=line.strip().split(",")
                    if details[0]==id:
                        item_name=input(f"update {details[1]} to : ")
                        price=input(f"update {details[2]} to : ")
                        file.write(f"{details[0]},{item_name},{price},{details[3]}\n")
                    else:
                        file.write(line)

        else:
            print("Item not found.")


    def view_items(self):
        with open("items.txt","r") as file:
            lines=file.readlines()
            print("------------------------------------------------------")
            print("| id   | name                | price     | quantity  |")
            print("------------------------------------------------------")
            for line in lines:
                details=line.strip().split(",")
                print(f"|{details[0]+(" ")*(5-len(details[0]))} |{details[1]+(" ")*(20-len(details[1]))} |{details[2]+(" ")*(10-len(details[2]))} |{details[3]+(" ")*(10-len(details[3]))} |")
            print("------------------------------------------------------")


class Cart(ItemsHandling):
    def __init__(self,userid):
        self.userid=userid

    def add_to_cart(self):
        item_name=input("enter Item name: ")
        with open("items.txt","r") as file:
            lines=file.readlines()

            is_found=False
            new_item=None
            with open("items.txt","w") as file:
                for line in lines:
                    details=line.strip().split(",")
                    if details[1]==item_name and int(details[-1])>0:
                        is_found=True
                        new_item=details
                        q=int(details[3])-1
                        file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                    else:
                        file.write(line)

            if is_found:
                with open("cart.txt","r") as file:
                    lines=file.readlines()

                is_found=False
                with open("cart.txt","w") as file:
                    for line in lines:
                        details=line.strip().split(",")
                        if details[2]==item_name and self.userid==details[0]:
                            is_found=True
                            q=int(details[-1])+1
                            file.write(f"{details[0]},{details[1]},{details[2]},{details[3]},{q}\n")
                        else:
                            file.write(line)

                if is_found==False:
                    new_item[-1]="1"
                    new_item.insert(0,self.userid)
                    with open("cart.txt","a") as file:
                        file.write(",".join(new_item)+"\n")

            else:
                print("Out of stock.")


    def decrease_cart(self):
        item_name=input("enter Item name: ")
        with open("cart.txt","r") as file:
            lines=file.readlines()

            is_found=False
            with open("cart.txt","w") as file:
                for line in lines:
                    details=line.strip().split(",")
                    if details[2]==item_name and details[0]==self.userid:
                            is_found=True
                            if int(details[-1])>1:
                                q=int(details[-1])-1
                                file.write(f"{details[0]},{details[1]},{details[2]},{details[3]},{q}\n")
                    else:
                        file.write(line)

            if is_found:
                with open("items.txt","r") as file:
                    lines=file.readlines()

                    is_found=False
                    with open("items.txt","w") as file:
                        for line in lines:
                            details=line.strip().split(",")
                            if details[1]==item_name:
                                q=int(details[3])+1
                                file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                            else:
                                file.write(line)


    def delete_item_in_cart(self):
        item_name=input("enter Item name: ")

        with open("cart.txt","r") as file:
            lines=file.readlines()

        is_found=False
        with open("cart.txt","w") as file:
            for line in lines:
                details=line.strip().split(",")
                if details[2]==item_name and details[0]==self.userid:
                    is_found=True
                else:
                    file.write(line)

        if is_found:
            print("Item deleted.")

        else:
            print("Item not found in cart.")


    def view_cart(self):
        with open("cart.txt","r") as file:
            lines=file.readlines()
            print("-----------------------------------------------")
            print("| name                | price     | quantity  |")
            print("-----------------------------------------------")
            total=0
            for line in lines:
                details=line.strip().split(",")
                if details[0]==self.userid:
                    total+=int(details[3])*int(details[-1])
                    print(f"| {details[2]+(" ")*(20-len(details[2]))}| {details[3]+(" ")*(10-len(details[3]))}| {details[4]+(" ")*(10-len(details[4]))}|")
            print("-----------------------------------------------")
            print("|           total=",total,"                   |")
            print("-----------------------------------------------")

def admin():
    while True:
        print("1) Add Item.")
        print("2) Decrease Item quantity.")
        print("3) update Item.")
        print("4) Delete Item.")
        print("5) View Items.")
        print("6) Exit")
        opt=input("choose one option: ")
        h=ItemsHandling()
        if opt=="1":
            h.add_item()
        elif opt=="2":
            h.decrease_quantity()
        elif opt=="3":
            h.update_item()
        elif opt=="4":
            h.delete_item()
        elif opt=="5":
            h.view_items()
        elif opt=="6":
            break
        else:
            print("choose valid option.")


def user(userid):
    while True:
        print("1) View Items.")
        print("2) Add Item to cart.")
        print("3) Decrease qunatity in cart.")
        print("4) Delete Item in cart.")
        print("5) View Items in cart.")
        print("6) Exit.")
        opt=input("choose one option: ")
        c=Cart(userid)
        if opt=="1":
            c.view_items()
        elif opt=="2":
            c.add_to_cart()
        elif opt=="3":
            c.decrease_cart()
        elif opt=="4":
            c.delete_item_in_cart()
        elif opt=="5":
            c.view_cart()
        elif opt=="6":
            break
        else:
            print("choose valid option.")


def run():
    while True:
        print("1) register")
        print("2) login")
        print("3) exit")
        opt=input("choose one option: ")
        a=Auth()
        if opt=="1":
            a.registration()
        elif opt=="2":
            res=a.login()
            if res[-1]=="yes":
                admin()
            else:
                user(res[0])
        elif opt=="3":
            print("Thanks for visiting.")
            break
        else:
            print("choose valid option.")

run()