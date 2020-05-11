class PaymentGateway:
    def __init__(self):

        self.valid_transactions = ["auth", "capture", "sale"]
        self.valid_credit_cards = ["4111111111111111", "5431111111111111", "6011601160116611"]
        self.lowest_amount = 1.00
        self.highest_amount = 150000.00

    def is_transaction_type_valid(self, transaction_type):

        if transaction_type not in self.valid_transactions:
            return {"error": 500, "message": "Esto no es una transaccion permitida"}

    def is_credit_card_valid(self, credit_card):
        if credit_card[0] not in ["4", "5", "6"]:
            return {"error": 500, "message": "Esto no es una tarjeta permitida"}

        if credit_card not in self.valid_credit_cards:
            return {"error": 500, "message": "Esto no es una tarjeta valida"}

    def is_transaction_amount_valid(self, amount):
        if amount < self.lowest_amount or amount > self.highest_amount:
            return {"error": 500, "message": "Esto no es un monto permitido"}

    def do_sale(self, amount, transaction_type, credit_card):

        # First, let me validate your information
        is_valid_transaction_type = self.is_transaction_type_valid(transaction_type)

        if is_valid_transaction_type:
            return is_valid_transaction_type

        is_valid_amount = self.is_transaction_amount_valid(amount)

        if is_valid_amount:
            return is_valid_amount

        is_valid_credit_card = self.is_credit_card_valid(credit_card)

        if is_valid_credit_card:
            return is_valid_credit_card

        # Let's obtain card type:

        if credit_card[0] == "4":
            card_type = "visa"
        elif credit_card[0] == "5":
            card_type = "mastercard"
        elif credit_card[0] == "6":
            card_type = "american express"
        else:
            card_type = None
        # Let's obtain return value
        if transaction_type == "auth":
            return_value = 1
        elif transaction_type == "capture":
            return_value = 2
        elif transaction_type == "sale":
            return_value = 3
        else:
            return_value = None
        return {
            "card_type": card_type,
            "transation_value": return_value
        }
