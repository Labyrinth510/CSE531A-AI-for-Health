import pandas as pd
import os
import glob


def extract_fields_from_csv(folder_path):
    # 使用 glob 模块获取文件夹中所有的 CSV 文件
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    # 创建一个字典用于存储文件名和对应的字段列表
    file_fields_dict = {}

    # 遍历 CSV 文件列表
    for csv_file in csv_files:
        # 读取 CSV 文件
        df = pd.read_csv(csv_file)

        # 提取字段名
        fields = df.columns.tolist()

        # 获取文件名
        file_name = os.path.basename(csv_file)

        # 存储字段名到字典中
        file_fields_dict[file_name] = fields

    return file_fields_dict


if __name__ == "__main__":
    folder_path = "Data\mimic-iii-clinical-database-demo-1.4"
    file_fields_dict = extract_fields_from_csv(folder_path)

    # 写入到 summary.txt 文件中
    with open('summary.txt', 'w') as summary_file:
        # 遍历 file_fields_dict 字典，将文件名和对应字段写入到 summary.txt 文件中
        for file_name, fields in file_fields_dict.items():
            summary_file.write(f"'{file_name}': {', '.join(fields)}\n")

    print("Summary.txt 文件已生成.")
