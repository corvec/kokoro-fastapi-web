# Kokoro FastAPI Workaround Web UI

## Overview

This repository is intended to be used in conjunction with https://github.com/remsky/Kokoro-FastAPI,
as a workaround for https://github.com/remsky/Kokoro-FastAPI/issues/103.

### Prerequisites

- Python 3.9 or higher
- Access to a Kokoro FastAPI server

### Getting Started

To begin using this interface, follow these steps:

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/corvec/kokoro-fastapi-web.git
    cd kokoro-fast-api-web
    ```
   
2. Install the required dependencies.
   It's recommended to use a virtual environment, e.g., `venv` or `conda`.
    ```bash
    pip install -r requirements.txt
    ```


3. Run the Gradio interface.
    ```bash
    python app.py
    ```


## Usage

1. Enter the URL to your Kokoro FastAPI instance in the input field.
2. Choose a voice option from the dropdown.
3. Input the desired text into the input textbox.
4. Click the "Generate" button or press Enter to create the corresponding speech.
5. The generated speech will be displayed as an audio output.

## Code Structure

The code is organized into two main components:

- `tts`: This module contains the function responsible for interacting with the OpenAI-compatible API to generate speech.
- `gradio_interface`: This module sets up the Gradio interface, including input fields, buttons, and the speech output.

## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as needed.
