import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import joblib
import numpy as np
#pip install pillow

mymodel = joblib.load("fassion-cloths-predictor.joblib")

def classify_image(img_path):
    img = Image.open(img_path)

    # Convert the image to grayscale and resize it to 28x28
    resize_img = img.convert('L').resize((28, 28))

    # Convert the resized image to a numpy array
    img_array = np.array(resize_img)

    # Flatten the image array to have 784 features
    shape_img = img_array.flatten()

    # Ensure the shape is correct
    if shape_img.shape != (784,):
        raise ValueError("Image shape does not match (784,)")

    # Predict using the model
    output = mymodel.predict(shape_img.reshape(1, -1))

    return output





def upload_image():
    filepath = filedialog.askopenfilename()
    
    myimg = Image.open(filepath)
    myimg.thumbnail((300, 300))
    convert_tk = ImageTk.PhotoImage(myimg)

    imshowu.config(image=convert_tk)
    imshowu.image = convert_tk

    zx = classify_image(filepath)

    lbloutput.config(text=f"The Predicted Product is : {zx}")



app = tk.Tk()
app.geometry("500x600")
app.title("Fassion Prdocts")
app.config(background = "light green")

lbl = tk.Label(app, text = "Upload Image To Check", font = ("robort", 20, "bold"), bg = "light green", fg = "green")
lbl.pack(pady = 20)

btn = tk.Button(app, text = "Check Product", font = ("arial", 15, "bold"), fg = "white", bg = "dark green", command = upload_image)
btn.pack()


imshowu = tk.Label(app)
imshowu.pack(pady=20)

lbloutput = tk.Label(app, text="", font=("arial", 15))
lbloutput.pack()


app.mainloop()