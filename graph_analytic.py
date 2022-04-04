import csv
import matplotlib
from matplotlib import pyplot as plt
import sqlite3
import pandas as pd
import seaborn as sns
import config as cfg


class GraphAnalytic:

    @staticmethod
    def db_to_csv_one_owner(owner, year):
        conn = sqlite3.connect(cfg.db_file_name)
        cur = conn.cursor()
        print(f'csv input : {owner} , {year}')
        cur.execute(
            'SELECT "Заказчик", "Дата обращения", "НМЦК", "Статус _принято/отказ" '
            'FROM ' + cfg.dB_table_name + ' '
            'WHERE '
            '"Заказчик"="' + owner + '" '
            'AND '
            'strftime("%Y", "Дата обращения")="' + year + '"')

        with open('csv_files/One_owner_csv_file.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur)

    @staticmethod
    def db_to_csv_result(year, result):
        conn = sqlite3.connect(cfg.db_file_name)
        cur = conn.cursor()
        print(f'csv input : {year} , {result}')
        cur.execute(
                'SELECT "Заказчик", "Дата обращения", "НМЦК", "Статус _принято/отказ" '
                'FROM ' + cfg.dB_table_name + ' '
                'WHERE '
                '"Статус _принято/отказ"="' + result + '" '
                'AND '
                'strftime("%Y", "Дата обращения")="' + year + '"')

        with open('csv_files/Result_csv_file.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur)

    @classmethod
    def db_to_csv(cls):
        conn = sqlite3.connect(cfg.db_file_name)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {cfg.dB_table_name}')

        with open('csv_files/Full_csv_file.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur)

    @classmethod
    def graph_one_owner(cls, owner, year):
        # get csv file
        cls.db_to_csv_one_owner(owner, year)
        # data set from csv file with drop nulls
        df = pd.read_csv('csv_files/One_owner_csv_file.csv', sep=',', quotechar='"', parse_dates=['Дата обращения'])
        # date format from DD-MM-YYYY HH:MM:SS.SSSSSS to YYYY-MM
        cls.date_format(df, 'Дата обращения', 'Месяц, год приемки')

        # set seaborn style
        sns.set_style('whitegrid')
        # graphic of result of acceptance with total sum on a time line
        g_rel = sns.relplot(x='Дата обращения', y='НМЦК', size='НМЦК', sizes=(15, 200), hue='Статус _принято/отказ', data=df)
        # set xlabels orientation
        cls.xticks_label_rotation(g_rel, 45)
        # set left adjust
        plt.subplots_adjust(left=0.10)
        # set title
        g_rel.fig.suptitle(owner)

        # init line plot
        sns.lineplot(x='Дата обращения', y='НМЦК', hue='Статус _принято/отказ', data=df, ci='sd', legend=False)
        # set Y axis limits
        plt.ylim(min(df['НМЦК']), max(df['НМЦК']))
        # set X axis limits
        plt.xlim(df['Дата обращения'].iloc[0], df['Дата обращения'].iloc[-1])
        # set axis format
        plt.gca().get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        # set Y axis ticks frequency
        plt.gca().get_yaxis().set_major_locator(matplotlib.ticker.MultipleLocator(20000000))

        plt.show()

    @classmethod
    def graph_result(cls, year, result):
        # get csv file
        cls.db_to_csv_result(year, result)
        # data set from csv file with drop nulls
        df = pd.read_csv('csv_files/Result_csv_file.csv', sep=',', quotechar='"', parse_dates=['Дата обращения'])
        # date format from DD-MM-YYYY HH:MM:SS.SSSSSS to YYYY-MM
        # cls.date_format(df, 'Дата обращения', 'Месяц, год приемки')

        # set seaborn style
        sns.set_style('whitegrid')
        # graphic of result of acceptance with total sum on a time line
        g_rel = sns.relplot(x='Дата обращения', y='НМЦК', size='НМЦК', sizes=(15, 200), data=df)
        # set xlabels orientation
        cls.xticks_label_rotation(g_rel, 45)
        # set left adjust
        plt.subplots_adjust(left=0.10)
        # set title
        g_rel.fig.suptitle(result)

        # init line plot
        sns.lineplot(x='Дата обращения', y='НМЦК', data=df, ci='sd', legend=False)
        # set Y axis limits
        plt.ylim(min(df['НМЦК']), max(df['НМЦК']))
        # set X axis limits
        plt.xlim(df['Дата обращения'].iloc[0], df['Дата обращения'].iloc[-1])
        # set axis format
        plt.gca().get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        # set Y axis ticks frequency
        plt.gca().get_yaxis().set_major_locator(matplotlib.ticker.MultipleLocator(20000000))

        plt.show()

    @classmethod
    def graph_all_owners(cls):
        # get csv file
        cls.db_to_csv()
        # data set from csv file with drop nulls
        df = pd.read_csv('csv_files/Full_csv_file.csv',
                         sep=',',
                         quotechar='"',
                         parse_dates=['Дата обращения'])
        # date format from DD-MM-YYYY HH:MM:SS.SSSSSS to YYYY-MM
        cls.date_format(df, 'Дата обращения', 'Месяц, год приемки')

        # seaborn style
        sns.set_style('whitegrid')
        # graphic of result of acceptance with total sum on a time line
        g_rel = sns.relplot(x='Дата обращения',
                            y='НМЦК',
                            size='НМЦК',
                            sizes=(15, 200),
                            hue='Заказчик',
                            col='Статус _принято/отказ',
                            legend='brief',
                            data=df)

        # set xlabels orientation
        cls.xticks_label_rotation(g_rel, 45)
        # set left adjust
        plt.subplots_adjust(left=0.09)

        # set Y axis limits
        plt.ylim(min(df['НМЦК']),
                 max(df['НМЦК']))
        # set X axis limits
        print(f'{df["Дата обращения"]}')
        
        plt.xlim(df['Дата обращения'].iloc[0],
                 df['Дата обращения'].iloc[-1])
        # set axis format
        plt.gca().get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        # set Y axis ticks frequency
        plt.gca().get_yaxis().set_major_locator(matplotlib.ticker.MultipleLocator(20000000))

        plt.show()

    @classmethod
    def date_format(cls, data_frame, column_name, new_column_name):
        data_frame[new_column_name] = data_frame[column_name].dt.strftime('%Y-%m')

    @classmethod
    def xticks_label_rotation(cls, plot_name, value):
        for axis in plot_name.axes.flat:
            for label in axis.get_xticklabels():
                label.set_rotation(value)
