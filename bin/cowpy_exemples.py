from cowpy import cow

def main():

    tux = cow.Tux()  # Create a Tux cow object
    message = tux.milk("Hello from Tux!")
    print(message)
    

if __name__ == "__main__":
    main()