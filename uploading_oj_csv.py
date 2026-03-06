import pandas as pd

def load_oj_csv(user, repo, file, branch="main"):
    """
    Load CSV directly from GitHub repository
    """
    
    url = f"https://raw.githubusercontent.com/noahshiira/econ-487-strategic-pricing/refs/heads/main/datasets/oj.csv"
    
    df = pd.read_csv(url)
    return df


if __name__ == "__main__":
    
    df = load_oj_csv(
        user="noahshiira",
        repo="econ-487-strategic-pricing",
        file="oj.csv"
    )

    print(df.head())
