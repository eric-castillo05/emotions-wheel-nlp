import warnings
warnings.filterwarnings("ignore")
import traceback
import torch
from transformers import MarianMTModel, MarianTokenizer

marian_model_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')
marian_tokenizer_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es')


def en2esp_marian(text, lang='Spanish'):
    try:
        inputs = marian_tokenizer_es(text, return_tensors="pt", padding=True, truncation=True)
        translated_text = marian_model_es.generate(**inputs)
        translated_text = marian_tokenizer_es.batch_decode(translated_text, skip_special_tokens=True)

        return translated_text[0]
    except(Exception) as e:
        # print(e)
        print(traceback.format_exc())



def en2esp_marian_cuda(text, lang='Spanish'):
    try:
        prompt = text
        
        inputs = marian_tokenizer_es(text, return_tensors="pt", padding=True, truncation=True)
        
        if torch.cuda.is_available():
            inputs = {key: value.cuda() for key, value in inputs.items()}
        
        translated_text = marian_model_es.generate(**inputs)
        translated_text = marian_tokenizer_es.batch_decode(translated_text, skip_special_tokens=True)

        return translated_text[0]
    except Exception as e:
        print(traceback.format_exc())      
