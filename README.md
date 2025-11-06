# Country Clustering Project (Kaggle: Unsupervised Learning on Country Data)

Este repositório contém **todas as quatro partes** do trabalho:

- **Parte 1 — Infraestrutura**
- **Parte 2 — Escolha de base & EDA**
- **Parte 3 — Clusterização (K-Means e Hierárquica)**
- **Parte 4 — Algoritmos (passos do K-means e versão medóide)**

## 🔧 Como executar (Ambiente local)

Você pode usar **virtualenv** ou **Conda**. Abaixo, exemplos:

### Opção A) Virtualenv (Python 3.9+)
```bash
python3 -m venv .venv
source .venv/bin/activate    # Linux/Mac
# .venv\Scripts\activate   # Windows PowerShell
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name country-clustering
```

### Opção B) Conda
```bash
conda create -n country-clustering python=3.9 -y
conda activate country-clustering
pip install -r requirements.txt
python -m ipykernel install --user --name country-clustering
```

> **Printscreen solicitado (Parte 1):**
> Abra um terminal com o ambiente ativado e rode:
> ```bash
> python -c "import sys,platform;print(platform.platform());print(sys.version)"
> python -c "import numpy,pandas,sklearn,scipy,matplotlib,seaborn;print('OK libs')"
> jupyter --version
> ```
> Tire um print do terminal e cole no relatório.

## 📥 Dados (Kaggle)
Baixe o dataset em:  
https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data

Coloque o arquivo **`Country-data.csv`** em `./data/Country-data.csv` antes de abrir o notebook.

## 📓 Notebook principal
Abra o notebook:
```
notebooks/01_country_clustering.ipynb
```
e selecione o kernel `country-clustering` (ou o kernel que você criou).

O notebook executa:
- Verificação do ambiente (Parte 1).
- EDA & pré-processamento (Parte 2).
- K-Means (k=3), interpretação, país representativo (mais próximo ao centróide).
- Clusterização Hierárquica + dendrograma e comparação (Parte 3).
- Passos do K-Means e implementação **K-Medóides** (PAM simplificado) (Parte 4).

## 🧪 Scripts auxiliares
- `src/kmedoids.py` — Implementação simples de K-Medóides (método PAM).

## 📦 Entrega
- **requirements.txt** incluso.
- Notebook + scripts.
- Inclua o **printscreen** do ambiente ativado no seu relatório.
- Publique estes arquivos em um repositório público **ou** compacte a pasta e submeta no Moodle.

---
Autor: (preencher com seu nome)
