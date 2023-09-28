# Data-Separator

O repositório "Data-Separator" contém um script Python projetado para dividir um arquivo Excel em lotes e salvar cada lote como um arquivo CSV separado. Posteriormente, todos os arquivos CSV gerados são compactados em um arquivo ZIP.

## 🚀 Funcionalidades

- Leitura de arquivo Excel.
- Divisão do DataFrame em lotes.
- Salvar cada lote como um arquivo CSV separado.
- Compactação de todos os arquivos CSV em um arquivo ZIP.

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- zipfile

## ⚙️ Como Utilizar

1. **Configurar Parâmetros**

   Abra o script e configure os seguintes parâmetros no final do arquivo:

   ```python
   input_file_path = "seu_arquivo.xlsx"  # Substitua pelo caminho do seu arquivo Excel
   base_file_name = "NOME_BASE"  # Nome base para os arquivos de lote
   output_directory = "./"  # Diretório onde os arquivos serão salvos
   batch_size = 4999  # Número de linhas por lote (sem contar o cabeçalho)
   ```

2. **Executar o Script**

   Execute o script Python no seu ambiente de desenvolvimento ou terminal.

   ```sh
   python nome_do_script.py
   ```

3. **Verificar Resultados**

   Após a execução, verifique o diretório de saída especificado para os arquivos CSV e ZIP gerados.
