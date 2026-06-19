import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info('Starting the csv validator')
    try:
        df = pd.read_csv('csv_validator/data/test_data/test_data.csv')
        logging.info('CSV file loaded successfully')
        logging.debug('CSV file head')
        df.head()
        
        # Perform validation checks
        if df.isnull().any().any():
            logging.warning('CSV file contains missing values')
        else:            
            logging.info('CSV file does not contain any missing values')
    except Exception as e:
        logging.error(f'Error loading CSV file: {e}')