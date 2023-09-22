# importing speech recognition package from google api
import speech_recognition as sr
import openai
import pyttsx3

openai.api_key = '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'

engine = pyttsx3.init()

rec = sr.Recognizer()

my_micro = sr.Microphone(device_index=1)

messages = [
    {"role": "system", "content": "You are a helpful assistant. Keep responses short."},
]

while True:
    with my_micro as source:
        print("Say something..")
        audio = rec.listen(source)

        to_text = rec.recognize_google(audio)

    print(f"User: {to_text}")
    message = to_text

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    engine.say(reply)
    engine.runAndWait()
    messages.append({"role": "assistant", "content": reply})