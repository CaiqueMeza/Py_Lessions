# Late Fine
Desenvolvi esta calculadora para uma simulação de atraso na data de devolução de um livro.

O usuário insere a data de retirada e data de devolução, em seguida o console retona se o usuário teve morosidade na devolução, aplicando multas caso teve demora.

### As multas se comportam da seguinte forma:

1. A data para devolução sempre será de até 5 dias após a retirada;
2. Caso passe 5 dias:
    + entre 1 a 3 dias de atraso = multa de R$ 0,50 por dia de atraso;
    + entre 4 a 7 dias de atraso = multa de R$ 1,00 por dia de atraso;
    + acima de 7 dias de atraso = multa de R$ 2,00 por dia de atraso.

### Conceitos abordados:

+ Usei pela primeira vez a biblioteca **__datetime__** para manipulação de datas;
+ uso de loopings **__(while)__**;
+ uso de condições **__(if, elif e else)__**;
+ formatação de strings **__(fstring)__**.




# English version
I delevoped this calculator for a book late fine simulation.

The user input the checkin and checkout date time, after that the terminal return the conditions of checkout, applyng fees for late checkout.

### Fees' behaviors:

1. The checkout aways will be until 5 days after checkin;
2. In case after 5 days:
    + between 1 to 3 days late = R$ 0,50 fee for each late day;
    + between 4 to 7 days late = R$ 1,00 fee for each late day;
    + above 7 days = R$ 2,00 fee for each late day.

### Concepts covered:

+ I used for first time **__datetime__** library for date manipulation;
+ use of loopings **__(while)__**;
+ use of conditions **__(if, elif, else)__**;
+ string formatting **__(fstring)__**.
