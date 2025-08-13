# SRT to VTT Converter

A simple Python script to convert SubRip subtitle files (`.srt`) to WebVTT (`.vtt`) format.

## Description

This script will scan a directory you specify, find all `.srt` files within it, and convert each of them to a `.vtt` file in the same directory. The original `.srt` files are not modified or deleted.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd srt-to-vtt
    ```

2.  **Run the script:**
    You will need Python 3.6 or higher.

    ```bash
    python3 main.py
    ```

3.  **Enter the directory path:**
    When prompted, enter the absolute or relative path to the directory containing your `.srt` files and press Enter.

    ```
    Input directory path (all files inside directory will be converted): /path/to/your/subtitles
    ```

    The script will then process all `.srt` files in that folder.

    ### Example

    If you have a file structure like this:

    ```
    /path/to/your/subtitles/
    ├── movie1.srt
    └── movie2.srt
    ```

    After running the script, it will look like this:

    ```
    /path/to/your/subtitles/
    ├── movie1.srt
    ├── movie1.vtt
    ├── movie2.srt
    └── movie2.vtt
    ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.