import spark as spark
from pyspark.sql.types import ArrayType,StringType
import json

def get_array_set(col_list):
    new_list = []
    if col_list:
        try:
            for x in col_list:
                if x not in new_list:
                    new_list.append(x)
        except:
            print("数据json异常:" )
            return []
    return new_list


get_array_set = spark.udf.register('get_array_set', get_array_set, ArrayType(StringType()))




