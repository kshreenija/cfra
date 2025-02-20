import pandas as pd 
import os
def excel_to_csv():
    excel1 = '/home/shreenija/Downloads/state_sg-20250212T095127Z-001/state_sg/holdings-daily-sg-en-d07.xlsx'
    excel2 = '/home/shreenija/Downloads/state_sg-20250212T095127Z-001/state_sg/holdings-daily-sg-en-es3.xlsx'
    excel3 = '/home/shreenija/Downloads/state_sg-20250212T095127Z-001/state_sg/holdings-daily-sg-en-s27.xlsx'
    excel_sheets = [excel1,excel2,excel3]

    column_headers={
        'Name':'constituent_name',
        'Weight (%)' : 'weighting_sponsor',
        'Identifier' : 'constituent_ticker',
        'ISIN' : 'isin',
        'SEDOL' : 'sedol',
        'Shares Held' : 'quantity_held',
        'Base Market Value' : 'market_value_held',
        'Local Currency' : 'local_currency',
        'Local Price' : 'local_price', 'Holdings As of' : 'as_of_date'
    }
    dataframe = []
    for excel in excel_sheets:
        df = pd.read_excel(excel)
        df.rename(columns=column_headers, inplace=True)
        if 'weighting_sponsor' in df.columns:
            df['weighting_sponsor']= df['weighting_sponsor']/100
        dataframe.append(df)
        
    combined_df = pd.concat(dataframe, ignore_index=True)    

    script_path = __file__
    root, filename = os.path.split(script_path)
    download_folder = os.path.join(root, filename.split(".")[0])
    os.makedirs(download_folder, exist_ok=True)

    output_csv=os.path.join(download_folder,"combined.csv")
    combined_df.to_csv(output_csv,index=False)
excel_to_csv()
