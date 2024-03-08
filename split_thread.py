import sys
import threading
import time
import pandas as pd
import concurrent.futures

from embedding_cutter import EmbeddingCutter


def batch():
    lock = threading.Lock()

    # Load the dataframe
    industry_file_path = 'data/industry_report.xlsx'
    df = pd.read_excel(industry_file_path)
    df = df.head(30)
    df = df[['source', 'content']]

    batch_size = 3
    with concurrent.futures.ThreadPoolExecutor() as executor:
        num_rows = len(df)
        num_batches = num_rows // batch_size + (num_rows % batch_size > 0)
        futures = []
        for i in range(num_batches):
            start_index = i * batch_size
            end_index = (i + 1) * batch_size
            batch_df = df[start_index: end_index]
            futures.append(executor.submit(process_df, batch_df, lock))

    # 等待所有任务完成
    concurrent.futures.wait(futures)


def process(row):
    pc = EmbeddingCutter(row['content'])
    chunks = pc.cut_paragraph()
    return chunks


def process_df(df, lock):
    # 获取线程锁
    chunks = df.apply(process, axis=1)

    # lock.acquire()

    try:

        result = "===========================\n"
        for i, chunk in enumerate(chunks):
            for j, c in enumerate(chunk):
                result += f"Chunk #{j} - Length: {len(c)}\n"
                result += f"{c.strip()}\n"
                result += "****************************\n\n"
        print(result)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        pass
    finally:
        pass
        # 释放线程锁
        # lock.release()


sys.stdout = open('output/industry_report_split_output_95_0_30_3.txt', 'wt')

if __name__ == "__main__":
    start = time.time()
    batch()
    print(time.time() - start)
