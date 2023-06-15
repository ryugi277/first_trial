""" 
Utility functions for interacting with the database.
Including:
1. connect to the database
2. Create Table kamus alay & Abusive
3. Insert Result of data cleansing 
"""
import pandas as pd
import sqlite3

def create_connection():
    conn = sqlite3.connect('gold_challenge.db')
    return conn

def insert_dictionary_to_db(conn):
    abusive_csv_file = "csv_data/abusive.csv"
    alay_csv_file = "csv_data/alay.csv"
    
    # Read csv file to dataframe
    print("Reading csv file to dataframe...")
    df_abusive = pd.read_csv(abusive_csv_file)
    df_alay = pd.read_csv(alay_csv_file, delimiter="\t")
    print(df_alay)
    
    # Standardize column name
    df_abusive.columns = ['word']
    df_alay.columns = ['alay_word', 'formal_word']
    
    # Insert dataframe to database
    print("Inserting dataframe to database...")
    df_abusive.to_sql('abusive', conn, if_exists='replace', index=False)
    df_alay.to_sql('alay', conn, if_exists='replace', index=False)
    print("Inserting dataframe to database success!")
    
def insert_result_to_db(conn, raw_text, clean_text):
    # Insert result to database
    print("Inserting result to database...")
    df = pd.DataFrame({'raw_text': [raw_text], 'clean_text': [clean_text]})
    df.to_sql('cleansing_result', conn, if_exists='append', index=False)
    print("Inserting result to database success!")
    
def insert_upload_result_to_db(conn, clean_df):
    # Insert result to database
    print("Inserting result to database...")
    clean_df.to_sql('cleansing_result', conn, if_exists='append', index=False)
    print("Inserting result to database success!")
    
    
def show_cleansing_result(conn):
    # Show cleansing result
    print("Showing cleansing result...")
    df = pd.read_sql_query("SELECT * FROM cleansing_result", conn)
    return df.T.to_dict()
    