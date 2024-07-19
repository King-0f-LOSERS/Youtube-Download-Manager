import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, AudioFileClip
import threading

class MergeApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("720x720")
        self.root.title("Master Merger")
        self.root.configure(bg='#301934')
        
        self.video_path_var = tk.StringVar()
        self.audio_path_var = tk.StringVar()
        self.output_path_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Video File:", bg='#301934', fg='white',font=("Times New Roman", 12)).grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.video_path_var, width=65,font=("Times New Roman", 12)).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.select_video_file,font=("Times New Roman", 12)).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(self.root, text="Audio File:", bg='#301934', fg='white',font=("Times New Roman", 12)).grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.audio_path_var, width=65,font=("Times New Roman", 12)).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.select_audio_file,font=("Times New Roman", 12)).grid(row=1, column=2, padx=10, pady=10)

        tk.Label(self.root, text="Output File:", bg='#301934', fg='white',font=("Times New Roman", 12)).grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.output_path_var, width=65,font=("Times New Roman", 12)).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.select_output_file,font=("Times New Roman", 12)).grid(row=2, column=2, padx=10, pady=10)

        tk.Button(self.root, text="Merge", command=self.start_merge,font=("Times New Roman", 16)).grid(row=3, column=0, columnspan=3,  padx=10, pady=20)
        tk.Button(self.root, text="Clear", command=self.clear_fields,font=("Times New Roman", 16)).grid(row=4, column=0, columnspan=3, padx=10, pady=20)

    def select_video_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
        if file_path:
            self.video_path_var.set(file_path)

    def select_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav;*.aac")])
        if file_path:
            self.audio_path_var.set(file_path)

    def select_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if file_path:
            self.output_path_var.set(file_path)

    def clear_fields(self):
        self.video_path_var.set("")
        self.audio_path_var.set("")
        self.output_path_var.set("")

    def start_merge(self):
        thread = threading.Thread(target=self.merge_files)
        thread.start()

    def merge_files(self):
        video_path = self.video_path_var.get()
        audio_path = self.audio_path_var.get()
        output_path = self.output_path_var.get()

        if not video_path or not audio_path or not output_path:
            messagebox.showerror("Error", "Please select all files.")
            return

        try:
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)

            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(output_path, threads=8)
            messagebox.showinfo("Success", f"Files merged successfully! Saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MergeApp(root)
    root.mainloop()