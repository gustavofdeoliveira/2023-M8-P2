import random
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import simpleaudio as sa

model = Ollama(model="dolphin2.2-mistral")
prompt = ChatPromptTemplate.from_template(
"""
Now you are an occupational {portugus teacher} will translate and correct Portuguese errors in the texts.
"""
)

chain = {"safety agent": RunnablePassthrough()} | prompt | model


def get_response():
    # create a loop
    while True:
        print("O que você deseja? \n")
        #get the value from terminal
        input = input()
        print("Resposta obtida: \n")
        #generate a response
        response_message = chain.stream(input)
        #print response
        print(response_message)
        #transform in a audio
        generate_audio(response_message)
    
def generate_audio(message):
    preload_models()
    # generate audio from text
    #text_prompt = """
   #     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
    #    But I also have other interests such as playing tic tac toe.
    #"""
    text_prompt = message
    audio_array = generate_audio(text_prompt)

    # Convert the audio array to int16 format (required by simpleaudio)
    audio_array_int16 = (audio_array * 32767).astype("int16")

    # Play audio directly
    play_obj = sa.play_buffer(audio_array_int16, 1, 2, SAMPLE_RATE)
    play_obj.wait_done()


def main():
    # call de function
    get_response()

if __name__ == "__main__":
    main()