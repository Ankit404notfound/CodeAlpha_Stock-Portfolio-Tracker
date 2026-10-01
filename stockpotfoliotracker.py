def track_portfolio():
    # 1. Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOG": 140.00,
        "MSFT": 330.00,
        "AMZN": 130.00
    }
    
    portfolio = {}
    
    print("Welcome to the Stock Portfolio Tracker!")
    print(f"Available stocks: {', '.join(stock_prices.keys())}")
    print("Type 'done' when you are finished adding stocks.\n")
    
    # 2. Input/Output loop
    while True:
        ticker = input("Enter stock ticker: ").upper()
        
        if ticker == 'DONE':
            break
            
        if ticker not in stock_prices:
            print("Stock not found in database. Try again.")
            continue
            
        try:
            quantity = float(input(f"Enter number of shares for {ticker}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        # Add to portfolio (combining quantities if entered multiple times)
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity
        
    # 3. Basic arithmetic and formatting
    total_investment = 0.0
    summary_text = ["\n--- Portfolio Summary ---"]
    
    for ticker, qty in portfolio.items():
        price = stock_prices[ticker]
        value = qty * price
        total_investment += value
        
        line = f"{ticker}: {qty} shares @ ${price:.2f} = ${value:.2f}"
        print(line)
        summary_text.append(line)
        
    total_line = f"\nTotal Investment Value: ${total_investment:.2f}"
    print(total_line)
    summary_text.append(total_line)
    
    # 4. File handling (Optional save)
    if portfolio:
        save_choice = input("\nSave this summary to a file? (y/n): ").lower()
        if save_choice == 'y':
            # Write all summary lines to a text file
            with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(summary_text))
            print("Successfully saved to 'portfolio_summary.txt'.")

if __name__ == "__main__":
    track_portfolio()