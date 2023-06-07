# Using-Dalle-A-2-and-Chat-GPT-2-to-Generate-Images
ChatGPT+ImageGenator.py
This code is a fusion of elements sourced from OpenAI's official documentation and educational YouTube videos. While not entirely original, 
I've thoughtfully curated and integrated these elements to construct a user-friendly application that caters to the intended purpose.
This code allows users to interactively generate images from textual descriptions using OpenAI's GPT-3.5-turbo model and an image creation module. 
The user provides a description which the AI model enhances for more detail and clarity. This amplified description is then used as a prompt for the
image creation module, generating an image that closely matches the user's intent. The user can continuously provide new descriptions to generate different
images. The process continues until the user explicitly opts to stop, thereby providing a flexible and interactive tool for translating textual descriptions into visual content.

ConversationChatGPTwithGUI.py
This code is not made by me. Creater of code is from https://www.youtube.com/watch?v=pGOyw_M1mNE&t=631s&ab_channel=TheAIAdvantage
I just tweaked a few things

This script sets up an interactive chat with GPT-3.5-turbo model using Gradio, a Python library for creating a user interface. 
The chat is specifically designed to simulate a conversation with a financial expert that specializes in real estate investment 
and negotiation. The user can input text, which gets appended as a user message to the system and user conversation history. The 
conversation history is sent to OpenAI's GPT-3.5-turbo model, which generates a corresponding assistant message that's added to the
conversation history. The assistant's response is displayed on the Gradio interface. This continues in a conversational loop, 
providing an interactive chat experience for the user.

ImageGenarator.py
Again this code isn't fully made by me, rather copyed from Youtube videos and documentation. I only put the code together so that it can run properly.
https://www.youtube.com/watch?v=q1-7KMHWju4&t=926s&ab_channel=ParametricCamp

This script employs OpenAI's API to generate images based on user-provided descriptions. The class ImageGenerator defines two methods.
The CreateImage method receives the user's description, sends it to OpenAI's Image model (like DALL-E), and generates images corresponding 
to the description. The images are saved in the same directory as the script. The Change method provides the user with the ability to input 
a new description for generating new images. The user is also asked how many times they want the script to run, allowing them to generate
multiple images in one session.

NonConversationChatGPt.py
Same as the previous ones, copyed some documentation and youtube videos to create this code.
This script works with OpenAI's DaVinci engine to enhance the user-provided descriptions. 
The class NoChatIncluded consists of two methods. The get_description method prompts the user to input 
a description. The enhance_description method takes this description and uses OpenAI's DaVinci engine to
generate an enhanced version. The enhanced description is intended to be more detailed and clear, suitable 
for generating an image. The user's input and the enhanced description are treated as a conversation with the
assistant, making it easy to view the original and the enhanced description side by side.







