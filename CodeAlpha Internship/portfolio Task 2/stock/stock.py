import tkinter as tk
from tkinter import messagebox, filedialog, ttk
STOCK_PRICES = {
    "AAPL": 175.50,
    "GOOGL": 2800.75,
    "MSFT": 300.40,
    "AMZN": 3400.20,
    "TSLA": 720.85,
    "NFLX": 500.30,
    "FB": 350.10
}
class PortfolioTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Portfolio Tracker")
        self.master.geometry("500x500")
        self.portfolio = {}  
        self._build_ui()
    def _build_ui(self):
        tk.Label(self.master, text="Stock Portfolio Tracker", font=("Helvetica", 16, "bold")).pack(pady=15)
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="Stock Symbol:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.stock_combobox = ttk.Combobox(input_frame, values=list(STOCK_PRICES.keys()), width=15)
        self.stock_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.stock_combobox.set("AAPL")  # Default selection
        tk.Label(input_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.qty_entry = tk.Entry(input_frame, width=18)
        self.qty_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(input_frame, text="Add Stock", command=self.add_stock).grid(row=2, column=0, columnspan=2, pady=10)
        self.output_text = tk.Text(self.master, height=15, width=60, state=tk.DISABLED)
        self.output_text.pack(pady=10)
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Show Portfolio", command=self.show_portfolio).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Save Summary", command=self.save_summary).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Clear Portfolio", command=self.clear_portfolio).grid(row=0, column=2, padx=10)
    def add_stock(self):
        symbol = self.stock_combobox.get().upper()
        qty_text = self.qty_entry.get()
        if symbol not in STOCK_PRICES:
            messagebox.showerror("Error", "Please select a valid stock symbol.")
            return
        try:
            qty = int(qty_text)
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a positive integer.")
            return
        if symbol in self.portfolio:
            self.portfolio[symbol] += qty
        else:
            self.portfolio[symbol] = qty
        messagebox.showinfo("Success", f"Added {qty} shares of {symbol}.")
        self.qty_entry.delete(0, tk.END)
    def show_portfolio(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        if not self.portfolio:
            self.output_text.insert(tk.END, "Portfolio is empty.\n")
        else:
            total_investment = 0
            self.output_text.insert(tk.END, "=== Portfolio Summary ===\n\n")
            for symbol, qty in self.portfolio.items():
                price = STOCK_PRICES[symbol]
                investment = price * qty
                total_investment += investment
                self.output_text.insert(tk.END,
                    f"{symbol}: {qty} shares @ ${price:.2f} → Investment: ${investment:.2f}\n")
            self.output_text.insert(tk.END, f"\nTotal Investment: ${total_investment:.2f}\n")
        self.output_text.config(state=tk.DISABLED)
    def save_summary(self):
        if not self.portfolio:
            messagebox.showwarning("Warning", "Nothing to save. Portfolio is empty.")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save Portfolio Summary"
        )
        if not file_path:
            return
        total_investment = 0
        with open(file_path, "w") as file:
            file.write("=== Portfolio Summary ===\n\n")
            for symbol, qty in self.portfolio.items():
                price = STOCK_PRICES[symbol]
                investment = price * qty
                total_investment += investment
                file.write(f"{symbol}: {qty} shares @ ${price:.2f} → Investment: ${investment:.2f}\n")
            file.write(f"\nTotal Investment: ${total_investment:.2f}\n")
        messagebox.showinfo("Saved", f"Portfolio saved to:\n{file_path}")
    def clear_portfolio(self):
        self.portfolio.clear()
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Portfolio cleared.\n")
        self.output_text.config(state=tk.DISABLED)
if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioTracker(root)
    root.mainloop()
