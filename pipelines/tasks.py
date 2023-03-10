class BaseTask:
    """Base Pipeline Task"""

    def run(self):
        raise RuntimeError('Do not run BaseTask!')

    def short_description(self):
        pass

    def __str__(self):
        task_type = self.__class__.__name__
        return f'{task_type}: {self.short_description()}'


class CopyToFile(BaseTask):
    """Copy table data to CSV file"""

    def __init__(self, table, output_file):
        self.table = table
        self.output_file = output_file

    def short_description(self):
        return f'{self.table} -> {self.output_file}'

    def run(self):
        print(f"Copy table `{self.table}` to file `{self.output_file}`")


import csv

class LoadFile(BaseTask):
    """Load file to table"""

    def __init__(self, table, input_file):
        self.table = table
        self.input_file = input_file

    def short_description(self):
        return f'{self.input_file} -> {self.table}'

    def run(self):
        data = []
        with open('original.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                # print(row)
                if (row[0] != 'id'):
                    temp = (row[0], row[1], row[2])
                    data.append(temp)
        
        con = sqlite3.connect("task.db")
        cur = con.cursor()
        cur.executemany("INSERT INTO original VALUES(?, ?, ?)", data)
        con.commit()
        print(f"Load file `{self.input_file}` to table `{self.table}`")

import sqlite3

class RunSQL(BaseTask):
    """Run custom SQL query"""

    def __init__(self, sql_query, title=None):
        self.title = title
        self.sql_query = sql_query

    def short_description(self):
        return f'{self.title}'

    def run(self):
        con = sqlite3.connect("task.db")
        cur = con.cursor()
        cur.execute(self.sql_query)
        con.commit()
        
        # for row in cur.execute("SELECT * FROM original"):
        #     print(row)
            
        # for row in cur.execute("SELECT * FROM norm"):
        #     print(row)
            
        print(f"Run SQL ({self.title}):\n{self.sql_query}")
        



class CTAS(BaseTask):
    """SQL Create Table As Task"""

    def __init__(self, table, sql_query, title=None):
        self.table = table
        self.sql_query = sql_query
        self.title = title or table

    def short_description(self):
        return f'{self.title}'

    def run(self):
        con = sqlite3.connect("task.db")
        cur = con.cursor()
        cur.execute(self.sql_query)
        con.commit()
        cur.execute("create table" + self.table)
        
        print(f"Create table `{self.table}` as SELECT:\n{self.sql_query}")
