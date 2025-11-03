class Product:
    def __init__(self, product_id, name, price, stock, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def add_stock(self, amount):
        if amount > 0:
            self.stock += amount
        else:
            print("Enter valid amount")

    def reduce_stock(self, amount):
        if amount <= 0:
            print("Enter a valid amount to reduce")
        elif amount > self.stock:
            print("Not enough stock available")
        else:
            self.stock -= amount

    def apply_discount(self, percentage):
        if 0 < percentage < 100:
            discount = self.price * (percentage / 100)
            self.price -= discount

    @property
    def is_available(self):
        return self.stock > 0

    def __str__(self):
        return f"{self.name} ({self.product_id}) - ${self.price:.2f} - Stock: {self.stock}"

    def __repr__(self):
        return f"Product({self.product_id!r}, {self.name!r}, {self.price!r}, {self.stock!r}, {self.category!r})"

    def __eq__(self, other):
        return isinstance(other, Product) and self.product_id == other.product_id

    def __hash__(self):
        return hash(self.product_id)

class Review:
    def __init__(self, user , rating, comment):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        
        self.user = user
        self.rating = rating
        self.comment = comment
    
    def is_positive(self):
        return self.rating >= 4

class ProductWithReviews(Product):
    def __init__(self, product_id, name, price, stock, category, reviews_list=None):
        super().__init__(product_id, name, price, stock, category)
        self.reviews_list = reviews_list if reviews_list is not None else []
    
    def add_review(self, review):
        self.reviews_list.append(review)
    
    def average_rating(self):
        if not self.reviews_list:
            return 0
        total = sum(review.rating for review in self.reviews_list)
        return total / len(self.reviews_list)
    
    def get_review_summary(self):
        if not self.reviews_list:
            return "No reviews yet."

        total_reviews = len(self.reviews_list)
        avg = self.average_rating()
        positive_count = sum(1 for r in self.reviews_list if r.is_positive())
        return f"{total_reviews} reviews - Average: {avg:.1f}/5 - {positive_count} positive"

class ShoppingCart:
    def __init__(self):
        self.items = {}
        
    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    
    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
    
    def update_quantity(self, product, quantity):
        if quantity <= 0:
            self.remove_item(product)
        elif product in self.items:
            self.items[product] = quantity
        else:
            print("Product not found in cart.")
    
    def get_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    
    def clear(self):
        self.items.clear()
        
    def __len__(self):
        return sum(self.items.values())

# Create products
laptop = ProductWithReviews("P001", "Gaming Laptop", 1200, 10, "Electronics")
mouse = ProductWithReviews("P002", "Wireless Mouse", 25, 50, "Accessories")
print(laptop)

# Check availability
print(f"Laptop available: {laptop.is_available}")

# Add reviews
laptop.add_review(Review("Alice", 5, "Excellent laptop!"))
laptop.add_review(Review("Bob", 4, "Great performance"))
laptop.add_review(Review("Charlie", 3, "Good but expensive"))

print(f"Average rating: {laptop.average_rating():.2f}")

print(laptop.get_review_summary())

# Shopping cart
cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
print(f"Cart size: {len(cart)}")

print(f"Cart total: ${cart.get_total()}")

# Apply discount
laptop.apply_discount(10)
print(f"Discounted price: ${laptop.price}")

print(f"New cart total: ${cart.get_total()}")

# Reduce stock when purchasing
for product, quantity in cart.items.items():
    product.reduce_stock(quantity)
print(f"Laptop stock after purchase: {laptop.stock}")

# Test equality
laptop2 = ProductWithReviews("P001", "Gaming Laptop", 1200, 10, "Electronics")
print(f"laptop == laptop2: {laptop == laptop2}")