import json
import base64
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("gemini_web2api_module", "gemini_web2api.py")
gemini_web2api = importlib.util.module_from_spec(spec)
sys.modules["gemini_web2api_module"] = gemini_web2api
spec.loader.exec_module(gemini_web2api)

img_path = "/Users/majingyi/Downloads/IMG_5154.PNG"
try:
    with open(img_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    
    images = [{"url": f"data:image/png;base64,{img_b64}"}]
    print("Uploading image...")
    refs = gemini_web2api.resolve_images(images)
    print("Result:", refs)
except Exception as e:
    print("Error:", e)
