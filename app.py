from openai import OpenAI
import docx
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Text Translator")
root.configure(bg="white")

header_font = ("Open Sans", 16, "bold")
header = tk.Label(root, text="Text Translator", bg="white", font=header_font)
header.grid(row=0, column=0, columnspan=2, pady=20)

browse_button = tk.Button(root, text="Browse",
                          bg="#4267B2", fg="black", relief="flat",
                          borderwidth=0, activebackground="#4267B2",
                          activeforeground="white")
browse_button.config(font=("Arial", 12, "bold"), width=10, height=2)
browse_button.grid(row=1, column=0, padx=20, pady=20)

# 创建语言选择下拉菜单
languages = ["Bulgarian", "Hindi", "Spanish", "French"]
language_var = tk.StringVar(root)
language_var.set(languages[0])  # 设置默认值
language_menu = tk.OptionMenu(root, language_var, *languages)
language_menu.config(font=("Arial", 12), width=10)
language_menu.grid(row=1, column=1, padx=20, pady=20)

# 创建文本区域
text_field = tk.Text(root, height=20, width=50, bg="white", fg="black",
                     relief="flat", borderwidth=0, wrap="word")
text_field.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

# 配置网格行和列的权重
text_field.grid_rowconfigure(0, weight=1)
text_field.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


root.mainloop()
