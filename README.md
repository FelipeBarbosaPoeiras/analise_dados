# Análise da Tabela 3 — Áreas gerais de formação na graduação

Análise da **Tabela 10063 (IBGE)** — pessoas com nível superior completo, por sexo e Grande
Região do Brasil, dividida em 3 recortes:

1. **Curso superior (geral)** — `superior.xlsx`
2. **Ciência, Tecnologia, Engenharias e Matemática (CTEM)** — `tecnologia.xlsx`
3. **Educação, Serviços pessoais, Saúde e Bem-estar** — `educacao_saude.xlsx`

## Conteúdo do repositório

| Arquivo | Descrição |
|---|---|
| `Analise_Tabela3.ipynb` | Notebook Jupyter com todo o código, os 3 recortes e as estatísticas (`describe()`) |
| `Tabela_3_Areas_gerais_de_formacao_na_graduacao__1_.xlsx` | Tabela original do IBGE |
| `superior.xlsx` | Homens/Mulheres/Total por região — curso superior (geral) |
| `tecnologia.xlsx` | Homens/Mulheres/Total por região — área de CTEM |
| `educacao_saude.xlsx` | Homens/Mulheres/Total por região — área de Educação/Saúde |

## Como executar

```bash
pip install pandas openpyxl jupyter
jupyter notebook Analise_Tabela3.ipynb
```

Fonte dos dados: IBGE - Censo Demográfico.
