# (c) 2025 Full Name 
# A simple store calculator using functions. 
 
def get_payment(cost): 
    payment = float(input("Enter payment: ")) 
    if payment < cost: 
        return get_payment(cost) 
     
    return payment 
 
def main(): 
    item1 = float(input("Enter price for item #1: ")) 
    item2 = float(input("Enter price for item #2: ")) 
    item3 = float(input("Enter price for item #3: ")) 
    cost = item1 + item2 + item3 
     
    print(f"The total cost is P{cost:,.2f} only.") 
     
    payment = get_payment(cost) 
    change = payment - cost 
    print(f"Your change is P{change:,.2f}.") 
 
 
if __name__ == "__main__": 
    main() 