import gradio as gr
import os, tempfile
from openai import OpenAI

server_name = os.getenv("SERVER_NAME", default="0.0.0.0")
server_port = int(os.getenv("SERVER_PORT", default="7860"))
default_api_key = os.getenv("OPENAI_API_KEY", default="not-needed")
default_base_url = os.getenv("OPENAI_API_BASE_URL", default="http://localhost:8880/v1")
share = os.getenv("SHARE", default="false").lower() == "true"
kokoro_voices = [
    "af_alloy",
    "af_aoede",
    "af_bella",
    "af_heart",
    "af_jadzia",
    "af_jessica",
    "af_kore",
    "af_nicole",
    "af_nova",
    "af_river",
    "af_sarah",
    "af_sky",
    "af_v0",
    "af_v0bella",
    "af_v0irulan",
    "af_v0nicole",
    "af_v0sarah",
    "af_v0sky",
    "am_adam",
    "am_echo",
    "am_eric",
    "am_fenrir",
    "am_liam",
    "am_michael",
    "am_onyx",
    "am_puck",
    "am_santa",
    "am_v0adam",
    "am_v0gurney",
    "am_v0michael",
    "bf_alice",
    "bf_emma",
    "bf_lily",
    "bf_v0emma",
    "bf_v0isabella",
    "bm_daniel",
    "bm_fable",
    "bm_george",
    "bm_lewis",
    "bm_v0george",
    "bm_v0lewis",
    "ef_dora",
    "em_alex",
    "em_santa",
    "ff_siwis",
    "hf_alpha",
    "hf_beta",
    "hm_omega",
    "hm_psi",
    "if_sara",
    "im_nicola",
    "jf_alpha",
    "jf_gongitsune",
    "jf_nezumi",
    "jf_tebukuro",
    "jm_kumo",
    "pf_dora",
    "pm_alex",
    "pm_santa",
    "zf_xiaobei",
    "zf_xiaoni",
    "zf_xiaoxiao",
    "zf_xiaoyi",
    "zm_yunjian",
    "zm_yunxi",
    "zm_yunxia",
    "zm_yunyang"
]
default_voice = os.getenv("DEFAULT_VOICE", default=kokoro_voices[0])

def tts(text, model, voice, api_key, base_url=None):
    if not api_key:
        raise gr.Error('Please enter your OpenAI API Key')

    try:
        # Only use base_url if it's not empty
        if base_url and base_url.strip():
            client = OpenAI(api_key=api_key, base_url=base_url)
        else:
            client = OpenAI(api_key=api_key)

        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text,
        )

    except Exception as error:
        print(str(error))
        raise gr.Error("An error occurred while generating speech. Please check your API key and try again.")

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file.write(response.content)

    return temp_file.name

def gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# <center> Kokoro FastAPI Text-To-Speech </center>")
        with gr.Row(variant='panel'):
            api_key = gr.Textbox(type='password', label='API Key', placeholder='Enter your OpenAI API key', value=default_api_key)
            base_url = gr.Textbox(label='API Base URL', placeholder='http://localhost:8880/v1', value=default_base_url)
            model = gr.Dropdown(choices=['tts-1','tts-1-hd'], label='Model', value='tts-1')
            voice = gr.Dropdown(choices=kokoro_voices, label='Voice Options', value=default_voice)

        text = gr.Textbox(label="Input text", placeholder="Enter your text and then click on the 'Generate' button, or press the Enter key.")
        btn = gr.Button("Generate")
        output_audio = gr.Audio(label="Speech Output")

        text.submit(fn=tts, inputs=[text, model, voice, api_key, base_url], outputs=output_audio, api_name="tts_enter_key")
        btn.click(fn=tts, inputs=[text, model, voice, api_key, base_url], outputs=output_audio, api_name="tts_button")

    demo.launch(server_name=server_name, server_port=server_port, share=share)

if __name__ == "__main__":
    gradio_interface()
