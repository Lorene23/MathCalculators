def main(): 
    F = int(input("Enter the Force in (N): ")) 
    Area = int(input("Enter the Area in (mm^2): ")) 
    
    stress = F / (Area / (1000000)) 
     
    print(f"So, the stress on the beam is {stress:,.2f} Pa.") 
 
 
if __name__ == "__main__": 
    main()