import requests
import json
import argparse

def send_prompt(content):
    url = "http://localhost:8000/api/chat"

    data = {
            "model": "qwen2:0.5b", 
            "messages": [
                {
                "role": "user",
                "content": f"Summarize the following text : {content}"
                },
            ],
            "stream" : True  
    }

    response = requests.post(url, json=data , stream=True)
    print(response.status_code)
    if response.status_code == 200:

        full_response = ''
        for line in response.iter_lines():
            if line:
                try:
                    json_object = json.loads(line)
                    if 'message' in json_object and 'content' in json_object['message']:
                        chunk = json_object['message']['content']
                        full_response += chunk
                        print(chunk , end='' , flush=True)
                except json.JSONDecodeError:
                    pass
        print()
        return full_response

    else:
        print(f"Error: {response.status_code}")
        return response.text

def main():
    parser = argparse.ArgumentParser(description="Summarize text or text file content.")
    parser.add_argument('-t', '--textfile', type=str, help="Path to the text file to summarize.")
    parser.add_argument('-s', '--string', type=str, help="Text string to summarize.")

    args = parser.parse_args()

    if args.textfile:
        try:
            with open(args.textfile, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: The file {args.textfile} does not exist.")
            return
    elif args.string:
        content = args.string
    else:
        print("Error: You must provide either a text file (-t) or a text string (-s).")
        return

    summary = send_prompt(content)
    print("Summary:")
    print(summary)

if __name__ == "__main__":
    main()
