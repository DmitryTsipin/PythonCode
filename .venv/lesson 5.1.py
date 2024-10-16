import pandas as pd
import pyodbc

# Параметры подключения к локальной базе данных MS SQL Server
server = 'LAPTOP-9DJOCEOC\SQLEXPRESS'  # Имя сервера
database = 'AdventureWorks2017'         # Имя базы данных

# Строка подключения с использованием Windows Authentication
# connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
#
# # Подключение к базе данных
# connection = pyodbc.connect(connection_string)
# query = 'SELECT * FROM [Person].[BusinessEntity]'
#
# # Загрузка данных в DataFrame
# df = pd.read_sql(query, connection)
#
# # Закрытие подключения
# connection.close()
#
# # Вывод первых строк датафрейма
# print(df.info())


#
#
#
#
#
# import pyodbc
#
# # Параметры подключения к базе данных MS SQL Server с Windows Authentication
# server = 'LAPTOP-9DJOCEOC\SQLEXPRESS'  # Имя сервера
# database = 'AdventureWorks2017'         # Имя базы данных
# connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
#
# # Подключаемся к базе данных
# connection = pyodbc.connect(connection_string)
# cursor = connection.cursor()
#
# # Пример данных для добавления в таблицу
# name = 'John Doe'
# position = 'Software Engineer'
# salary = 75000
#
# # SQL-запрос для вставки данных
# insert_query = """
#     INSERT INTO Test (employee, position, salary)
#     VALUES (?, ?, ?)
# """
#
# # Выполнение запроса с передачей параметров
# cursor.execute(insert_query, (name, position, salary))
#
# # Подтверждаем изменения в базе данных
# connection.commit()
#
# # Закрываем соединение
# cursor.close()
# connection.close()
#
# print("Данные успешно добавлены в таблицу.")
# Change 2342335646купеукцпеывап
import pandas as pd
from sqlalchemy import create_engine
import urllib

# Шаг 1: Создание соединения с локальной MS SQL базой данных с использованием аутентификации Windows
server = 'LAPTOP-9DJOCEOC\SQLEXPRESS'  # Имя сервера
database = 'AdventureWorks2017'         # Имя базы данных

# Создаем строку подключения для Windows аутентификации
# params = urllib.parse.quote_plus(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')
params = urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')

engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

# Шаг 2: Пример создания DataFrame
# Допустим, у нас есть DataFrame с данными сотрудников
data = {
    'firstname': ['John', 'Jane', 'Mary'],
    'lastname': ['Doe', 'Smith', 'Johnson'],
    'mail': ['john.doe@example.com', 'jane.smith@example.com', 'mary.j@example.com']
    # 'age': [30, 25, 35]
}

df = pd.DataFrame(data)

# Шаг 3: Вставка данных в таблицу Test
df.to_sql('Test1', con=engine, if_exists='append', index=False)

print("Данные успешно вставлены в таблицу Test1.")
