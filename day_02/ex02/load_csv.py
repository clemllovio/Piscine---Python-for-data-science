import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file from the specified path into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(path, index_col=0)
        shape = data.shape
        print(f"Loading dataset of dimensions: {shape}")
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
