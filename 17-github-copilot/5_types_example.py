import pandas as pd

def get_first_customers_age(df: pd.DataFrame):
    """Get the age of the first customer in the dataframe.

    Args:
        df (pd.DataFrame): The dataframe to get the age of the first customer from.

    Returns:
        int: The age of the first customer in the dataframe.
    """
    return df.iloc[0]["age"]
    