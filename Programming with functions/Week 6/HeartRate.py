# import tkinter as tk
# from tkinter import Frame, Label, Button
# from NumberEntry import IntEntry


# def main():
#     root = tk.Tk()
#     frm_main = Frame(root)
#     frm_main.master.title("Heart Rate")
#     frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
#     populate_main_window(frm_main)
#     root.mainloop()

# def populate_main_window(frm_main):
#     lbl_age = Label(frm_main, text="Age (12 - 90):")
#     ent_age = IntEntry(frm_main, width=4, lower_bound=12, upper_bound=90)
#     lbl_age_units = Label(frm_main, text="years")
#     lbl_rates = Label(frm_main, text="Rates:")
#     lbl_slow = Label(frm_main, width=3)
#     lbl_fast = Label(frm_main, width=3)
#     lbl_rate_units = Label(frm_main, text="beats/minute")
#     btn_clear = Button(frm_main, text="Clear")
#     lbl_age.grid(      row=0, column=0, padx=3, pady=3)
#     ent_age.grid(      row=0, column=1, padx=3, pady=3)
#     lbl_age_units.grid(row=0, column=2, padx=0, pady=3)

#     lbl_rates.grid(     row=1, column=0, padx=(30,3), pady=3)
#     lbl_slow.grid(      row=1, column=1, padx=3, pady=3)
#     lbl_fast.grid(      row=1, column=2, padx=3, pady=3)
#     lbl_rate_units.grid(row=1, column=3, padx=0, pady=3)

#     btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

#     def calculate(event):
#         try:
#             age = ent_age.get()
#             max_rate = 220 - age

#             slow = max_rate * 0.65
#             fast = max_rate * 0.85

#             lbl_slow.config(text=f"{slow:.0f}")
#             lbl_fast.config(text=f"{fast:.0f}")

#         except ValueError:
#             lbl_slow.config(text="")
#             lbl_fast.config(text="")

#     def clear():
#         btn_clear.focus()
#         ent_age.clear()
#         lbl_slow.config(text="")
#         lbl_fast.config(text="")
#         ent_age.focus()

#     ent_age.bind("<KeyRelease>", calculate)

#     btn_clear.config(command=clear)

#     ent_age.focus()

# if __name__ == "__main__":
#     main()
#print('--------------------')
import math
import tkinter as tk
from tkinter import Frame, Label, Button
from NumberEntry import IntEntry, FloatEntry


def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Tire Volume")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_window(frm_main)
    root.mainloop()


def populate_main_window(frm_main):
    lbl_width = Label(frm_main, text="Width (80 - 300):")
    lbl_ratio = Label(frm_main, text="Aspect Ratio (30 - 90):")
    lbl_diam = Label(frm_main, text="Diameter (7 - 30):")
    lbl_volume = Label(frm_main, text="Volume:")
    ent_width = IntEntry(frm_main, width=5, lower_bound=80, upper_bound=300)
    ent_ratio = IntEntry(frm_main, width=5, lower_bound=30, upper_bound=90)
    ent_diam = FloatEntry(frm_main, width=5, lower_bound=7, upper_bound=30)
    txt_volume = Label(frm_main, width=5, anchor="e")
    lbl_width_units = Label(frm_main, text="millimeters")
    lbl_diam_units = Label(frm_main, text="inches")
    lbl_vol_units = Label(frm_main, text="liters")
    btn_clear = Button(frm_main, text="Clear")
    lbl_width.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
    ent_width.grid(      row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_width_units.grid(row=0, column=2, padx=0, pady=2, sticky="w")

    lbl_ratio.grid(     row=1, column=0, padx=3, pady=2, sticky="e")
    ent_ratio.grid(     row=1, column=1, padx=3, pady=2, sticky="w")

    lbl_diam.grid(      row=2, column=0, padx=3, pady=2, sticky="e")
    ent_diam.grid(      row=2, column=1, padx=3, pady=2, sticky="w")
    lbl_diam_units.grid(row=2, column=2, padx=0, pady=2, sticky="w")

    lbl_volume.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
    txt_volume.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
    lbl_vol_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
    btn_clear.grid(    row=3, column=3, padx=3, pady=2)

    def calculate(event):
        try:
            w = ent_width.get()
            a = ent_ratio.get()
            d = ent_diam.get()

            v = (math.pi * w * w * a * (w * a + 2540 * d)) / 10_000_000_000

            txt_volume.config(text=f"{v:.2f}")

        except ValueError:
            txt_volume.config(text="")
    def clear():
        btn_clear.focus()
        ent_width.clear()
        ent_ratio.clear()
        ent_diam.clear()
        txt_volume.config(text="")
        ent_width.focus()

    ent_width.bind("<KeyRelease>", calculate)
    ent_ratio.bind("<KeyRelease>", calculate)
    ent_diam.bind("<KeyRelease>", calculate)

    btn_clear.config(command=clear)

    ent_width.focus()

if __name__ == "__main__":
    main()