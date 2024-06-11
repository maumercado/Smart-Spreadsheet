# Smart Spreadsheet AI CLI

Smart Spreadsheet AI CLI is a command-line interface (CLI) tool that processes Excel files, normalizes their data, and allows users to interact with the data using OpenAI's language model. The tool is designed to help users query their Excel data conversationally.

## Features

- Load and normalize Excel files
- Interact with the data using natural language queries
- Maintain conversation context for coherent interactions
- Display loading spinners during processing and querying

## Requirements

- Python 3.7 or above
- The following Python libraries:
  - `pandas`
  - `openai`
  - `python-dotenv`
  - `yaspin`
  - `argparse`

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/maumercado/Smart-Spreadsheet.git
   cd Smart-Spreadsheet
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python3 -m venv smartsheet
   source smartsheet/bin/activate  # On Windows, use `smartsheet\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the OpenAI API key:**
   - Create a `.env` file in the root directory of the project with the following content:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

To use the CLI, run the `main.py` script with the required flags:

```sh
python main.py -f file1.xlsx file2.xlsx
```

### Example

```sh
python main.py -f data1.xlsx data2.xlsx
```

After processing the files, you can interact with the data by entering your queries in the console:

```sh
You: What is the total sales for 2023?
OpenAI: The total sales for 2023 are ...
```

To exit the interaction, type `quit` or `exit`.

## Demo

![ezgif-6-5504ccf339](https://github.com/maumercado/Smart-Spreadsheet/assets/282004/ae78d8f7-feaf-4824-b5b2-96b7a63d3c76)


## Directory Structure

```
smart_spreadsheet_ai/
├── main.py
├── openai_client.py
├── data_processing.py
├── cli.py
├── .env.example
├── requirements.txt
└── README.md
```

### File Descriptions

- `main.py`: Entry point of the application.
- `openai_client.py`: Handles interaction with the OpenAI API.
- `data_processing.py`: Handles data loading and normalization.
- `cli.py`: Handles the command-line interface logic.
- `.env.example`: Example `.env` file to set up the OpenAI API key.
- `requirements.txt`: Lists all the dependencies for the project.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
