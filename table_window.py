import sys
from tkinter import Tk

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableView, QPushButton, QVBoxLayout, QMenu,
                             QTableWidgetItem, QWidget, QHBoxLayout)
from PyQt5.uic.properties import QtWidgets
from webtest import app

import config as cfg
from auto_doc_window import AutoDocWindow
from import_data_to_db import ImportDataToDb
from report_window import ReportWindow
from analytic_window import AnalyticWindow


class SqlTableWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowTitle('SQL Table')
        self.resize(1000, 400)

        # Set up model
        self.model = QSqlTableModel(self)
        self.model.setTable(cfg.dB_table_name)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # Headers
        self.model.setHeaderData(0, Qt.Horizontal, '№ пп')
        self.model.setHeaderData(1, Qt.Horizontal, 'Заказчик')
        self.model.setHeaderData(2, Qt.Horizontal, 'Наименовние закупки')
        self.model.setHeaderData(3, Qt.Horizontal, 'Номер в ЕИС')
        self.model.setHeaderData(4, Qt.Horizontal, 'НМЦК')
        self.model.setHeaderData(5, Qt.Horizontal, 'Оператор ЭТП')
        self.model.setHeaderData(6, Qt.Horizontal, 'Заявитель, краткое наименование, ИНН')
        self.model.setHeaderData(7, Qt.Horizontal, 'Дата обращения')
        self.model.setHeaderData(8, Qt.Horizontal, 'Суть обращения')
        self.model.setHeaderData(9, Qt.Horizontal, 'Статус _принято/отказ')
        self.model.setHeaderData(10, Qt.Horizontal, 'Основание отказа')
        self.model.setHeaderData(11, Qt.Horizontal, 'Дата отзыва обращения')
        self.model.setHeaderData(12, Qt.Horizontal, 'Результат _рассматривается, подведены итоги')
        self.model.setHeaderData(13, Qt.Horizontal, 'Дата рассмотрения')
        self.model.setHeaderData(14, Qt.Horizontal, 'Голосов ЗА')
        self.model.setHeaderData(15, Qt.Horizontal, 'Голосов ПРОТИВ')
        self.model.setHeaderData(16, Qt.Horizontal, 'Голосов ВОЗДЕРЖАЛСЯ')
        self.model.setHeaderData(17, Qt.Horizontal, 'Ссылка на итоги')
        self.model.select()
        # Set up view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.columnWidth(30)
        self.setCentralWidget(self.view)
        # button

    def add_row(self):
        rowCount = self.model.rowCount()
        self.model.insertRow(rowCount)

    def remove_row(self):
        if self.model.rowCount() > 0:
            self.model.removeRow(self.model.rowCount() - 1)

    @staticmethod
    def create_auto_doc_window():
        win = AutoDocWindow()
        win.show()
        sys.exit(app.exec_())

    @staticmethod
    def import_excel():
        data_frame = ImportDataToDb.import_data_from_excel(
            'raw_files/Arbitration_registry.xls',
            'sqlite:///data_base/arbitrationDb.db',
            'arbitrationDb'
        )
        return data_frame


class AppTable(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)
        self.setWindowTitle('SQL Table')

        mainLayout = QHBoxLayout()
        table = SqlTableWindow()
        mainLayout.addWidget(table)
        buttonLayout = QVBoxLayout()

        button_new = QPushButton('New')
        button_new.clicked.connect(table.add_row)
        buttonLayout.addWidget(button_new)

        button_remove = QPushButton('Remove')
        button_remove.clicked.connect(table.remove_row)
        buttonLayout.addWidget(button_remove, alignment=Qt.AlignTop)

        button_import_excel = QPushButton('Import Excel')
        button_import_excel.clicked.connect(lambda: table.import_excel())
        buttonLayout.addWidget(button_import_excel)

        button_auto_doc = QPushButton('(test) Create doc')
        button_auto_doc.clicked.connect(lambda: AutoDocWindow().run_widget())
        buttonLayout.addWidget(button_auto_doc)

        button_report = QPushButton('Create report')
        button_report.clicked.connect(lambda: ReportWindow().run_widget())
        buttonLayout.addWidget(button_report)

        button_graph = QPushButton('Graphics')
        button_graph.clicked.connect(lambda: AnalyticWindow().run_widget())
        buttonLayout.addWidget(button_graph)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)


def create_connection():
    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName(cfg.db_file_name)
    if not con.open():
        QMessageBox.critical(None, 'QTableView Example - Error!', 'Database Error: %s' % con.lastError().databaseText())
        return False
    return True


app = QApplication(sys.argv)
app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}')
if not create_connection():
    sys.exit(1)
win = AppTable()
win.show()
sys.exit(app.exec_())
