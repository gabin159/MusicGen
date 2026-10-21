import torch
from scipy.io.wavfile import write
from transformers import AutoProcessor, MusicgenForConditionalGeneration

MODEL_ID = "facebook/musicgen-small"
DEVICE = "cpu"
PROMPT = "reggaeton, dembow drum pattern, deep punchy kick and rimshot, round sub bass, plucked synth hook, smooth male vocal sung in Spanish, light auto-tune, call-and-response ad-libs, 94 BPM"

print("Cargando Musicgen...")

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = MusicgenForConditionalGeneration.from_pretrained(MODEL_ID)

model.to(DEVICE)
model.eval()

print("Preparando el prompt...")

inputs = processor(
    text=[PROMPT],
    padding=True,
    return_tensors="pt"
).to(DEVICE)

print("Generando música....")

with torch.inference_mode():
    audio = model.generate(
        **inputs,
        do_sample=True,
        guidance_scale=3.0,
        max_new_tokens=200
    )

sample_rate = model.config.audio_encoder.sampling_rate
waveform = audio[0, 0].cpu().float().numpy()

write("musica.wav", sample_rate, waveform)
print("¡Música generada con éxito en musica.wav!")
