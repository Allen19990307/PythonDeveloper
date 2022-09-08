from pathlib import Path
import pandas as pd
if __name__ == '__main__':
   # 每月的数据统计表的计算
   # file_directory
   this_dir = Path(__file__).resolve().parent
   # read excel files from sales_data
   parts = []
   for path in (this_dir / "sales_data").rglob("*.xls"):
      # print(f'Reading {parts.name}')
      part = pd.read_excel(path,index_col="transaction_id")
      parts.append(part)
   #merge multiple DataFrames into a single one
   df = pd.concat(parts)
   #transaction_data: 将数据进行汇总的操作
   pivot = pd.pivot_table(df, index="transaction_date", columns="store", values="amount", aggfunc="sum")
   # 按月重采，赋予一个索引的名称
   sum = pivot.resample("M").sum()
   sum.index.name ="Month"
   # 总结报告表写入Excel
   sum.to_excel(this_dir/"sales_report_pandas.xlsx")
