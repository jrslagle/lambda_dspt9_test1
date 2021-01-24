def enlarge(n):
    """
    Multiply a number by 100.

    :param n: the number to enlarge
    :returns: the number multiplied by 100
    """
    return n * 100


def null_count(df) -> int:
    """
    Get the total number of nulls in a dataframe

    :param df: the pandas DataFrame to inspect
    :returns: The total number of nulls as an int
    """
    import pandas as pd
    return df.isna().sum().sum()


def year_month_day(raw_dates):
    """
    Split a date column into three columns: Year, Month, Day

    :param raw_dates: a Series of dates as type string or datetime64[ns]
    :returns: A DataFrame with columns ['year', 'month', 'day']
    """
    # Convert to datetime64[ns] if possible
    import pandas as pd
    datatype = raw_dates.dtype
    if datatype == 'object':
        dates = pd.to_datetime(raw_dates, infer_datetime_format=True)
    elif datatype == 'datetime64[ns]':
        dates = raw_dates
    else:
        assert False, f"Dates must either be type object or datetime64[ns], not {datatype}"

    # Extract components and return
    return pd.DataFrame({
        'year': dates.dt.year,
        'month': dates.dt.month,
        'day': dates.dt.day})


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))
