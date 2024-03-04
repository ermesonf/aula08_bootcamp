import pandas as pd
import os
import glob

# Extract
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total
# Transform

# Load

if __name__ == "__main__":
    pasta = 'data'
    print(extrair_dados(pasta=pasta))