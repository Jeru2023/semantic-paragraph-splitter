import pandas
from paragraph_cutter import ParagraphCutter
import sys


domestic_file_path = 'data/domestic_report.xlsx'
industry_file_path = 'data/industry_report.xlsx'

df = pandas.read_excel(domestic_file_path)
df = df.head(30)
df = df[['source', 'content']]


sys.stdout = open('output/industry_report_split_output.txt', 'wt')

for index, row in df.iterrows():
    pc = ParagraphCutter(row['content'])
    chunks = pc.cut_paragraph()

    print(f"Source: {row['source']}")
    print("===========================")

    for i, chunk in enumerate(chunks):
        print(f"Chunk #{i} - Length: {len(chunk)}")
        print(chunk.strip())
    print("****************************\n\n")
