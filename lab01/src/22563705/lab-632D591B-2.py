def getDiscount( day, amount ) :
    amountAfterDiscount = 0
    # START: Write your code here
    if day is "Monday":
        amountAfterDiscount = (amount/100) * 0.9
    else:
        if day is  "Tueaday":
            amountAfterDiscount = (amount/100) * 0.95
        else:
            amountAfterDiscount = (amount / 100) * 0.99
    # END: Write you code here
    return amountAfterDiscount

def main():
    day = input("Enter the current day: ")
    amount = int(input("Enter the invoice amount: ")) 
    amountAfterDiscount = getDiscount(day, amount)
    print("Final amount is: {}".format(amountAfterDiscount) )

if __name__ == "__main__":
    main()