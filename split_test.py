import pandas
from embedding_cutter import EmbeddingCutter
import sys


domestic_file_path = 'data/domestic_report.xlsx'
industry_file_path = 'data/industry_report.xlsx'
news_file_path = 'data/news.xlsx'

df = pandas.read_excel(industry_file_path)
df = df.head(30)
df = df[['source', 'content']]

sys.stdout = open('output/industry_report_split_output_95_0_30.txt', 'wt')
#sys.stdout = open('output/domestic_report_split_output_95_0_30.txt', 'wt')
#sys.stdout = open('output/news_split_output_95_0_30.txt', 'wt')

for index, row in df.iterrows():
    pc = EmbeddingCutter(row['content'])
    chunks = pc.cut_paragraph()

    print(f"Source: {row['source']}")
    print("===========================")

    for i, chunk in enumerate(chunks):
        print(f"Chunk #{i} - Length: {len(chunk)}")
        print(chunk.strip())
    print("****************************\n\n")
