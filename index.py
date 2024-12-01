import customtkinter

customtkinter.set_appearance_mode('system')

root = customtkinter.CTk()
root.geometry('400x400')

# place()
yellow = customtkinter.CTkFrame(master=root, fg_color='yellow', corner_radius=0, border_width=0)
yellow.place(relwidth=0.5, relheight=0.5)

red = customtkinter.CTkFrame(master=root, fg_color='red', corner_radius=0, border_width=0)
red.place(relwidth=0.5, relheight=0.5, relx=0.5)

gray = customtkinter.CTkFrame(master=root, fg_color='gray', corner_radius=0, border_width=0)
gray.place(relwidth=0.5, relheight=0.5, rely=0.5)

blue = customtkinter.CTkFrame(master=root, fg_color='blue', corner_radius=0, border_width=0)
blue.place(relwidth=0.5, relheight=0.5, rely=0.5, relx=0.5)


root.mainloop()