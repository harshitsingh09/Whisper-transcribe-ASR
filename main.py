### First install dependencies: 
### " pip install openai-whisper gradio torch "

import whisper
import gradio as gr

# Load the Whisper model
model = whisper.load_model("base")

# Define the transcription function
def transcribe_audio(audio):
    # Load and transcribe the audio
    transcription = model.transcribe(audio)["text"]
    return transcription

# Create the Gradio interface
with gr.Blocks() as app:
    gr.Markdown("### Whisper Audio Transcription")
    audio_input = gr.Audio(type="filepath", label="Speak or upload an audio file")
    output_text = gr.Textbox(label="Transcription")

    # Link input and output to the transcription function
    audio_input.change(fn=transcribe_audio, inputs=audio_input, outputs=output_text)

# Launch the app
app.launch()

# Verification
print("App running!")