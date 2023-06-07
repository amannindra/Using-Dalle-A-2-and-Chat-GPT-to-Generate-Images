import openai


class NoChatIncluded:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key 
    def get_description(self):
        user_input = input("Please enter a description: ")
        return user_input
    
    def enhance_description(self):
        user_input = self.get_description()
        messages = [{"role": "system", "content": "ChatGPT is responding"}]
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Enhance the following description in a way that Dalle-2 can create an image out of it.:\n{user_input}",
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        ChatGPT_reply = response.choices[0].text
        messages.append({"role": "user", "content": user_input})
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
TestCode = NoChatIncluded("####")
ChatGPTresponce = TestCode.enhance_description()
print(ChatGPTresponce)