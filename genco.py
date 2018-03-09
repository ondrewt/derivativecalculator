def main():
    print("Welcome. This is a polynomial derivative calculator.")
    print("Specify the order, exponent, and coefficient of each term.")
    print("Note: x^0=1!  If no more terms desired, press enter.")
    polynomial=[]
    exponent=0
    coefficient=0
    while exponent!='' and coefficient!='':
        order=input("Order of derivative: ")
        exponent=input("Exponent of polynomial term: ")
        coefficient=input("Coefficient of polynomial term: ")
        if order!='':
            order=int(order)
            while order>0:
                if coefficient!='' and exponent!='':
                    coefficient=int(coefficient)
                    exponent=int(exponent)
                    coefficient=coefficient*exponent
                    exponent-=1
                    term='{0}x^{1}'.format(coefficient,exponent)
                    order-=1
            polynomial.append(term)
        else:
            print('+'.join(polynomial))
if __name__=="__main__":
    main()
