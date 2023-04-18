#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from pygpt4all.models.gpt4all import GPT4ALL

from pygpt4all.models.gpt4all import GPT4ALL as GPT4ALL

def new_text_callback(text):
    print(text, end="")

llama_model = "/home/su/Downloads/gpt4all/gpt4all-lora-quantized-converted.bin"
gj_model = '/home/su/Downloads/ggml-gpt4all-j.bin'

# model = GPT4ALL(gj_model)
model = GPT4ALL(llama_model)
model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)

if __name__ == '__main__':
    pass
