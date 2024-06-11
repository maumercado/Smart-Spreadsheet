import pandas as pd

def load_excel(file_path):
  """
  Load an Excel file into a pandas dataframe.

  Args:
      file_path (str): The path to the Excel file.

  Returns:
      pandas.ExcelFile: The loaded Excel file.
  """
  return pd.ExcelFile(file_path)

def normalize_column_names(df):
  """
  Normalize column names in a pandas dataframe.

  Args:
      df (pandas.DataFrame): The dataframe to normalize column names in.

  Returns:
      pandas.DataFrame: The dataframe with normalized column names.
  """
  df.columns = [str(col).strip().lower().replace(' ', '_') for col in df.columns]
  return df

def convert_data_types(df):
  """
  Convert data types in a pandas dataframe.

  Args:
      df (pandas.DataFrame): The dataframe to convert data types in.

  Returns:
      pandas.DataFrame: The dataframe with data types converted.
  """
  for col in df.columns:
    if not pd.api.types.is_datetime64_any_dtype(df[col]):
      df[col] = df[col].astype(str)
  return df

def handle_missing_values(df):
  """
  Handle missing values in a pandas dataframe.

  Args:
      df (pandas.DataFrame): The dataframe to handle missing values in.

  Returns:
      pandas.DataFrame: The dataframe with missing values handled.
  """
  df.fillna('missing', inplace=True)
  return df

def remove_empty_rows_and_columns(df):
  """
  Remove empty rows and columns from a pandas dataframe.

  Args:
      df (pandas.DataFrame): The dataframe to remove empty rows and columns from.

  Returns:
      pandas.DataFrame: The dataframe with empty rows and columns removed.
  """
  df.dropna(how='all', inplace=True)
  df.dropna(how='all', axis=1, inplace=True)
  return df

def normalize_table(df):
  """
  Normalize a table in a pandas dataframe.

  Args:
      df (pandas.DataFrame): The table to normalize.

  Returns:
      pandas.DataFrame: The normalized table.
  """

  df = normalize_column_names(df)
  df = convert_data_types(df)
  df = handle_missing_values(df)
  df = remove_empty_rows_and_columns(df)
  return df

def process_excel(file_path):
  """
  Process an Excel file and return a dictionary of normalized tables.

  Args:
      file_path (str): The path to the Excel file.

  Returns:
      dict: A dictionary of normalized tables, where the keys are sheet names and the values are normalized dataframes.
  """
  excel = load_excel(file_path)
  normalized_tables = {}
  for sheet in excel.sheet_names:
    df = pd.read_excel(excel, sheet)
    normalized_df = normalize_table(df)
    normalized_tables[sheet] = normalized_df.to_csv(index=False)
  return normalized_tables
