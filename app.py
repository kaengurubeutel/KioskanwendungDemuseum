import eel
import base64
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel, UniPCMultistepScheduler
from PIL import Image
import numpy as np
import torch
import io


# load the ML models and build them into a pipeline

controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-scribble", torch_dtype=torch.float16
)

pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", controlnet=controlnet, safety_checker=None, torch_dtype=torch.float16
)

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
    img = decode_img(imageStr)
    result = pipe("astronomical photo", img, num_inference_steps=20).images[0]
    result.show()
    return




#starting the Framework in chromium
eel.init("web")
eel.start("index.html")
