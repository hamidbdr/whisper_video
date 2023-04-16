import whisper

model = whisper.load_model("small")
result = model.transcribe("Recording.m4A")

print(result["text"])
