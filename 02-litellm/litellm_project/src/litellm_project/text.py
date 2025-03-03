from litellm import completion
import os

# set ENV variables
os.environ["GEMINI_API_KEY"] = "AIzaSyB8RQ10xhcAtzUs70YscSGx7IBbOJYWMIU"


def gemini_15_flash():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response)
    print("Print Content")
    print(response['choices'][0]['message']['content'])


def gemini_15_flash_pro():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response)


def main():
    print("Running first func")
    gemini_15_flash()
    print("Running second func")
    gemini_15_flash_pro()
