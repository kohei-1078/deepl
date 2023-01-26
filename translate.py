import os
from dotenv import load_dotenv
import deepl

load_dotenv()
API_KEY = os.environ['API_KEY']

def translate_text(api_key, text, source_lang, target_lang):
    translator = deepl.Translator(api_key)
    translated_text = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    print('翻訳前： ', text)
    print('翻訳後： ', translated_text)

def translate_document(api_key, input_path, output_path, target_lang):
    translator = deepl.Translator(api_key)
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang=target_lang,
        # formality='more'
    )


def main():
    text = "Riemann Zeta function is a very important function in number theory."
    source_lang = 'EN'
    target_lang = 'JA'
    translate_text(API_KEY, text, source_lang, target_lang)

    # input_path = './test.m4a_translated.txt'
    # output_path = './test.m4a_retranslated.txt'
    # target_lang = 'EN-US'
    # translate_document(API_KEY, input_path, output_path, target_lang)

if __name__=="__main__":
    main()