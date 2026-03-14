import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# ----------------------------
# Function to handle sending messages
# ----------------------------
def send_message():
    try:
        message = entry.get().strip()  # Get and clean input
        if not message:
            raise ValueError("Cannot send an empty message!")
        
        # Add user message to chat history
        chat_history.config(state='normal')
        chat_history.insert(tk.END, f"You: {message}\n")
        chat_history.config(state='disabled')
        entry.delete(0, tk.END)
        
        # Simulate a bot response
        chat_history.config(state='normal')
        chat_history.insert(tk.END, f"Bot: Echoing '{message}'\n")
        chat_history.config(state='disabled')
        
        # Scroll to the end
        chat_history.yview(tk.END)
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ----------------------------
# Create main application window
# ----------------------------
root = tk.Tk()
root.title("Simple Chat UI")
root.geometry("500x400")  # Set window size

# ----------------------------
# Chat history area (scrollable)
# ----------------------------
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
chat_history.pack(padx=10, pady=10)

# ----------------------------
# Entry box and Send button
# ----------------------------
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=5)

entry = tk.Entry(entry_frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 5))

send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

# Allow pressing Enter key to send message
def enter_pressed(event):
    send_message()

entry.bind("<Return>", enter_pressed)

# ----------------------------
# Start the GUI loop
# ----------------------------
root.mainloop()