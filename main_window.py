import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from import_data_to_db import ImportDataToDb
import config as cfg
from auto_doc_window import AutoDocWindow


def button_clear_text_field(entry_text):
    choice = messagebox.askyesno('Очистка поля', 'Вы дествительно хотите очистить содержимое поля')
    if choice:
        print(entry_text.get())
        entry_text.delete(0, END)


def button_import_excel(data_frame):
    choice = messagebox.askyesno('Импорт Excel', 'Вы дествительно хотите импортировать Excel')
    if choice:
        data_frame


class MainWindow:
    def __init__(self, width, height, x, y, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        #  <editor-fold desc="Edit text variables">
        self.field_owner = Entry(self.root,
                                 font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_contract_subject = Entry(self.root,
                                            font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_registry_number = Entry(self.root,
                                           font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_contract_price = Entry(self.root,
                                          font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_portal = Entry(self.root,
                                  font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_complainant_name = Entry(self.root,
                                            font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_complaint_date = Entry(self.root,
                                          font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_complainant_subject = Entry(self.root,
                                               font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_status = Entry(self.root,
                                  font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_grounds_refusal = Entry(self.root,
                                           font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_date_withdraw = Entry(self.root,
                                         font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_result = Entry(self.root,
                                  font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_concideration_date = Entry(self.root,
                                             font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue',
                                             bd=1)
        self.field_vote_accept = Entry(self.root,
                                       font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_vote_reject = Entry(self.root,
                                       font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_vote_hold = Entry(self.root,
                                     font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        self.field_path = Entry(self.root,
                                font='Consoles 12', justify=LEFT, relief=SUNKEN, fg='blue', bd=1)
        # </editor-folds>

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):

        button_width = 15
        message_text_width = 250

        # <editor-fold desc="message_text + edit text group">
        Message(self.root,
                text='Заказчик',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=1, column=0, sticky=W)
        self.field_owner.grid(row=1, column=1, sticky=W + E)

        Message(self.root,
                text='Наименовние закупки',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=2, column=0, sticky=W)
        self.field_contract_subject.grid(row=2, column=1, sticky=W + E)

        Message(self.root,
                text='Номер в ЕИС',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=3, column=0, sticky=W)
        self.field_registry_number.grid(row=3, column=1, sticky=W + E)

        Message(self.root,
                text='НМЦК',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=4, column=0, sticky=W)
        self.field_contract_price.grid(row=4, column=1, sticky=W + E)

        Message(self.root,
                text='Оператор ЭТП',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=5, column=0, sticky=W)
        self.field_portal.grid(row=5, column=1, sticky=W + E)

        Message(self.root,
                text='Заявитель, краткое наименование, ИНН',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=6, column=0, sticky=W)
        self.field_complainant_name.grid(row=6, column=1, sticky=W + E)

        Message(self.root,
                text='Дата обращения',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=7, column=0, sticky=W)
        self.field_complaint_date.grid(row=7, column=1, sticky=W + E)

        Message(self.root,
                text='Суть обращения',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=8, column=0, sticky=W)
        self.field_complainant_subject.grid(row=8, column=1, sticky=W + E)

        Message(self.root,
                text='Статус _принято/отказ',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=9, column=0, sticky=W)
        self.field_status.grid(row=9, column=1, sticky=W + E)

        Message(self.root,
                text='Основание отказа',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=10, column=0, sticky=W)
        self.field_grounds_refusal.grid(row=10, column=1, sticky=W + E)

        Message(self.root,
                text='Дата отзыва обращения',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=11, column=0, sticky=W)
        self.field_date_withdraw.grid(row=11, column=1, sticky=W + E)

        Message(self.root,
                text='Результат _рассматривается, подведены итоги',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=12, column=0, sticky=W)
        self.field_result.grid(row=12, column=1, sticky=W + E)

        Message(self.root,
                text='Дата рассмотрения',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=13, column=0, sticky=W)
        self.field_concideration_date.grid(row=13, column=1, sticky=W + E)

        Message(self.root,
                text='Голосов ЗА',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=14, column=0, sticky=W)
        self.field_vote_accept.grid(row=14, column=1, sticky=W + E)

        Message(self.root,
                text='Голосов ПРОТИВ',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=15, column=0, sticky=W)
        self.field_vote_reject.grid(row=15, column=1, sticky=W + E)

        Message(self.root,
                text='Голосов ВОЗДЕРЖАЛСЯ',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=16, column=0, sticky=W)
        self.field_vote_hold.grid(row=16, column=1, sticky=W + E)

        Message(self.root,
                text='Ссылка на итоги',
                width=message_text_width,
                font=('Consoles', 12)).grid(row=17, column=0, sticky=W)
        self.field_path.grid(row=17, column=1, sticky=W + E)

        # </editor-fold>

        # <editor-fold desc="buttons group">
        Button(self.root,
               text='Загрузить в базу',
               width=button_width,
               command=self.button_upload_to_sql,
               relief=GROOVE,
               bd=3).grid(row=0, column=3, sticky=W)

        Button(self.root,
               text='Импорт Excel',
               width=button_width,
               command=lambda: button_import_excel(self.import_excel()),
               relief=GROOVE,
               bd=3).grid(row=1, column=3, sticky=E)

        Button(self.root,
               text='Очистить все',
               width=button_width,
               command=lambda: self.button_clear_all(),
               relief=GROOVE,
               bd=3).grid(row=3, column=3, sticky=E)

        Button(self.root,
               text='Выход',
               width=button_width,
               command=self.exit_check,
               relief=GROOVE,
               bd=3).grid(row=4, column=3, sticky=E)

        Button(self.root,
               text='Обращение принято-Doc',
               width=button_width,
               command=self.create_auto_doc_window,
               relief=GROOVE,
               bd=3).grid(row=2, column=3, sticky=E)

        # </editor-fold>

        # Button(self.root,
        #        text='Отчеты',
        #        width=button_width,
        #        command=self.create_report_window,
        #        relief=GROOVE,
        #        bd=3) \
        #     .grid(row=0, column=3, sticky=E)
        #
        # Button(self.root,
        #        text='Графики',
        #        width=button_width,
        #        command=self.create_analytic_window,
        #        relief=GROOVE,
        #        bd=3) \
        #     .grid(row=1, column=3, sticky=E)
        #
        # Button(self.root,
        #        text='Тест записи',
        #        width=button_width,
        #        command=lambda: self.test_import_in_db(),
        #        relief=GROOVE,
        #        bd=3) \
        #     .grid(row=2, column=3, sticky=E)
        # </editor-fold>

    def button_upload_to_sql(self):
        length = len(self.arrayEntries) - 1
        choice = messagebox.askyesno('Загрузка в базу данных',
                                     'Действительно подтверждаете загрузку в базу данных?')
        # insert data rows to db
        # for i in range(length):
        ImportDataToDb.insert_variable_into_table(
            self.field_owner.get(),
            self.field_contract_subject.get(),
            self.field_registry_number.get(),
            self.field_contract_price.get(),
            self.field_portal.get(),
            self.field_complainant_name.get(),
            self.field_complaint_date.get(),
            self.field_complainant_subject.get(),
            self.field_status.get(),
            self.field_grounds_refusal.get(),
            self.field_date_withdraw.get(),
            self.field_result.get(),
            self.field_concideration_date.get(),
            self.field_vote_accept.get(),
            self.field_vote_reject.get(),
            self.field_vote_hold.get(),
            self.field_path.get()
        )

        if choice:
            messagebox.showinfo('Выгрузка в базу данных', 'Данные загружены в базу')
            print(self.arrayEntries[0:length])
            # TODO
            #  clear oll data after upload to DB
            self.arrayEntries.clear()

    def button_clear_all(self):
        choice = messagebox.askyesno('Очистка всех полей', 'Вы дествительно хотите очистить содержимое всех полей')
        for i in range(len(self.arrayEntries) - 1):
            if choice:
                self.arrayEntries[i].delete(0, END)
            # self.field_acceptance_invoke_date.delete(0, END)
            # self.field_contract_owner.delete(0, END)
            # self.field_contract_details.delete(0, END)
            # self.field_contract_value.delete(0, END)
            # self.field_acceptance_value.delete(0, END)
            # self.field_acceptance_period.delete(0, END)
            # self.field_counterparty_name.delete(0, END)
            # self.field_contract_subject.delete(0, END)
            # self.field_acceptance_date.delete(0, END)
            # self.field_acceptance_status.delete(0, END)
            # self.field_diff_invoke_acceptance.delete(0, END)
            # self.field_violation_of_terms.delete(0, END)
            # self.field_acceptance_participants.delete(0, END)
            # self.field_ICD_opinion.delete(0, END)
            # self.field_acceptance_summary_value.delete(0, END)
            # self.field_reminder_contract_value.delete(0, END)

    @staticmethod
    def import_excel():
        data_frame = ImportDataToDb.import_data_from_excel('raw_files/Arbitration_registry.xls',
                                                                'sqlite:///data_base/arbitrationDb.db',
                                                                'arbitrationDb')
        return data_frame

    def exit_check(self):
        choice = messagebox.askyesno('Выход', 'Хотите выйти?')
        if choice:
            self.root.destroy()

    def create_auto_doc_window(self):
        cfg.auto_doc_window = AutoDocWindow(self.root, 600, 480, 805, 200, 'Reports Window')
        return cfg.auto_doc_window

    def create_sql_table(self):
        pass
