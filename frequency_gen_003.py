import numpy as np  # Importing the NumPy library for numerical operations
import matplotlib.pyplot as plt  # Importing matplotlib for plotting graphs
import tkinter as tk  # Importing Tkinter for GUI
from tkinter import messagebox  # Importing messagebox for alerts

# Function to generate a sine wave
def generate_sine_wave(frequency, duration, sample_rate):
    total_samples = int(sample_rate * duration)  # Calculate total samples
    t = np.linspace(0, duration, total_samples, endpoint=False)  # Generate time values
    sine_wave = np.sin(2 * np.pi * frequency * t)  # Generate sine wave values
    return t, sine_wave  # Return time and sine wave values

# Function to plot the sine wave based on user inputs
def plot_sine_wave():
    try:
        # Get user input from the entry fields
        frequency = float(frequency_entry.get())
        duration = float(duration_entry.get())
        sample_rate = int(sample_rate_entry.get())

        # Generate the sine wave
        time_values, sine_wave_values = generate_sine_wave(frequency, duration, sample_rate)

        # Plotting the sine wave
        plt.figure(figsize=(10, 5))  # Set the figure size
        plt.plot(time_values, sine_wave_values)  # Plot time vs. sine wave values
        plt.title(f'Sine Wave at {frequency} Hz')  # Title of the plot
        plt.xlabel('Time (seconds)')  # X-axis label
        plt.ylabel('Amplitude')  # Y-axis label
        plt.grid(True)  # Show grid for better readability
        plt.xlim(0, duration)  # Set x-axis limits
        plt.ylim(-1.5, 1.5)  # Set y-axis limits
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Add a horizontal line at y=0
        plt.show()  # Display the plot

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")  # Show error if input is invalid

# Setting up the Tkinter GUI
root = tk.Tk()  # Create the main window
root.title("Frequency Generator")  # Set the window title
root.geometry("300x250")  # Set the window size

# Create a light green canvas
canvas = tk.Canvas(root, bg='lightgreen')
canvas.pack(fill=tk.BOTH, expand=True)

# Input fields for frequency, duration, and sample rate on the canvas
tk.Label(canvas, text="Frequency (Hz):").pack(pady=5)  # Frequency label
frequency_entry = tk.Entry(canvas)  # Entry for frequency
frequency_entry.pack(pady=5)

tk.Label(canvas, text="Duration (seconds):").pack(pady=5)  # Duration label
duration_entry = tk.Entry(canvas)  # Entry for duration
duration_entry.pack(pady=5)

tk.Label(canvas, text="Sample Rate (samples/sec):").pack(pady=5)  # Sample rate label
sample_rate_entry = tk.Entry(canvas)  # Entry for sample rate
sample_rate_entry.pack(pady=5)

# Button to generate the sine wave
generate_button = tk.Button(canvas, text="Generate Sine Wave", command=plot_sine_wave)
generate_button.pack(pady=20)  # Add the button to the canvas

# Start the Tkinter event loop
root.mainloop()