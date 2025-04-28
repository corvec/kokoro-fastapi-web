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

2. It's recommended, but not required, to use a virtual environment, e.g., `venv`, `conda`, or `uv`.
   These instructions are for `venv` and may need to be adjusted if you're using Windows:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```


4. Run the Gradio interface.
    ```bash
    python app.py
    ```

## Usage

1. Enter the URL to your Kokoro FastAPI instance in the input field.
2. Choose a voice option from the dropdown.
3. Input the desired text into the input textbox.
4. Click the "Generate" button or press Enter to create the corresponding speech.
5. The generated speech will be displayed as an audio output.

## Env Vars

This app will use the following env vars if they're present. None are required.

- `OPENAI_API_KEY`: Provide the default OpenAI API key. Not generally relevant as Kokoro FastAPI doesn't require it.
- `OPENAI_API_BASE_URL`: Provide the default base URL for the OpenAI-compatible API. Point this to your server. By default it is set to `http://localhost:8880/v1`, which will work if you're running Kokoro locally.
- `DEFAULT_VOICE`: Provide the default voice. If you don't provide one, this will default to the first entry in the list.
- `SERVER_URL`: That's the URL for this service. 
  - Use `0.0.0.0` (the default) to expose the service on your local network.
  - Use `127.0.0.1` to restrict access to your local machine.
- `SERVER_PORT`: The port for the server. By default, it is set to `7860`, which is the default for Gradio.
  You should change this if you're running something else on that port.
- `SHARE`: If set to `true`, then Gradio will create a public link to the app.
  - See https://www.gradio.app/guides/sharing-your-app#sharing-demos for more information.

## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as needed.
