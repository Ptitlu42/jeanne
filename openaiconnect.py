import opena

GPT_KEY = ""
openai.api_key = GPT_KEY

while True:
    prompt = input("Prompt:")

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    response = response.choices[0].text.strip()
    print(response)