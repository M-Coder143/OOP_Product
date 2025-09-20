class Product: # Manages product information and inventory
    inventory = []
    product_counter = 0
 
    def __init__(self, product_id, name, category, quantity, price, supplier): # Initializes a new product
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
    
    @classmethod
    def add_product(cls,name, category, quantity, price, supplier): # Adds a new product to the inventory
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        Product.inventory.append(new_product)
        return "Product added successfully"
    
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None): # Updates product information
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None: 
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully" or "Product not found"
        
    @classmethod
    def delete_product(cls, product_id): # Deletes a product from the inventory
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully" or "Product not found"
      
    @classmethod
    def display_inventory(cls): # Displays the current inventory
        if not cls.inventory:
            return "Inventory is empty"
        inventory_list = []
        for product in cls.inventory:
            inventory_list.append(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Quantity: {product.quantity}, Price: {product.price}, Supplier: {product.supplier}")
        return "\n".join(inventory_list)

class Order: # Manages customer orders
    
    def __init__(self, order_id, product_id, quantity, customer_info=""): # Initializes a new order
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info
        
    def place_order(self): # Places an order if sufficient stock is available
        for product in Product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity
                    return f"Order placed successfully. Order ID: {self.order_id}"
                else:
                    return "Insufficient stock" or "Product not found"

          
print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
print(Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B"))
print(Product.display_inventory())
print("")

print(Product.update_product(1, quantity=45, price=950))
print(Product.display_inventory())
print("")

print(Product.delete_product(2))
print(Product.display_inventory())
print("")

order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())
