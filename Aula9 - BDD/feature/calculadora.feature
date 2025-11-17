Feature: Calculadora
    Como aluno de automação de testes de software
    Eu quero escrever um exemplo usando pytest-bdd
    Como um exemplo de soma de dois números

Scenario: Soma dois numeros
    Given eu tenho o número 2 como entrada para a Calculadora
    And eu também tenho o número 7 como entrada para a Calculadora
    When eu solicito que realize a soma
    Then o resultado deve ser 9
    
