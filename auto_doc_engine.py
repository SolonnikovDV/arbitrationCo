import logging
import re

from docxtpl import DocxTemplate
from docx import Document
import os.path
import os, sys
from mailmerge import MailMerge
from datetime import date

import sql_connect
import sql_connect as conn
import config as cfg
from sklearn.feature_extraction.text import CountVectorizer


class AutoDoc:

    @staticmethod
    def fill_doc_test(doc_name):
        doc = DocxTemplate('raw_files/' + doc_name)
        context = {'field_portal': 'Высшая ЭТП'}
        doc.render(context)
        file = 'docs/final_' + doc_name
        doc.save(file)
        if os.path.exists(file):
            print('docs/final_' + doc_name + ' is successful created')
        else:
            print('docs/final_' + doc_name + ' not found')

    # @staticmethod
    def doc_of_accept_complaint(self, doc_name, number_db_item):
        # execute values from DB
        val_field_portal = conn.sql_connect().execute(
            'SELECT "Оператор ЭТП" from '
            + cfg.dB_table_name
            + ' WHERE "№ пп"='
            + number_db_item
        ).fetchone()[0]
        val_field_owner = conn.sql_connect().execute(
            'SELECT "Заказчик" from arbitrationDb WHERE "№ пп"=' + number_db_item
        ).fetchone()[0]
        val_field_complainant_name = conn.sql_connect().execute(
            'SELECT "Заявитель, краткое наименование, ИНН" from arbitrationDb WHERE "№ пп"=' + number_db_item
        ).fetchone()[0]
        val_field_complainant_subject = conn.sql_connect().execute(
            'SELECT "Суть обращения" from arbitrationDb WHERE "№ пп"=' + number_db_item
        ).fetchone()[0]
        val_field_concideration_date = conn.sql_connect().execute(
            'SELECT "Дата рассмотрения" from arbitrationDb WHERE "№ пп"=' + number_db_item
        ).fetchone()[0]
        date_of_concideration = val_field_concideration_date.split(' ')[0]

        # save the doc
        os.chdir(sys.path[0])
        doc = DocxTemplate("raw_files/" + doc_name)
        context = {
            'field_portal': val_field_portal,
            'field_owner': val_field_owner,
            'field_complainant_name': val_field_complainant_name,
            'field_complainant_subject': val_field_complainant_subject,
            'field_concideration_date': date_of_concideration
        }
        doc.render(context)
        doc.save("docs/final_" + doc_name)

        # doc saving check
        self.check_is_doc_created(doc_name)

    @staticmethod
    def doc_of_reject_complaint(doc_name, number_db_item):
        ##TODO 1. make the doc sample 2. make query
        pass

    @staticmethod
    def doc_of_result_complaint(doc_name, number_db_item):
        pass

    @staticmethod
    def get_complainant_id():
        cursor = sql_connect.sql_connect()
        cursor.execute('select distinct "№ пп" from ' + cfg.dB_table_name)
        data = cursor.fetchall() # data tuple type

        # convert data from tuple to iterable string
        data_str = []
        for row in data:
            data_str.append(re.sub('[''"{},()]', '', str(row)))

        # print('data_string :  ', {data_str})
        # print('get_complainant_id() type: ', {type(data_str)})
        return data_str

    def check_is_doc_created(self, doc_name):
        if os.path.exists("docs/final_" + doc_name):
            print("final_" + doc_name + " is successful created")
        else:
            print("final_" + doc_name + " is not found")