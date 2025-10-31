import openai
import google.colab import userdata


#Openai Access-Key definieren
openai.api_key = userdata.get('openai.api_key')

def chat_with_gpt(promt):
  response = openai.ChatCompletion.create(
      model="gpt-5-nano",
      messages=[{"role": "user", "content": prompt}]
  )

  return response.choice[0].message.content.strip()

if __name__ = "__main__":
  while True:
    if user_input.lower() in ["quit", "exit", " bye"]:
      break

    response = caht_with_gpt(user_input)
    print("Chatbot:")