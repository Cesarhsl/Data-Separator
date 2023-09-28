
import os
import pandas as pd
import zipfile

def divide_excel_in_batches(input_file_path, base_file_name, output_directory, batch_size=4999):
    # Ler o arquivo Excel
    try:
        df = pd.read_excel(input_file_path)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    # Verificar se o diretório de saída existe, senão criar
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Dividir o DataFrame em lotes e salvar cada lote como um novo arquivo CSV
    file_paths = []  # Para armazenar os caminhos dos arquivos gerados
    for i, start_row in enumerate(range(0, len(df), batch_size)):
        end_row = start_row + batch_size
        batch_df = df.iloc[start_row:end_row]
        
        # Nome do arquivo de lote
        batch_file_name = f"{base_file_name}_{i+1}.csv"
        batch_file_path = os.path.join(output_directory, batch_file_name)
        
        # Salvar o lote em um arquivo CSV
        batch_df.to_csv(batch_file_path, index=False)
        file_paths.append(batch_file_path)

    # Criar um arquivo ZIP para armazenar todos os arquivos de lote
    zip_file_name = f"{base_file_name}_LOTES.zip"
    zip_file_path = os.path.join(output_directory, zip_file_name)
    
    # Zipar todos os arquivos de lote
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file_path in file_paths:
            zipf.write(file_path, os.path.basename(file_path))
    
    print(f"Arquivos divididos e salvos em {zip_file_path}")

if __name__ == "__main__":
    # Parâmetros
    input_file_path = "seu_arquivo.xlsx"  # Substitua pelo caminho do seu arquivo Excel
    base_file_name = "NOME_BASE"  # Nome base para os arquivos de lote
    output_directory = "./"  # Diretório onde os arquivos serão salvos
    batch_size = 4999  # Número de linhas por lote (sem contar o cabeçalho)


    # Executar a função
    divide_excel_in_batches(input_file_path, base_file_name, output_directory, batch_size)