def main(): 
    C2 = int(input("Enter Final Cement Concentration in (g/L): ")) 
    C1 = int(input("Enter Initial Cement Concentration: in (g/L): ")) 
    V2 = int(input("Enter Final Volume (L): ")) 
    
    V1 = ((C2)*(V2))/(C1)
     
    print(f"So, you need {V1:,.2f} liters of the original slurry.") 
     
if __name__ == "__main__": 
    main() 