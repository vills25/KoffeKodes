class Cart():
    def __init__(self):
        self.products = {} # store products in dictnory

    def add_product(self, product_name, product_id, quantity=1): # Quantity by default 1
        if product_id in self.products:
            self.products[product_id]['quantity'] += quantity # increment quantity
        else:
            self.products[product_id] = {"Product name": product_name, "Quantity": quantity}
            
    # def edit_product(self):

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found")

    def view_cart(self):
        for product_id, product in self.products.items():
            print(f"Product name: {product['product_name']}, Product ID: {product_id}, Quantity: {product['quantity']}")

    def get_product(self, product_id):
        return self.products.get(product_id)
    
    def clear_cart(self):
        self.products.clear()

    def main():
        cart = Cart()
        while True:
            print("1. Add Product: ")
            print("2. Edit Product: ")
            print("3. Delete Product: ")
            print("4. view Cart: ")
            print("5. Search Product: ")
            print("6. Clear cart: ")
            print("7. Place Order: ")
            print("8. Exit: ")

            choice = input("Enter number: ")
            if choice == "1":
                product_id = input("enter Product ID: ")
                product_name = input("Enter Product Name: ")
                quantity = input("enter Product Quantity: ")
                cart.add_product(product_id, product_name, quantity)
            elif choice == "2":
                product_id = input("enter Product ID: ")
                product_name = input("Enter NEW Product Name: ")
                quantity = input("enter NEW Product Quantity: ")
                cart.edit_product(product_id, product_name, quantity)
                
                

