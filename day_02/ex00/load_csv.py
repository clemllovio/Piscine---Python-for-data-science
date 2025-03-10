import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file from the specified path into a pandas DataFrame.
    """
    try:
        if path[-4:] != '.csv':
            raise ValueError(f'Expected a .csv file, got {path}')
        data = pd.read_csv(path, index_col=0)
        print(f"Loading dataset of dimensions: {data.shape}")
        return data
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return None
