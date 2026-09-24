import torch
import soundfile as sf

from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer


MODEL = "ai4bharat/indic-parler-tts"

device = "cuda:0" if torch.cuda.is_available() else "cpu"

print("Loading SAAKHAA TTS...")
print("Device:", device)

model = ParlerTTSForConditionalGeneration.from_pretrained(
    MODEL
).to(device)

tokenizer = AutoTokenizer.from_pretrained(MODEL)

description_tokenizer = AutoTokenizer.from_pretrained(
    model.config.text_encoder._name_or_path
)


prompt = "नमस्ते, मैं साखा हूँ। मैं आपकी सहायता करने के लिए तैयार हूँ।"

description = (
    "A male Indian speaker speaks clearly and naturally. "
    "The voice is calm, friendly and conversational. "
    "The speech has a moderate pace and very clear audio."
)


description_inputs = description_tokenizer(
    description,
    return_tensors="pt"
).to(device)

prompt_inputs = tokenizer(
    prompt,
    return_tensors="pt"
).to(device)


with torch.no_grad():

    generation = model.generate(
        input_ids=description_inputs.input_ids,
        attention_mask=description_inputs.attention_mask,
        prompt_input_ids=prompt_inputs.input_ids,
        prompt_attention_mask=prompt_inputs.attention_mask,
    )


audio = generation.cpu().numpy().squeeze()

sf.write(
    "sakhaa_test.wav",
    audio,
    model.config.sampling_rate
)

print("Done!")
print("Saved: sakhaa_test.wav")