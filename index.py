import json
import os
import time
import random

import gradio as gr
import requests
from PIL import Image


URL = "http://127.0.0.1:8188/prompt"
INPUT_DIR = r"C:/ComfyUI/ComfyUI_windows_portable/ComfyUI/input"
OUTPUT_DIR = r"C:/ComfyUI/ComfyUI_windows_portable/ComfyUI/output"
cached_seed = 0

def get_latest_image(folder):
    """Get the latest generated image from the output directory."""
    files = os.listdir(folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    return latest_image

def start_queue(prompt_workflow):
    """Send a request to start the image generation workflow."""
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    requests.post(URL, data=data)

def generate_image(prompt_text):
    """Generate an image based on the provided text prompt."""
    with open("workflow (1).json", "r") as file_json:
        prompt = json.load(file_json)

    prompt["6"]["inputs"]["text"] = prompt_text   
    prompt["3"]["inputs"]["seed"] = random.randint(1, 1500000)

    global cached_seed
    if cached_seed == prompt["3"]["inputs"]["seed"]:
        return get_latest_image(OUTPUT_DIR)
    cached_seed = prompt["3"]["inputs"]["seed"]
    
    start_queue(prompt)

    previous_image = get_latest_image(OUTPUT_DIR)
    
    while True:
        latest_image = get_latest_image(OUTPUT_DIR)
        if latest_image != previous_image:
            return Image.open(latest_image)

        time.sleep(1)


demo = gr.Interface(
    fn=generate_image, 
    inputs=gr.Textbox(label="Enter your text prompt"), 
    outputs=gr.Image(label="Generated Image"),
    title="Text2Img Generation" 
)


demo.launch(share=True)