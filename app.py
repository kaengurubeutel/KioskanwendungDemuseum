import eel
import base64
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from PIL import Image
import numpy as np
import torch
import io
from deep_translator import GoogleTranslator




# load the ML models and build them into a pipeline

controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-scribble", torch_dtype=torch.float32
).to('cpu')

pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", controlnet=controlnet, 
).to('cpu')

pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
#prompts for testing
prompt = "a wide landscape"
negative_prompt = "monochrome, lowres, bad anatomy, worst quality, low quality"

#encodes base64 Strings into Pillow Image Objects (helperfunction)
def decode_img(input):
    input = input[input.find(",")+1:]
    b = base64.b64decode(input)
    img = Image.open(io.BytesIO(b))
    return img
 

#test if framework works properly
@eel.expose
def hello_world():
    print("Hello from python")

@eel.expose
def get_greeting(string):
    return f"hello {string}"


#part of the backend, which has the ML logic @Todo: add prompt
@eel.expose
def get_image(imageStr):
    #print (imageStr)
    print("\n . \n . \n Gib einen Prompt ein: ")
    prompt = str(input())
    txttmp =GoogleTranslator(source='de', target='en').translate(prompt)
    print(txttmp)
    img = decode_img(imageStr)
    img = img.resize((750, 400))
    result = pipe(txttmp, img, num_inference_steps=3, guidance_scale=15.0).images[0]
    result.show()
    return




#starting the Framework in chromium
eel.init("web")
eel.start("index.html")
