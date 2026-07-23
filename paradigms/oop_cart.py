class Product:
    def __init__(self, name, unit_price, quantity):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

        class Cart:
            def __init__(self):
                self.products = []

                def add_product(self, product):

                    self.produts.append(product)

                    def get_total(self):
                        total = 0

                        for product in self.products:
                            total += product.unit_price *
                            product.quantity

                            return total

                        def apply_discount(self):
                            total = self.get_total()

                            if total > 50000:
                                total = total * 0.9

                                return total

                            #Create a cart object
                            cart = cart()

                            # Add products to the cart
                            cart.add_product(Product("Rice", 12000, 2))
                            cart.add_product(Product("Oil", 8000, 1))
                            cart.add_product(Product("Sugar", 5000, 3))

                            #Display final price
                            print("Final price:",
                                  cart.apply_discount(), "FCFA")