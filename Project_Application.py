import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

class EmotionApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Emotion Prediction App")
        self.geometry("1000x600")  # Adjust the size as needed

        # Create sidebar for emotion labels
        self.sidebar = tk.Frame(self, width=200, bg='white')
        self.sidebar.pack(fill='y', side='left', expand=False)

        # Define emotions and colors
        self.emotions = ['ANGER', 'CONTEMPT', 'DISGUST', 'FEAR', 'HAPPINESS', 'NEUTRALITY', 'SADNESS', 'SURPRISE']
        self.colors = [
            '#c12f2f',  # Darker red for ANGER
            '#cca300',  # Darker gold for CONTEMPT
            '#7a0099',  # Darker purple for DISGUST
            '#33cc33',  # Darker green for FEAR
            '#007acc',  # Darker blue for HAPPINESS
            '#a6a6a6',  # Darker grey for NEUTRALITY
            '#e6e600',  # Darker yellow for SADNESS
            '#ff6600'   # Darker orange for SURPRISE
        ]

        # Create a label for each emotion in the sidebar
        self.emotion_labels = {}
        for emotion, color in zip(self.emotions, self.colors):
            label = tk.Label(self.sidebar, text=emotion, bg=color, fg='white', width=20, height=2)
            label.pack(pady=5, padx=10)
            self.emotion_labels[emotion] = label

        # Label to display instructions
        self.instruction_label = tk.Label(self, text="Drag an image here or click to browse.")
        self.instruction_label.pack(side="top", pady=10)

        # Frame to hold the image
        self.display_frame = tk.Frame(self)
        self.display_frame.pack(expand=True)

       # Frame to hold the actual and predicted labels
        self.bottom_frame = tk.Frame(self, bg='white')
        self.bottom_frame.pack(side="bottom", fill="x", pady=10)  # Add padding for visual spacing

        # Label font configuration
        label_font = ('Helvetica', 16, 'bold')  # Increased font size for better visibility

        # Initialize labels for actual and predicted emotions and pack them horizontally and centered
        self.actual_label = tk.Label(self.bottom_frame, text="ACTUAL: ", bg="white", fg="black", font=label_font)
        self.predicted_label = tk.Label(self.bottom_frame, text="PREDICTED: ", bg="white", fg="black", font=label_font)
        self.actual_label.pack(side="left", expand=True, anchor='center')
        self.predicted_label.pack(side="left", expand=True, anchor='center')

        # Make the instruction label a drop target
        self.instruction_label.drop_target_register(DND_FILES)
        self.instruction_label.dnd_bind('<<Drop>>', self.on_drop)
        self.instruction_label.bind("<Button-1>", self.browse_image)

    def on_drop(self, event):
        file_path = event.data
        if file_path:
            self.predict_and_display(file_path)

    def browse_image(self, event):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.predict_and_display(file_path)

    def predict_and_display(self, file_path):
        for widget in self.display_frame.winfo_children():
            widget.pack_forget()

        # Load the image using PIL and display it
        image = Image.open(file_path)
        image.thumbnail((250, 250))  # Resize for display
        photo = ImageTk.PhotoImage(image)

        # Image label
        image_label = tk.Label(self.display_frame, image=photo)
        image_label.image = photo
        image_label.pack()

        # Predict emotion (replace this with your actual prediction logic)
        predicted_emotion = "CONTEMPT"  # Placeholder for the predicted emotion
        actual_emotion = "ANGER"     # Placeholder for the actual emotion

        # Update the actual and predicted emotion labels
        self.actual_label.config(text=f"ACTUAL: {actual_emotion}", bg=self.emotion_labels[actual_emotion].cget("bg"), fg='white')
        self.predicted_label.config(text=f"PREDICTED: {predicted_emotion}", bg=self.emotion_labels[predicted_emotion].cget("bg"), fg='white')

        # Repack the actual and predicted labels at the bottom, centered horizontally
        self.actual_label.pack(side="left", expand=True, anchor='center')
        self.predicted_label.pack(side="left", expand=True, anchor='center')


if __name__ == "__main__":
    app = EmotionApp()
    app.mainloop()
