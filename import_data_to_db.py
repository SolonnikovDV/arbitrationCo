import sqlite3
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
import config as cfg

# importing data from excel file to sqlite
class ImportDataToDb:
    @classmethod
    def import_data_from_excel(cls, file, db_path, db_table_name):
        df = pd.read_excel(file)
        engine = create_engine(db_path)
        df.to_sql(db_table_name, con=engine, if_exists='replace', index=False)

    @classmethod
    def insert_variable_into_table(
            cls,
            field_owner,
            field_contract_subject,
            field_registry_number,
            field_contract_price,
            field_portal,
            field_complainant_name,
            field_complaint_date,
            field_complainant_subject,
            field_status,
            field_grounds_refusal,
            field_date_withdraw,
            field_result,
            feld_concideration_date,
            field_vote_accept,
            field_vote_reject,
            field_vote_hold,
            field_path):
        try:
            sqlite_connection = sqlite3.connect(cfg.db_file_name)
            cursor = sqlite_connection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO arbitrationDb
                    (
                    'Заказчик', 
                    'Наименовние закупки', 
                    'Номер в ЕИС', 
                    'НМЦК', 
                    'Оператор ЭТП', 
                    'Заявитель, краткое наименование, ИНН', 
                    'Дата обращения', 
                    'Суть обращения', 
                    'Статус _принято/отказ', 
                    'Основание отказа', 
                    'Дата отзыва обращения', 
                    'Результат _рассматривается, подведены итоги', 
                    'Дата рассмотрения', 
                    'Голосов ЗА', 
                    'Голосов ПРОТИВ', 
                    'Голосов ВОЗДЕРЖАЛСЯ', 
                    'Ссылка на итоги'
                    ) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

            data_tuple = (
                field_owner,
                field_contract_subject,
                field_registry_number,
                field_contract_price,
                field_portal,
                field_complainant_name,
                datetime.strptime(field_complaint_date, "%d-%m-%Y"),
                field_complainant_subject,
                field_status,
                field_grounds_refusal,
                field_date_withdraw,
                field_result,
                datetime.strptime(feld_concideration_date, "%d-%m-%Y"),
                field_vote_accept,
                field_vote_reject,
                field_vote_hold,
                field_path
            )
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqlite_connection.commit()
            print("Python Variables inserted successfully into SqliteDb_developers table")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("The SQLite connection is closed")
