import argparse
from pathlib import Path
from yaspin import yaspin
from data_processing import process_excel
from openai_client import answer_query

def run_cli():
  parser = argparse.ArgumentParser(description="Smart Spreadsheet AI CLI")
  parser.add_argument("-f", "--files", nargs='+', required=True, help="Excel files to process")
  parser.add_argument("-s", "--streaming", action='store_true', help="Enable streaming response from OpenAI")
  args = parser.parse_args()

  for file_path in args.files:
    if not Path(file_path).is_file():
      print(f"Error: File '{file_path}' does not exist.")
      return

  all_tables = {}
  with yaspin(text="Processing files", color="cyan") as spinner:
    for file_path in args.files:
      normalized_tables = process_excel(file_path)
      all_tables.update(normalized_tables)
    spinner.ok("✔")  # Mark the spinner as completed successfully

  print("Files processed successfully. You can now ask questions about the data.")
  print("(press enter to send query or type 'quit' to exit)")

  conversation_history = []

  while True:
    user_query = input("\nYou: ")
    if user_query.lower() in ['quit', 'exit']:
      print("Exiting...")
      break
    with yaspin(text="Generating answer...", color="cyan") as spinner:
      spinner.hide()
      print("OpenAI: ", end="", flush=True)
      for chunk in answer_query(user_query, all_tables, conversation_history):
        print(chunk, end="", flush=True)
      print("\n")
