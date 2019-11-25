# exprparser

O software deste repositório utiliza um parser criado com [ANTLR](http://antlr.org) para calcular valores de expressões aritméticas. No momento são válidas as sintaxes:

* `expressão * expressão`
* `expressão / expressão`
* `expressão + expressão`
* `expressão - expressão`

Onde `expressão` é um número inteiro.

## Executar

Antes de executar o software crie um arquivo texto com expressões aritméticas, uma em cada linha. Depois, execute o software no prompt indicando o arquivo com as expressões aritméticas. Por exemplo, supondo que o arquivo com as expressões seja `teste.expr` (há um arquivo com este nome no repositório como exemplo):

```
python Program.py teste.expr
```

A saída da execução, se bem-sucedida, será a lista das expressões aritméticas e seus valores.

## Ferramentas

Para que o software funcione, instale as dependências (no arquivo `requirements.txt`).

## Nota

Este software é uma demonstração dos conceitos de compiladores e da utilização do ANTLR para criá-los (análise léxica, análise sintática, análise semântica, gramática).
