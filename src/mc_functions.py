import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def oy_df(df):
    '''Creates dataframe that meets the conditions of Opportunity Youth

    Creates a dataframe of only the observations that qualify
    as Opportunity Youth from the dataframe given from parameter.
    To qualify as Opportunity Youth, the sch column must equal 1 
    and the esr column must equal either 3 or 6.

    Args:
        df: A dataframe containing information on individuals 
            from the imported sql database
    
    Returns:
        df[mask]: A new dataframe containing information on the 
            individuals from df who meet the conditions of
            Opportunity Youth
    '''
    # Set conditions for data I want in returned dataframe
    mask = (
        (df['sch'] == '1') &
        ((df['esr'] == '3') | (df['esr'] == '6'))
    )
    return df[mask]

def data_import():
    '''Imports data from sql database

    Retrieves necessary sql databased and returns it as 
    a Pandas Dataframe. Only returns columns pertaining to specific
    analysis and rows that meet initial conditions.

    Returns:
        df: A pandas DataFrame with columns serialno, puma, pwgtp, agep, sch, and esr
            and rows where age is between 16 and 24 (initial condition for Opportunity Youth)

    '''
    # Import table from sql
    DBNAME = 'opportunity_youth'
    conn = psycopg2.connect(dbname=DBNAME)

    #Select required columns 
    df = pd.read_sql('''
    SELECT serialno, puma, pwgtp, agep, sch, esr
    FROM pums_2017
    WHERE agep BETWEEN 16 and 24;
    ''', conn)

    # Return df
    return df

def create_puma_dict(df, pumas):
    '''Creates a dictionary of number of people from df in each puma from pumas list

    Creates a dictionary with the total number of people in each
    puma from the puma list by utilizing the weight column in given dataframe

    Args:
        df: A pandas dataframe containing information on individuals
            within a puma code
        pumas:
            A list of pumas that will be the keys for the dictionary

    Returns:
        d: A dictionary with keys as the pumas from given pumas list and
            values as total number of people in that given puma. Dictionary
            is sorted by value.
    '''
    # Empty dict
    d = {}

    # loop through dataframe
    for index, row in df.iterrows():
        # Check if puma is in the parameter pumas list
        if row['puma'] in pumas:
            if row['puma'] in d:
                d[row['puma']] += row['pwgtp']
            else:
                d[row['puma']] = row['pwgtp']
    # Return sorted dict
    return {k:v for k, v in sorted(d.items(), key=lambda x: x[1])}

def create_plot_from_dict(d, l, p):
    '''Creates bar plot from given dictionary

    Creates a bar plot from the passed in dictionary with the key as x value
    and the values of the dictionary as the y values. The plot is labeled 
    according to the parameter l and the bar colors correspond to the puma codes
    in the parameter p.

    Args:
        d: The dictionary to be plotted on the bar plot
        l: List of labels to put on the graph. First index is plot title,
            second index is x-axis label and third index is y-axis label
        p: A list of certain pumas that are to be highlighted on the 
            plot in a different color

    Returns:
        Doesn't return anything, but creates a plot from given parameters.
    '''
    # Set style and figsize
    sns.set_style('white')
    sns.set_context({'figure.figsize': (15, 10)})

    # Set x and y values
    x = [i[0] for i in d.items()] # x is puma code from sorted_d
    y = [i[1] for i in d.items()] # y is the value corresponding to puma code

    # Create color list
    colors = []
    for idx in d.items():
        puma = idx[0]
        if puma in p:
            colors.append('#A8DADC')
        else:
            colors.append('#1D3557')

    # Create plot
    splot = sns.barplot(x, y, order=x, palette=colors)

    # Set font_scale
    sns.set(font_scale=1.5)

    # Set title and labels
    splot.set_title('{}'.format(l[0]), fontsize = 25)
    splot.set_xlabel('{}'.format(l[1]), fontsize = 22)
    splot.set_ylabel('{}'.format(l[2]), fontsize = 22)
    splot.set_xticklabels(x, rotation=30)

    # Create legend
    labels = ['South King County', 'Other King County']
    n = []
    n.append(splot.bar(0, 0, color = '#A8DADC'))
    n.append(splot.bar(0, 0, color = '#1D3557'))
    splot.legend(n, labels, loc='0', fontsize=18);