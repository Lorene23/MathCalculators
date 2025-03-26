def main(): 
    rise = float(input("Enter the rise of the road in (m): ")) 
    run = float(input("Enter horizontal distance of the road in (m): "))
    
    slope = (rise/run) * 100
     
    print(f"So, the slope of the road is {slope:,.2F} %. ") 
     
if __name__ == "__main__": 
    main() 