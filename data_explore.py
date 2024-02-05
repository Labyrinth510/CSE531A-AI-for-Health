import pandas as pd

def top_n_diseases(data_path, n):
    # 读取 DIAGNOSES_ICD.csv 文件
    diagnoses_icd_df = pd.read_csv(f"{data_path}/DIAGNOSES_ICD.csv")

    # 读取 D_ICD_DIAGNOSES.csv 文件
    d_icd_diagnoses_df = pd.read_csv(f"{data_path}/D_ICD_DIAGNOSES.csv")

    # 合并两个数据框，以获取疾病的完整描述
    merged_df = pd.merge(diagnoses_icd_df, d_icd_diagnoses_df, left_on='icd9_code', right_on='icd9_code')

    # 统计最常见的 n 个疾病编码
    top_n_diseases = merged_df['icd9_code'].value_counts().head(n)

    # 获取疾病编码对应的疾病名称和全名
    top_n_diseases_with_names = {}
    for icd9_code, count in top_n_diseases.items():
        row = merged_df[merged_df['icd9_code'] == icd9_code].iloc[0]
        short_title = row['short_title']
        long_title = row['long_title']
        top_n_diseases_with_names[icd9_code] = {'short_title': short_title, 'long_title': long_title, 'count': count}

    return top_n_diseases_with_names


data_path = "Data/mimic-iii-clinical-database-demo-1.4"
# 获取结果
top_diseases = top_n_diseases(data_path, 10)
# 打印结果
print("Top 10 Most Common Diseases:")
for icd9_code, info in top_diseases.items():
    print(f"ICD9 Code: {icd9_code}")
    print(f"Count: {info['count']}")
    print(f"Short Title: {info['short_title']}")
    print(f"Long Title: {info['long_title']}")
    print()
