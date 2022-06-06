import os
import pandas as pd
import fnmatch
from time import sleep
import datetime

os.chdir('Diretório da pasta de downloads')
pd.options.display.max_colwidth = 80
arquivo = ''
for c in os.listdir():
    if fnmatch.fnmatch(c, 'AttendeeReport*.csv'):
        arquivo = c
csv = pd.read_csv(arquivo)
df = pd.DataFrame(csv[['Full Name',  'Participant Id']])
df_drop = df.drop_duplicates()
df_drop.insert(2, 'Total', '', True)
df_drop.at[0, 'Total'] = len(df_drop)
print(f'{df_drop}\n')
opc = str(input('Criar uma planilha com os dados filtrados?[s/n] \n')).upper()[0]
if opc == 'S':
    print(f'Criando planilha e deletando o arquivo {arquivo}...')
    df_drop.to_excel(f'Audiencia-{datetime.datetime.now().date()}.xlsx', index=False)
else:
    print(f'Deletando o arquivo {arquivo}...')
os.remove(arquivo)
sleep(3)
