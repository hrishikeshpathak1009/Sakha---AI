from indicvoice import IndicPipeline
import soundfile as sf

pipeline = IndicPipeline(
    lang_code="a",
    repo_id="Bindkushal/IndicVoice-82M"
)

for gs, ps, audio in pipeline(
    "Hello Pathak ji, I am your personal AI assistant. How can I help you today",
    voice="am_adam"
):
    sf.write("sakhaa.wav", audio, 24000)

print("Done!")