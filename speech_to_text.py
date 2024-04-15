import assemblyai as aai

aai.settings.api_key = "f94f355026724abfade3adba31ee8c82"

FILE_URL = "C:/Users/abhi1/Downloads/SawanoHiroyuki-nZk-feat-XAI-DARK-ARIA-LV2-(Celebnob.com).mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
