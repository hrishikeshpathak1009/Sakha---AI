from indicvoice import IndicPipeline
import sounddevice as sd
import numpy as np


# --------------------------------------------------
# SAAKHAA TTS CONFIG
# --------------------------------------------------

LANG_CODE = "a"                    # a = American English
VOICE = "am_adam"        # blended female voice
SAMPLE_RATE = 26000


# --------------------------------------------------
# LOAD MODEL ONCE
# --------------------------------------------------

print("Loading SAAKHAA voice...")

pipeline = IndicPipeline(
    lang_code=LANG_CODE,
    repo_id="Bindkushal/IndicVoice-82M"
)

print("My voice ready.")


# --------------------------------------------------
# SPEAK
# --------------------------------------------------

def bolo(text):
    """
    Convert text to speech and play it.
    """

    if not text:
        return

    print(f"SAAKHAA: {text}")

    audio_chunks = []

    for gs, ps, audio in pipeline(
        text,
        voice=VOICE
    ):
        audio_chunks.append(audio)

    if not audio_chunks:
        return

    # Join all generated chunks
    audio = np.concatenate(audio_chunks)

    # Play
    sd.play(audio, SAMPLE_RATE)
    sd.wait()