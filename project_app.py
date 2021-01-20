# Function definitions
def main_menu():
    choice = int(input("\nEnter '0' to exit. \nEnter '1' to show the product menu... "))
    file = open("products.txt","r")
    products = file.read()
    if choice == 0:
        exit()
    
    elif choice == 1:
        product_menu()


def product_menu():
    choice = int(input("\nEnter '0' to return to main menu \nEnter '1' to print out the products\nEnter '2' to create new product\nEnter '3' to update a product\nEnter '4' to delete a product... \n"))
    if choice == 0:
        main_menu()
        
    elif choice == 1:
        show_products() 
        product_menu()
        
    elif choice == 2:
        new_product()
        product_menu()
        
    elif choice == 3:
        update_product()
        product_menu()
        
        
    elif choice == 4:
        delete_product()
        product_menu()


def new_product():
    with open("products.txt","a") as products:
        products.write(input("\nEnter a new product to add to the list ")+"\n")


def show_products():
    with open("products.txt","r") as products:
        print(products.read())


def update_product():
    show_products()
    product_list = list(open("products.txt","r").readlines())
    temp_list = []
    
    for row in product_list:
        temp_list.append(row.strip())
    print(temp_list)
    product_to_change = input("\nEnter the product to update ")
    new_product = input("\nEnter the new product ")
    for row in temp_list:
        print(row)
        if row == product_to_change:
            index = temp_list.index(row)
            temp_list[index] = new_product
            
    print(temp_list)
    with open("products.txt","w") as products:
        for item in temp_list:
            products.write(item + "\n")


def delete_product():
    # index = int(input("\nSelect the index of a product to delete "))
    # del products[index]
    show_products()
    product_list = list(open("products.txt","r").readlines())
    temp_list = []
    
    for row in product_list:
        temp_list.append(row.strip())
    print(temp_list)
    product_to_delete = input("\nEnter the product to delete ")
    for row in temp_list:
        print(row)
        if row == product_to_delete:
            index = temp_list.index(row)
            del temp_list[index] 
            
    print(temp_list)
    with open("products.txt","w") as products:
        for item in temp_list:
            products.write(item + "\n")


# Main code
main_menu()
