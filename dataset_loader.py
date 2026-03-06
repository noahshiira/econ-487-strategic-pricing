import pandas as pd
import polars as pl

def load_oj_csv(user, repo, file, branch="main"):
    """
    Load CSV directly from GitHub repository
    """
    
    url = f"https://raw.githubusercontent.com/noahshiira/econ-487-strategic-pricing/refs/heads/main/datasets/oj.csv"
    
    data_oj = pl.read_csv(url)
    return data_oj


if __name__ == "__main__":
    
    data_oj = load_oj_csv(
        user="noahshiira",
        repo="econ-487-strategic-pricing",
        file="oj.csv"
    )

    print(data_oj.head())

