import pandas as pd

def load_dataset_from_github(url: str):
    """
    Loads a dataset directly from a GitHub raw URL.
    
    Parameters
    ----------
    url : str
        Raw GitHub file URL

    Returns
    -------
    pandas.DataFrame
    """
    
    df = pd.read_csv(url)
    return df