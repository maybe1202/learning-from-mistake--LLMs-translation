from sacrebleu import corpus_chrf
import json

# 讀取JSON檔案
file_path = ""
with open(file_path, 'r', encoding='utf-8') as file:

    data = json.load(file)
    # data = json.load(file)

# 如果data不是列表，請將其轉換為列表
if not isinstance(data, list):
    data = [data]

# 從數據中提取參考句子和翻譯句子
references = [pair.get('參考句子', '') for pair in data]
translations = [pair.get('翻譯句子', '') for pair in data]

# 使用sacrebleu.corpus_chrf計算chrF分數
chrf = corpus_chrf(translations, [references])
print(f"{chrf.score}")