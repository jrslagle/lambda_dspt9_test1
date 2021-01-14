import pandas as pd

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

def null_count(df) -> int:
    # the total number of nulls in a dataframe as an int
    return df.isna().sum().sum()

def year_month_day(raw_dates):
    # Convert to datetime64[ns] if possible
    datatype = raw_dates.dtype
    if datatype == 'object':
        dates = pd.to_datetime(raw_dates, infer_datetime_format=True)
    elif datatype == 'datetime64[ns]':
        dates = raw_dates
    else:
        assert False, f"Dates must either be type object or datetime64[ns], not {datatype}"

    # Extract components and return
    return pd.DataFrame({
        'year':dates.dt.year,
        'month':dates.dt.month,
        'day':dates.dt.day})

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))