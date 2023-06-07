import openai
import os
import base64
import time

Key = "####"
openai.api_key = Key

class ImageGenerator:


    def CreateImage(self, user_input):  # Removed limit and Change() as parameters
        text = user_input
        ChatGPT_Image = openai.Image.create(pr1ompt = text, n = 3, size = "1024x1024", response_format = "b64_json")
        for i in range(0, len(ChatGPT_Image['data'])):
            b64 = ChatGPT_Image['data'][i]['b64_json']
            filename = f'image_image_WithoutChatGPT__{i}.png'
            with open(filename, 'wb') as f:
                f.write(base64.urlsafe_b64decode(b64))
        

    def Change(self, limit):  # Removed limit as a parameter
        user_changedescription_input = input("Write a description on your new image: ")
        return user_changedescription_input
        

#    def Continue(self, user_change):  # Removed limit and CreateImage() as parameters
  #      if(self.limit == 3):
 #           return "Sorry reached Limit"
   #     else:
#            return self.CreateImage(user_change)  # Call CreateImage() with user_change as argument

user_limit = int(input("How many times do you want to run?"))
if user_limit < 1:
    exit(0)
part3 = ImageGenerator()  # Create an instance of Part3
user_input = input("Describe an image you want Dall-E to create.")
image_url = part3.CreateImage(user_input)
for i in range(0, user_limit-1):
    user_change = part3.Change(i)  # Call Change() on the instance
    part3.CreateImage(user_change)
#part3.Continue(user_change)  # Call Continue() on the instance
