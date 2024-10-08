import PyPDF2

import gTTS

import os



def pdf_to_speech(pdf_file, lang='en'):

    # Create a PDF file reader object

    with open(pdf_file, 'rb') as file:

        reader = PyPDF2.PdfReader(file)

        text = ""

       

        # Iterate through each page and extract text

        for page in reader.pages:

            text += page.extract_text() + "\n"

   

    # Check if any text was extracted

    if not text.strip():

        print("No text found in the PDF file.")

        return



    # Create a speech object

    tts = gTTS(text=text, lang=lang)

   

    # Save the speech to an audio file

    audio_file = pdf_file.replace('.pdf', '.mp3')

    tts.save(audio_file)

   

    # Optionally play the audio file

    os.system(f'start {audio_file}' if os.name == 'nt' else f'open {audio_file}')

   

    print(f"Converted '{pdf_file}' to '{audio_file}' and played it.")



# Example usage

pdf_file_path = "example.pdf"  # Replace with your PDF file path

pdf_to_speech(pdf_file_path)