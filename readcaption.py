from  moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

video_path = "sample.mp4"

video = VideoFileClip(video_path)

audio = video.audio

audio_file = "temp_audio.wav"
audio.write_audiofile(audio_file)

recognition = sr.Recognizer()
while True:
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognition.record(source)
            caption = recognition.recognize_google(audio_data)
            caption = caption.lower()
            print(caption)

    
    except speech_recognition.UnknownValueError as e:
        print("Could not understand audio: ", str(e))
        continue

os.remove(audio_file)