import tkinter as tk
import openai

openai.api_key = "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"

history = []

def set_api_key():
    openai.api_key = api_key_entry.get()
    try:
        model_engine = openai.Model.list()
        set_api_key_button.config(state="disabled")
        send_button.config(state="normal")
    except:
        invalid_key_warning = tk.Toplevel(root)
        invalid_key_warning.title("Invalid API Key")
        invalid_key_warning.geometry("340x100")
        invalid_key_warning_label = tk.Label(invalid_key_warning, text="Invalid API Key. Please enter a valid key.")
        invalid_key_warning_label.pack()
        invalid_key_warning_button = tk.Button(invalid_key_warning, text="Ok", command=invalid_key_warning.destroy)
        invalid_key_warning_button.pack()


def chat_with_chatgpt():
    user_input = input_field.get()
    history_text.config(state="normal")
    history_text.insert("end", "You: " + user_input + "\n")
    history.append("You: " + user_input + "\n")
    context = "".join(history)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=context,
        max_tokens=1000,
        temperature=0.5
    ).get("choices")[0].get("text")
    history_text.insert("end", "ChatGPT: " + response + "\n")
    history.append("ChatGPT: " + response + "\n")
    history_text.config(state="disabled")
    input_field.delete(0, "end")

def change_theme(theme):
    if theme == "Bruh":
        # Set text color to white
        text_color = "white"
        # Set background color to white
        background_color = "white"
        # Set button color to gray
        button_color = "gray"
    elif theme == "Bro":
        # Set text color to white
        text_color = "white"
        # Set background color to black
        background_color = "black"
        # Set button color to gray
        button_color = "gray"
    elif theme == "Morninng":
        # Set text color to white
        text_color = "white"
        # Set background color to light green
        background_color = "green3"
        # Set button color to bright yellow
        button_color = "yellow"
    elif theme == "Sunset":
        # Set text color to white
        text_color = "white"
        # Set background color to orange-red
        background_color = "orange red"
        # Set button color to yellow
        button_color = "yellow"
    else:
        # Set default values for text color, background color, and button color
        background_color = "white"

    # Update the color of text, background, and buttons in the application
    root.config(bg=background_color)

root = tk.Tk()
root.title("You will never be that smart")
root.geometry("800x850")

api_key_label = tk.Label(root, text="API Key:")
api_key_label.pack(pady=10)

api_key_entry = tk.Entry(root, width=50)
api_key_entry.pack(pady=10)

set_api_key_button = tk.Button(root, text="Check API Key", command=set_api_key)
set_api_key_button.pack()

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Themes", menu=theme_menu)

theme_menu.add_command(label="Bruh", command=lambda: change_theme("Bruh"))
theme_menu.add_command(label="Bro", command=lambda: change_theme("Bro"))
theme_menu.add_command(label="Morninng", command=lambda: change_theme("Morninng"))
theme_menu.add_command(label="Sunset", command=lambda: change_theme("Sunset"))

history_text = tk.Text(root, height=30, width=70)
history_text.pack(pady=10)
history_text.config(state="disabled")

input_field = tk.Entry(root, width=70)
input_field.pack(pady=10)

send_button = tk.Button(root, text="Send", command=chat_with_chatgpt)
send_button.pack()


change_theme("Bruh")

send_button.config(state="disabled")

root.mainloop()
