def tester(givenstring):
    if givenstring == "quit":
        quit()
    elif len(givenstring) < 10:
        return False
    else:
        return True

def take_input():
    take = input("Write something (quit ends): ")
    return take

def main():
    while True:
        testing = take_input()
        result = tester(testing)
        if result == False:
            print("Too short")
        if result == True:
            print(testing)
        
        

if __name__=="__main__":
    main()
