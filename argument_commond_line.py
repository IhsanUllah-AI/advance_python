import argparse
#is used to pass argument from coomond line 
if __name__=="__main__":
    perser=argparse.ArgumentParser()
    perser.add_argument("number1", help=" first number")
    perser.add_argument("number2", help="second number")
    perser.add_argument("operation", help="operation")
    args=perser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1=int(args.number1)
    n2=int(args.number2)
    result=None
    
    if args.operation=="add":
        result=n1+n2
    elif args.operation=="sub":
        result=n1-n2
    elif args.opration=="mul":
        result=n1*n2
    elif args.operation=="div":
        result=n1/n2

    print("result=",result)