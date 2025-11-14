import tkinter as tk
from tkinter import ttk, messagebox

# --- Updated Area Function ---

def myArea(name, length, breadth, height, radius):
    name = name.lower()

    if name == "rectangle":
        return length * breadth

    elif name == "square":
        return length ** 2

    elif name == "triangle":
        return 0.5 * breadth * height

    elif name == "circle":
        return 3.14 * radius ** 2

    elif name == "parallelogram":
        return breadth * height

    elif name == "trapezoid":
        return 0.5 * (length + breadth) * height

    elif name == "ellipse":
        return 3.14 * length * breadth

    elif name == "rhombus":
        return (length * breadth) / 2

    else:
        return -1


# --- Updated Volume Function ---

def myvolume(name, length, breadth, height, radius):
    name = name.lower()

    if name == "sphere":
        return (4/3) * 3.14 * radius ** 3

    elif name == "cube":
        return length ** 3

    elif name == "cone":
        return (1/3) * 3.14 * radius ** 2 * height

    elif name == "cuboid":
        return length * breadth * height

    elif name == "cylinder":
        return 3.14 * radius ** 2 * height

    elif name == "pyramid":
        return (1/3) * length * breadth * height

    elif name == "prism":
        return length * breadth * height

    elif name == "hemisphere":
        return (2/3) * 3.14 * radius ** 3

    elif name == "ellipsoid":
        return (4/3) * 3.14 * length * breadth * height

    else:
        return -1


# -- Condition Function ----

def mycondition(condition, a, b, c, angle):
    if condition == "Pythagorean Triplet Checker":
        if a**2 + b**2 == c**2:
            return "Yes, it's a Pythagorean Triplet"
        else:
            return "No, it's NOT a Pythagorean Triplet"

    if condition == "Complementary & Supplementary Angles":
        if angle <= 90:
            com = 90 - angle
            sup = 180 - angle
        elif angle <= 180:
            com = "error"
            sup = 180 - angle
        else:
            com = sup = "error"

        return f"Complementary: {com},     Supplementary: {sup}"


# -- GUI --

root = tk.Tk()
root.title("Math Tools GUI - Upgraded")
root.geometry("600x650")
root.resizable(False, True)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)


# -- AREA TAB --


area_frame = ttk.Frame(notebook)
notebook.add(area_frame, text="Area Calculator")

shape_area_var = tk.StringVar()
shape_area_var.set("rectangle")

ttk.Label(area_frame, text="Choose Shape:").pack(pady=5)
area_menu = ttk.Combobox(area_frame, textvariable=shape_area_var,
                         values=[
                             "rectangle", "square", "triangle", "circle",
                             "parallelogram", "trapezoid", "ellipse",
                             "rhombus"
                         ])
area_menu.pack()

length_entry = tk.Entry(area_frame)
breadth_entry = tk.Entry(area_frame)
height_entry = tk.Entry(area_frame)
radius_entry = tk.Entry(area_frame)

for widget, label in [(length_entry, "Length"),
                      (breadth_entry, "Breadth"),
                      (height_entry, "Height"),
                      (radius_entry, "Radius")]:

    ttk.Label(area_frame, text=label+":").pack()
    widget.pack()

def calc_area():
    try:
        result = myArea(
            shape_area_var.get(),
            float(length_entry.get() or 0),
            float(breadth_entry.get() or 0),
            float(height_entry.get() or 0),
            float(radius_entry.get() or 0)
        )
        messagebox.showinfo("Area Result", f"Area = {result}")
    except:
        messagebox.showerror("Error", "Invalid Input!")

ttk.Button(area_frame, text="Calculate Area", command=calc_area).pack(pady=10)



# --- VOLUME TAB ---


vol_frame = ttk.Frame(notebook)
notebook.add(vol_frame, text="Volume Calculator")

shape_vol_var = tk.StringVar()
shape_vol_var.set("cube")

ttk.Label(vol_frame, text="Choose 3D Shape:").pack(pady=5)
vol_menu = ttk.Combobox(vol_frame, textvariable=shape_vol_var,
                        values=[
                            "sphere", "cube", "cone", "cuboid", "cylinder",
                            "pyramid", "prism", "hemisphere", "ellipsoid"
                        ])
vol_menu.pack()

length_v = tk.Entry(vol_frame)
breadth_v = tk.Entry(vol_frame)
height_v = tk.Entry(vol_frame)
radius_v = tk.Entry(vol_frame)

for widget, label in [(length_v, "Length"),
                      (breadth_v, "Breadth"),
                      (height_v, "Height"),
                      (radius_v, "Radius")]:

    ttk.Label(vol_frame, text=label+":").pack()
    widget.pack()

def calc_volume():
    try:
        result = myvolume(
            shape_vol_var.get(),
            float(length_v.get() or 0),
            float(breadth_v.get() or 0),
            float(height_v.get() or 0),
            float(radius_v.get() or 0)
        )
        messagebox.showinfo("Volume Result", f"Volume = {result}")
    except:
        messagebox.showerror("Error", "Invalid Input!")

ttk.Button(vol_frame, text="Calculate Volume", command=calc_volume).pack(pady=10)



# ---- CONDITION TAB ----


cond_frame = ttk.Frame(notebook)
notebook.add(cond_frame, text="Pythagoras / Angles")

cond_var = tk.StringVar()
cond_var.set("Pythagorean Triplet Checker")

ttk.Label(cond_frame, text="Choose Condition:").pack(pady=5)
cond_menu = ttk.Combobox(cond_frame, textvariable=cond_var,
                         values=["Pythagorean Triplet Checker", "Complementary & Supplementary Angles"])
cond_menu.pack()

a_entry = tk.Entry(cond_frame)
b_entry = tk.Entry(cond_frame)
c_entry = tk.Entry(cond_frame)
angle_entry = tk.Entry(cond_frame)

for widget, label in [(a_entry, "a"),
                      (b_entry, "b"),
                      (c_entry, "c"),
                      (angle_entry, "Angle")]:
    ttk.Label(cond_frame, text=label + ":").pack()
    widget.pack()

def calc_condition():
    try:
        result = mycondition(
            cond_var.get(),
            float(a_entry.get() or 0),
            float(b_entry.get() or 0),
            float(c_entry.get() or 0),
            float(angle_entry.get() or 0),
        )
        messagebox.showinfo("Result", result)
    except:
        messagebox.showerror("Error", "Invalid Input!")

ttk.Button(cond_frame, text="Calculate", command=calc_condition).pack(pady=10)


root.mainloop()

