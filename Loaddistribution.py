def main(): 
    Load = float(input("Enter Load(N/m): ")) 
    Length = float(input("Enter Length (m): "))
    
    Force = (Load) * (Length)
     
    print(f"So, the total load acting on the beam is {Force:,.2F} N. ") 
     
if __name__ == "__main__": 
    main() 