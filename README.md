# Image Watermarking Tool

A simple Python application built with Tkinter to add text watermarks to your images. This tool allows you to customize the watermark text and its angle, providing a real-time preview before saving.

## Features

- **Graphical User Interface:** Easy-to-use interface built with Tkinter.
- **Image Support:** Load and watermark PNG and JPG images.
- **Customizable Text:** Enter your specific watermark text.
- **Angle Adjustment:** Rotate the watermark text from 0 to 90 degrees using a slider.
- **Real-time Preview:** See how your watermark looks before saving.
- **Background Support:** The application interface includes a background image.

## Prerequisites

- **Python 3.x**: Ensure you have Python installed. The code is compatible with Python 3.13.
- **Pillow**: The Python Imaging Library (Fork) is used for image processing.
- **Tkinter**: Usually comes pre-installed with standard Python distributions.

## Installation

1.  **Clone or download** this repository to your local machine.

2.  **Install the required dependencies**.
    The project relies on the `Pillow` library. You can install it using pip:

    ```bash
    pip install pillow
    ```
    
    *Note: The `requirements.txt` file may list `thinker`, which is likely a typo for `tkinter` (which is standard) or meant to be ignored since `pillow` is the main external dependency.*

## Usage

1.  Navigate to the project directory in your terminal or command prompt.

2.  Run the application:

    ```bash
    python image_watermarking_using_tkinter_python.py
    ```

3.  **Using the App:**
    - Click **"Select Image"** to choose the photo you want to watermark.
    - Enter your desired text in the **"Watermark Text"** field.
    - Adjust the **"Watermark Angle"** slider (0–90°) to rotate your text.
    - Click **"Apply Watermark"** to preview the result.
    - Click **"Save Image"** to save your watermarked photo to your computer.

## Project Structure

- `image_watermarking_using_tkinter_python.py`: The main application script.
- `requirements.txt`: List of dependencies.
- `background.png`: Background image used in the application UI.
