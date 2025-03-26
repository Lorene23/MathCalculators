def main(): 
    Length = float(input("Enter length of sidewalk in (m): ")) 
    Width = float(input("Enter width of sidewalk in (m): ")) 
    Depth = float(input("Enter depth of sidewalk in (m):: ")) 
    
    Volume = (Length) * (Width) * (Depth)
     
    print(f"So, you need {Volume:,.2f} cubic meters of concrete.") 
     
if __name__ == "__main__": 
    main() 