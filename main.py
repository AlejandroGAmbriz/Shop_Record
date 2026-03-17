"""This is the main module of the application."""

from classes.seller import Seller

def main():
    """
    Main function
    """
    seller = Seller()

    seller.system_loop()

if __name__ == "__main__":
    main()
