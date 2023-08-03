import streamlit as st
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio


preload_models()

def main():
    st.title('Zoon Bark')
    user_input = st.text_area(label='Prompt', value='Hola, me llamo Bark y soy un modelo generativo de voces y audio, a que es impresionante?!')
    audio_array = generate_audio(user_input)
    write_wav("./tmp/bark.wav", SAMPLE_RATE, audio_array)

    if st.button('Submit'):
        st.write(Audio(audio_array, rate=SAMPLE_RATE))

if __name__ == "__main__":
    main()
