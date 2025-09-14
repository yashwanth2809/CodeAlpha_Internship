import tkinter as tk
from tkinter import scrolledtext, messagebox
RESPONSES = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a simple bot, but I'm functioning perfectly!",
    "bye": "Goodbye! Have a great day!",
    "exit": "Goodbye! Have a great day!"
}
class SimpleChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Rule-Based Chatbot")
        self.root.geometry("500x500")
        self.chat_display = scrolledtext.ScrolledText(self.root, state='disabled', wrap=tk.WORD)
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        self.user_input = tk.Entry(input_frame, width=40)
        self.user_input.pack(side=tk.LEFT, padx=(0, 10))
        send_button = tk.Button(input_frame, text="Send", command=self.process_message)
        send_button.pack(side=tk.LEFT)
    def process_message(self):
        message = self.user_input.get().strip()
        if not message:
            return  
        self._update_chat("You", message)
        response = self._get_bot_response(message)
        self._update_chat("Bot", response)
        self.user_input.delete(0, tk.END)
        if message.lower() in ['bye', 'exit']:
            messagebox.showinfo("Chatbot", "Chat session ended.")
            self.root.quit()
    def _get_bot_response(self, user_message):
        user_message = user_message.lower()
        for key in RESPONSES:
            if key in user_message:
                return RESPONSES[key]
        return "I'm sorry, I don't understand that."
    def _update_chat(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)
if __name__ == "__main__":
    window = tk.Tk()
    app = SimpleChatbotApp(window)
    window.mainloop()
