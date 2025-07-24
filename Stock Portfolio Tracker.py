import tkinter as tk
from tkinter import messagebox, filedialog

# GUI Setup
root = tk.Tk()
root.title("Stock Portfolio Tracker || Developer by Ramakant Chaudhari")
root.geometry("500x600")
root.configure(bg='yellow')  # Set background color of the window

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320,
    "HP": 200
}

portfolio = {}

def add_stock():
    stock = stock_entry.get().upper()
    try:
        qty = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid quantity.")
        return

    if stock not in stock_prices:
        messagebox.showerror("Stock not found", f"{stock} is not in the price list.")
        return

    if stock in portfolio:
        portfolio[stock] += qty
    else:
        portfolio[stock] = qty

    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    update_summary()

def update_summary():
    summary_text.delete("1.0", tk.END)
    total = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = price * qty
        total += investment
        summary_text.insert(tk.END, f"{stock}: {qty} × ${price} = ${investment}\n")
    summary_text.insert(tk.END, f"\nTotal Investment: ${total}")

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write("Stock,Quantity,Price,Investment\n")
            total = 0
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                investment = price * qty
                total += investment
                f.write(f"{stock},{qty},{price},{investment}\n")
            f.write(f"\nTotal Investment: ${total}")
        messagebox.showinfo("Saved", f"Portfolio saved to {file_path}")

# Labels and entries
tk.Label(root, text="Stock Symbol:", bg='yellow').pack()
stock_entry = tk.Entry(root)
stock_entry.pack()

tk.Label(root, text="Quantity:", bg='yellow').pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(root, text="Add to Portfolio", command=add_stock, bg='lightgray').pack(pady=10)

tk.Label(root, text="Portfolio Summary:", bg='yellow').pack()
summary_text = tk.Text(root, height=15, width=45)
summary_text.pack()

tk.Button(root, text="Save to File", command=save_to_file, bg='lightgray').pack(pady=10)

root.mainloop()
