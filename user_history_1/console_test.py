from payment_gateway import PaymentGateway

if __name__ == '__main__':
    transaction_type = input("Tipo de transaccion: ")

    transaction_amount = float(input("Monto de transaccion: "))

    credit_card = input("Tarjeta a utilizar: ")

    pg = PaymentGateway()

    transaction_info = pg.do_sale(amount=transaction_amount, credit_card=credit_card, transaction_type=transaction_type)

    print(transaction_info)