import pandas as pd


def get_percent(
    df: pd.DataFrame, cat_col: str, group_col: str = "week"
) -> pd.DataFrame:
    total_group = df.groupby([group_col].size().reindex(week_range, fill_value=0))
    total_group_cat = df.groupby([group_col]).size().unstack(fill_value=0)
    percent_group = total_group.div(total_group_cat, axis=0).reset_index()

    return percent_group
