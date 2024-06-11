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
  Generate an answer to a user query based on provided tables and history.

  Args:
      query (str): The user's query.
      tables (dict): A dictionary of tables, where the keys are sheet names and the values are CSV data.
      history (list): A list of messages exchanged between the user and the assistant.

  Returns:
      str: The assistant's answer to the user's query.

  This function combines all the tables into a single string, constructs the message history for the chat model,
  and sends it to the OpenAI GPT-3.5-turbo-1106 model for completion. The resulting answer is appended to the
  history and returned.

  The combined CSV data is constructed by joining each table with a newline separator and a table number.
  The initial message content is a system message that provides an introduction to the assistant and the provided
  CSV data. The messages list is constructed by appending the initial message, the history, and the user's query.
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
      f"You are a helpful accountant assistant. Based on the provided CSV data below, answer the user's questions. "
      f"Provide detailed explanations and perform complex calculations if needed.\n\n{combined_csv}\n\n"
    )
  }

  messages = [initial_message] + history
  messages.append({"role": "user", "content": query})

  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=messages,
    temperature=0.2
  )

  answer = response.choices[0].message.content
  history.append({"role": "user", "content": query})
  history.append({"role": "assistant", "content": answer})

  return answer
