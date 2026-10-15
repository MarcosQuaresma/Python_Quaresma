# Fundamentos de Python

Repositório de estudos de Python com exemplos práticos e exercícios. Os scripts usam situações como cadastro, busca e avaliação de filmes para demonstrar os conceitos fundamentais da linguagem.

## Organização

- [`aulas/`](./aulas): exemplos didáticos organizados em sequência.
- [`exercicios/`](./exercicios): exercícios de aplicação dos conceitos.

## Tópicos estudados

| Script | Resumo técnico |
| --- | --- |
| `aulas/01_primeiro.py` | Execução sequencial de instruções e exibição de texto com `print()`. |
| `aulas/02_dados.py` | Variáveis, tipos primitivos (`str`, `int`, `float` e `bool`) e inspeção de tipo com `type()`. |
| `aulas/03_input.py` | Leitura de dados com `input()`, conversão explícita de tipos e interpolação de valores em mensagens. |
| `aulas/04_concatenacao.py` | Arquivo sem conteúdo no momento; o nome indica o tópico de concatenação. |
| `aulas/05_operadores.py` | Operadores aritméticos, de comparação e de atribuição composta; formatação numérica em saídas. |
| `aulas/06_strings.py` | Strings simples e multilinha, sensibilidade a maiúsculas/minúsculas, repetição e busca de conteúdo com `in`. |
| `aulas/07_index_slice.py` | Indexação e fatiamento de strings com início, fim e passo, incluindo índices negativos e inversão. |
| `aulas/08_metodos_str.py` | Métodos de string para alterar capitalização, centralizar, localizar, contar, substituir e dividir texto. |
| `aulas/09_lista.py` | Listas, acesso por índice e fatiamento para selecionar elementos e intervalos. |
| `aulas/10_metodos_listas.py` | Operações com listas: tamanho, busca de posição, inclusão, ordenação, cópia e remoção de itens. |
| `aulas/11_tuplas.py` | Tuplas como coleções ordenadas, consulta por índice, fatiamento e busca de posição. |
| `aulas/12_set_conjuntos.py` | Conjuntos, cardinalidade, inclusão e remoção de elementos; demonstração da unicidade dos elementos. |
| `aulas/13_dicionario.py` | Dicionários de chave e valor, leitura, consulta de chaves/valores, inclusão, atualização e remoção. |
| `aulas/14_dicionário_aninhado.py` | Dicionários aninhados para representar registros relacionados, acessar dados internos, inserir e excluir registros. |
| `aulas/15_condicao.py` | Fluxo condicional com `if`/`elif`/`else` para selecionar operações de uma calculadora e tratar divisão por zero. |
| `aulas/16_for.py` | Iteração com `for` e `range()`, controle com `break` e `continue` e cálculo de média de avaliações. |
| `aulas/17_while.py` | Repetição condicionada com `while`, controle de índice e contador, interrupção/pulo de iterações e cálculo de média. |
| `aulas/18_compressao_de_listas.py` | List comprehensions com filtros para gerar listas e buscar filmes; laço interativo de pesquisa com condição de saída. |
| `aulas/19_funcao.py` | Definição e chamada de funções, retorno de resultados e exemplos de cálculo e cadastro. |
| `aulas/20_argumentos_funcoes.py` | Parâmetros posicionais e padrão, passagem de argumentos e retorno de valores em funções. |
| `aulas/21_funcao_recursiva.py` | Recursão com casos-base para calcular fatorial e soma dos inteiros até um número. |
| `aulas/22_funcpes_argumentos_kwargs.py` | Argumentos variáveis: `*args` para valores posicionais e `**kwargs` para argumentos nomeados. |
| `aulas/23_funcao_lambda.py` | Funções lambda para operações concisas, validação de paridade, manipulação de strings e exemplos com filmes. |
| `exercicios/01_ex.py` | Formatação de nomes, inversão de texto com slicing e comparação de uma string com sua inversa para verificar palíndromo. |

## Execução

Execute um arquivo individual com Python 3, por exemplo:

```bash
python aulas/01_primeiro.py
```

Os scripts que solicitam dados usam entrada interativa pelo terminal.
