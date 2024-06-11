from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

open_api_key = os.environ.get('OPENAI_API_KEY')

try:
  client = OpenAI(
    api_key=open_api_key
  )
except Exception as e:
  print("This requires an OpenAI API key, please set it in the .env file as 'OPENAI_API_KEY'. Error", e)

def answer_query(query, tables, history):
  """
  Answer a query using the OpenAI chat model.

  Args:
    query (str): The query to answer.
    tables (dict): A dictionary of tables, where the keys are sheet names and the values are CSV data.
    history (list): A list of messages in the conversation history.

  Returns:
    str: The answer to the query.
  """

  try:
    combined_csv = "\n\n".join([f"Table {i+1}:\n{csv_data}" for i, (sheet, csv_data) in enumerate(tables.items())])
  except Exception as e:
    print(f"Error combining CSV data: {e}")
    return "Error combining CSV data."

  # Construct the message history for the chat model
  initial_message = {
    "role": "system",
    "content": (
      f"You are a helpful accountant assistant. Based on the provided CSV data below, answer the user's questions.\n\n"
      f"The currency is in USD but you can ask the user to provide currency in any other format.\n\n"
      f"Provide detailed explanations and perform complex calculations if needed.\n\n{combined_csv}\n\n"
    )
  }

  messages = [initial_message] + history
  messages.append({"role": "user", "content": query})

  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=messages,
    temperature=0.2,
    stream=True
  )
  answer = ""
  for chunk in response:
    content = chunk.choices[0].delta.content
    if content is not None:
      answer += content
      yield content

  history.append({"role": "user", "content": query})
  history.append({"role": "assistant", "content": answer})
