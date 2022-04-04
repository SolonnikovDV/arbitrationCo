from tkinter import *
from tkinter.ttk import Combobox
import config as cfg
from auto_doc_engine import AutoDoc
import re
import logging
from PyQt5.QtWidgets import QMainWindow, QFrame, QWidget, QDialog, QGridLayout, QComboBox, QHBoxLayout, QPushButton, \
    QVBoxLayout


class AutoDocWindow(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Auto Doc menu')
        self.resize(400, 400)
        print('Autodoc win called')
        # add main layout
        layout = QVBoxLayout(self)

        #  <editor-fold desc="Buttons section">
        self.button = QPushButton('(test) Create Accept doc sample')
        self.button.clicked.connect(
            lambda : AutoDoc.doc_of_accept_complaint(
                AutoDoc(),
                cfg.doc_accept_complainant + '.docx',
                self.cb_complainant_id_from_db.currentText()
            )
        )
        layout.addWidget(self)
        layout.addWidget(self.button)

        self.cb_notif_names = QComboBox()
        self.cb_notif_names.addItems(self.notification_names())
        layout.addWidget(self.cb_notif_names)

        self.cb_complainant_id_from_db = QComboBox()
        print(type(AutoDoc.get_complainant_id()))
        self.cb_complainant_id_from_db.addItems(AutoDoc.get_complainant_id())
        layout.addWidget(self.cb_complainant_id_from_db)
    #
    # def draw_widgets(self):
    #     button_width = 60
    #
    #     self.cb_notif_names.grid(row=0, column=1, sticky=W)
    #     self.cb_complainant_id_from_db.grid(row=1, column=1, sticky=W)
    #
    #     Label(self.root, text='Выберите тип уведомления').grid(row=0, column=0, sticky=W)
    #
    #     Button(self.root,
    #            text='(Test) Создать уведомление',
    #            width=button_width,
    #            command=lambda : self.notification_selection(),
    #            relief=GROOVE,
    #            bd=3)\
    #         .grid(row=4, column=1, sticky=W)

    def notification_selection(self):
        notif_name = self.cb_notif_names.get()
        notif_id = self.notification_id()
        # accept
        if notif_name == cfg.doc_accept_complainant:
            AutoDoc.doc_of_accept_complaint(notif_name + '.docx', notif_id)
            logging.debug(
                'notification_selection(self): notif_name = ' + notif_name + '; notif_ID = ' + self.notification_id()
            )
        ## TODO 'if esle' for Rejected and Result notification
        # reject
        if notif_name == cfg.doc_reject_complainant:
            AutoDoc.doc_of_reject_complaint(notif_name + '.docx', notif_id)
            logging.debug(
                'notification_selection(self): notif_name = ' + notif_name + '; notif_ID = ' + self.notification_id()
            )
        # result
        if notif_name == cfg.doc_result_of_complaint:
            AutoDoc.doc_of_result_complaint(notif_name + '.docx', notif_id)
            logging.debug(
                'notification_selection(self): notif_name = ' + notif_name + '; notif_ID = ' + self.notification_id()
            )

    @staticmethod
    def notification_names():
        notif_names = [cfg.doc_accept_complainant, cfg.doc_reject_complainant, cfg.doc_result_of_complaint]
        length = len(notif_names)
        for i in range(length):
            notif_names[i] = re.sub('[''"{}]', '', notif_names[i])
            print(notif_names[i])
        return notif_names

    def notification_id(self):
        notif_id = self.cb_complainant_id_from_db.get()
        notif_id = re.sub('[''"{}]', '', notif_id)
        return str(notif_id)

    def run_widget(self):
        self.show()
