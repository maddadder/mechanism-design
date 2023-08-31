class Buyer:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.bid = 0
        self.winner = False
        self.pay_price = 0  # Added this line to initialize pay_price

class Product:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.current_price = base_price

def main():
    # Step 1: Get product's base price and buyers' initial bids
    product_base_price = float(input("Enter the base price of the product: "))
    buyer_t_initial_bid = float(input("Enter initial bid for Buyer T: "))
    buyer_u_initial_bid = float(input("Enter initial bid for Buyer U: "))
    
    # Step 2: Create buyers and products
    buyer_t = Buyer("Buyer T", buyer_t_initial_bid)
    buyer_u = Buyer("Buyer U", buyer_u_initial_bid)
    
    product_p = Product("Product P", product_base_price)
    
    buyers = [buyer_t, buyer_u]
    
    # Step 3: Simulate auction
    for round in range(1, 3):  # Assuming two rounds
        for buyer in buyers:
            if round == 1:
                buyer.bid = float(input(f"{buyer.name}, enter your bid for round {round}: "))
            else:
                min_bid = max(buyer.bid, product_base_price)
                buyer.bid = float(input(f"{buyer.name}, enter your bid for round {round} (must be at least ${min_bid}): "))
        
        highest_bidder = max(buyers, key=lambda x: x.bid)
        second_highest_bidder = max(filter(lambda x: x != highest_bidder, buyers), key=lambda x: x.bid)
        
        for buyer in buyers:
            if buyer == highest_bidder:
                buyer.winner = True
                buyer.pay_price = second_highest_bidder.bid
            else:
                buyer.winner = False
        
        if round == 1:
            print(f"Round {round}:")
            for buyer in buyers:
                print(f"{buyer.name} bids ${buyer.bid}")
        
        if round == 2:
            print(f"Round {round}:")
            for buyer in buyers:
                print(f"{buyer.name} bids ${buyer.bid}, wins: {buyer.winner}, pays: ${buyer.pay_price}")
    
    # Step 4: Update prices based on winners
    for buyer in buyers:
        if buyer.winner:
            product_p.current_price = buyer.pay_price
    
    print(f"{product_p.name} price updated to ${product_p.current_price}")

if __name__ == "__main__":
    main()
