def main():
    while True:
        try:
            rem_pesos = int(input("What is the remaining pesos?"))
            rem_soles = int(input("What is the remaining soles?"))
            rem_reais = int(input("What is the remaining reais?"))
            break
        except valueError:
            print("Please enter a valid remaining currency")

    usd_pesos = (rem_pesos / 4028)
    usd_soles = (rem_soles / 3.69)
    usd_reais = (rem_reais / 0.17)

    total = (usd_pesos + usd_soles + usd_reais)
    print(f"Total value in USD: ${total:.2f}")
main()
