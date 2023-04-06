import tkinter as tk
#import requests
import openai
#from pprint import pprint

def generate_output():
    tense = tense_entry.get()
    topic = topic_entry.get()
    request = request_entry.get()
    print([tense,topic,request]) 
    openai.api_key = "OPEN_AI_API_KEY"
    
    output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    #{"role": "system", "content": "Generate"},
    #{"role": "user", "content": "English text"},
    #{"role": "assistant", "content": "exercise for tenses"},
    {"role": "user", "content": f"Prepare a student exercise to train {tense} with blank spaces to fill in. Make it about {topic}. {request}"},
    #{"role": "user", "content": "write code to solve linear programe problem of three constraints "}
    ]
    )
    print(output['choices'][0]['message']['content'])
    #print(output)
    f = open("english_tool_ex", "w")
    f.write(output['choices'][0]['message']['content'])
    f.close()
# Set up the GUI window
window = tk.Tk()
window.title("ChatGPT tool to prepare student exercises.")
window.geometry("1024x768")

# Set up the GUI elements
tense_label = tk.Label(window, text="Enter a tense (e.g. present simple, past continuous):")
tense_label.pack()
tense_entry = tk.Entry(window)
tense_entry.pack()

topic_label = tk.Label(window, text="Enter a topic (e.g. Python programming, tropical ecology):")
topic_label.pack()
topic_entry = tk.Entry(window)
topic_entry.pack()

request_label = tk.Label(window, text="Enter a request (e.g. exercise, definition):")
request_label.pack()
request_entry = tk.Entry(window)
request_entry.pack()

generate_button = tk.Button(window, text="Generate output", command=generate_output)
generate_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

# Set up the OpenAI API endpoint
url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

window.mainloop()

