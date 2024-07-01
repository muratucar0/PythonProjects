import tkinter as tk
from tkinter import messagebox
from pytube import YouTube


def download_video():
    video_url = url_entry.get()
    output_path = path_entry.get()

    try:
        yt = YouTube(video_url)
        messagebox.showinfo("YouTube Video Downloader", f"Downloading '{yt.title}'...")

        stream = yt.streams.get_highest_resolution()


        messagebox.showinfo("YouTube Video Downloader", "Download started. Please wait...")

        stream.download(output_path)

        messagebox.showinfo("YouTube Video Downloader", f"Download complete! Saved to {output_path}")
    except Exception as e:
        messagebox.showerror("YouTube Video Downloader", f"Error downloading video: {str(e)}")



window = tk.Tk()
window.title("YouTube Video Downloader")

# Labels
url_label = tk.Label(window, text="Enter YouTube Video URL:")
url_label.pack()


url_entry = tk.Entry(window, width=50)
url_entry.pack()


path_label = tk.Label(window, text="Enter Output Path:")
path_label.pack()


path_entry = tk.Entry(window, width=50)
path_entry.pack()


download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack()


window.mainloop()