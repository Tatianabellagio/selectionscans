# file: retrieve_and_process_data_sites.py
import cdsapi
import xarray as xr
import pandas as pd
import sys
import ast
import pickle

with open('key_assignments.pkl', 'rb') as file:
    key_assignments_prec = pickle.load(file)

def retrieve_and_process_data(api_key, years, months, days, times, variable, ecotypes_df):
    cds = cdsapi.Client(url="https://cds.climate.copernicus.eu/api", key='31c8afc7-5139-4aec-ba9f-432084c01f8a')
    results = {}  # List to store results
    for index, row in ecotypes_df.iterrows():
        for year in years: ## one year at the time the max retrieving is 12000 item and one year has 8928
            lat, lon, ecotype = row['latitude'], row['longitude'], row['ecotype_id']
            area = [lat, lon, lat, lon]  # Small bounding box around each point
            filename = f'era5_ecotype_{ecotype}_{year}_{variable}.nc'
            cds.retrieve(
                'reanalysis-era5-single-levels', ## land so its 9 km grid 
                {
                    'product_type': 'reanalysis',
                    'variable': variable,
                    'year': year,
                    'month': months,
                    'day': days, 
                    'time': times,
                    'area': area,
                    'format': 'GRIB'
                },
                filename)

if __name__ == '__main__':
    api_key = sys.argv[1]
    variable = sys.argv[2]
    time_start = sys.argv[3]
    time_end = sys.argv[4]
    dataset = sys.argv[5]
    

    if variable == 'total_precipitation':
        with open('key_assignments.pkl', 'rb') as file:
            key_assignments = pickle.load(file)
        ecotypes_toretrieve = key_assignments[api_key]

    if variable == '2m_temperature':
        with open('key_assignments.pkl', 'rb') as file:
            key_assignments = pickle.load(file)
        ecotypes_toretrieve = key_assignments[api_key]
    
    years = list(range(int(time_start),int(time_end)))
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days = [str(i).zfill(2) for i in range(1, 32)]
    times = [f'{str(i).zfill(2)}:00' for i in range(24)]

    ## import any ecotype df that contains lat lon and an ecotype id 

    ecotypes_df = pd.read_csv(dataset)
    ecotypes_df = ecotypes_df[ecotypes_df['ecotype_id'].isin(ecotypes_toretrieve)]
    
    retrieve_and_process_data(api_key, years, months, days, times, variable, ecotypes_df)
