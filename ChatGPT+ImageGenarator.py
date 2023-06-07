import openai
import base64
import time

openai.api_key = "####"

class Chat:
    def __init__(self):
        self.messages = []
        self.initialDescription = ("You are going to Enhance the following Description in a way that it can be used to generate an image: "
                                   "Description: the ball falling from the leaning tower of pisa. "
                                   "You will respond with In the heart of Italy, a vibrant, sun-kissed ball descends rapidly from the apex of the iconic, "
                                   "architecturally askew Leaning Tower of Pisa. The ball, caught mid-fall, contrasts dramatically against the azure sky "
                                   "and ancient stone edifice, casting a fleeting shadow on the sunlit tower. Framed by verdant greenery and an awestruck audience, "
                                   "this singular moment blends the simplicity of gravity with the grandeur of historical architecture.")
        self.messages.append({"role": "system", "content": self.initialDescription})
    def get_enhanced_description(self, user_description):
        self.messages.append({"role": "user", "content": user_description})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": reply})
        return reply

class ImageGeneratorConnection:
    def CreateImage(self, user_input):
        ChatGPT_Image = openai.Image.create(prompt = user_input, n = 3, size = "1024x1024", response_format = "b64_json")
        for i in range(0, len(ChatGPT_Image['data'])):
            b64 = ChatGPT_Image['data'][i]['b64_json']
            filename = f'image_{int(time.time())}_{i}.png'
            with open(filename, 'wb') as f:
                f.write(base64.urlsafe_b64decode(b64))
                return filename
    def CreateVariation(self, variation1):
        ChatGPT_Image_Variation = openai.Image.create_variation(image = open(variation1, "rb"), n = 1, size = "1024x1024", response_format = "b64_json")
        for i in range(0, len(ChatGPT_Image_Variation['data'])):
            b64 = ChatGPT_Image_Variation['data'][i]['b64_json']
            filename = f'image_Variation_{i}.png'
            with open(filename, 'wb') as f:
                f.write(base64.urlsafe_b64decode(b64))
                return filename
chat_model = Chat()
ImageGenerate = ImageGeneratorConnection()
user_description = input("Describe the image you want or respond no to stop: ")
if user_description.strip().lower() == "no":
    quit()
number = 0
while True:
    if(number != 0):
        user_description = input("Do you want a different variation of the image?(Respond with Yes or No)")
        if user_description.strip().lower() == "No":
            quit()
        else:
            print("New Variation incoming")
            NewFilename = ImageGenerate.CreateVariation(NewFilename)

    else:
        number = 1
        enhanced_description = chat_model.get_enhanced_description(user_description)
        print(enhanced_description)
        Filename = ImageGenerate.CreateImage(enhanced_description)
        print(Filename)
        NewFilename = Filename
