
from pesapal import PesapalAPI
import uuid

def main():
    # Initialize PesapalAPI
    pesapal = PesapalAPI()
    
    # Example payment details
    phone = "254712345678"  # Replace with actual phone number
    bid_amount = 100.00
    order_id = str(uuid.uuid4())  # Generate unique order ID
    fname = "John"
    lname = "Doe"
    
    # Initiate payment
    result = pesapal.initiate_payment(phone, bid_amount, order_id, fname, lname)
    
    if result:
        print("Payment initiated successfully:")
        print(result)
    else:
        print("Failed to initiate payment")

if __name__ == "__main__":
    main()
