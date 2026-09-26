from indicvoice import IndicPipeline
import sounddevice as sd
import numpy as np


# --------------------------------------------------
# SAAKHAA TTS CONFIG
# --------------------------------------------------

LANG_CODE = "a"          # a = American English
VOICE = "af_heart"
SAMPLE_RATE = 24000


# --------------------------------------------------
# LOAD MODEL ONCE
# --------------------------------------------------

print("Loading SAAKHAA voice...")

pipeline = IndicPipeline(
    lang_code=LANG_CODE,
    repo_id="Bindkushal/IndicVoice-82M"
)

print("This is Sakha, My voice is ready.")


# --------------------------------------------------
# SPEAK
# --------------------------------------------------

def bolo(text):
    """
    Convert text to speech and play it as soon as
    audio chunks are generated.
    """

    if not text:
        return

    print(f"SAAKHAA: {text}")

    # Generate and play chunks immediately
    for gs, ps, audio in pipeline(
        text,
        voice=VOICE
    ):

        if audio is None:
            continue

        # Make sure audio is a numpy array
        audio = np.asarray(audio, dtype=np.float32)

        # Play this chunk immediately
        sd.play(audio, SAMPLE_RATE)
        sd.wait()