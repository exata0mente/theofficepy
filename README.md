#  Aprendendo POO com o chat GPT na temática de The Office

Eu pedi para o chat GPT-3 da OpenAI ministrar um curso de Python Orientado a Objetos para mim. Para tornar interessante pedi que fosse utilizado o tema de The Office como exemplo.

De fato o conteúdo do curso ficou interessante inclusive com a adição de um tema que particularmente gosto muito. 

Importante já ressaltar aqui que apesar de interessante as aulas propostas pelo chat GPT-3, elas não substituem um ensino formal, tampouco livros e artigos. Além disso, para conseguir um conteúdo minimamente fluído e que seguisse uma sequência, não foi fácil.

Entre idas e vindas, utilizei os seguintes comandos

> Me dê um curso de Python Orientado a Objetos, utilizando como tema a série The Office. O curso deve considerar o Python 3.x e deve ser para iniciantes. Apresente a lista de aulas para que eu possa indicar em qual devemos iniciar

Como qualquer modelo de linguagem, é importante dar o máximo de detalhes possíveis. Veja que enfatizo qual o tema, qual a versão do python a ser seguido, peço uma lista das aulas que serão apresentadas (isso é importante), ressalto que é para o chat GPT-3 ministrar o curso para mim. Quanto mais especifico for a solicitação, mais refinado é o resultado.

A resposta foi:

```
Claro! Aqui está uma lista de aulas para um curso introdutório de Python orientado a objetos com o tema da série The Office:

    Introdução a Python Orientado a Objetos (OO) e a série The Office
        O que é Python OO e por que é útil?
        Visão geral da série The Office
        Instalação do Python 3.x e ambiente de desenvolvimento

    Classes e objetos em Python
        O que é uma classe em Python e como definir uma classe?
        O que é um objeto em Python e como criar um objeto?
        Criando uma classe Personagem e objetos dos personagens de The Office

    Atributos e métodos em Python
        O que são atributos de classe e atributos de instância?
        Como definir métodos de instância em uma classe?
        Criando atributos e métodos para a classe Personagem

    Herança e polimorfismo em Python
        O que é herança em Python e como criar uma classe filha?
        Como usar a função super() para acessar métodos da classe pai?
        O que é polimorfismo em Python e como usá-lo?
        Criando uma classe de Personagem e subclasses para as diferentes posições na Dunder Mifflin

    Encapsulamento e abstração em Python
        O que é encapsulamento em Python e por que é importante?
        Como usar o conceito de abstração em Python?
        Implementando encapsulamento e abstração na classe Personagem

    Gerenciamento de erros em Python
        O que são exceções em Python e como tratá-las?
        Usando blocos try-except para lidar com erros
        Lidando com exceções na classe Personagem

    Projetando um sistema de personagens em The Office
        Projeto e implementação de uma classe para gerenciar personagens da série
        Criando métodos para adicionar, remover e buscar personagens na classe PersonagensTheOffice
        Criando um programa para interagir com a classe PersonagensTheOffice

Espero que essa lista ajude! Você pode começar com a aula 1 se for iniciante em Python OO. Caso contrário, pode pular para a aula que mais lhe interessa.
```

Desta forma, eu indiquei a aula que eu gostaria de iniciar e alguns "quantificadores" que julguei interessante. Novamente, detalhar é importante. Antes eu mandava comandos como "seguir aula", "próxima aula", "continuar" e o chat GPT-3 não entendia, repetia ou voltava em conteúdos já abordados.

Então, adotei o seguinte texto:

> Ir para a próxima aula: "Gerenciamento de erros em Python" mantendo a temática proposta. Ao final proponha um exercício e também cite uma referência, de preferência livro, e o capitulo que aborde o tema apresentado em aula.

Assim além de garantir que o conteúdo fosse seguido, eu também pedia um exercício (o que foi bem legal) e também uma referência pois, novamente, o chatgpt é um assistente (pelo menos ainda) de estudos.

E de fato ele cumpriu as especificações. Inclusive, quando eu pedia a correção do exercício proposto ele me dava a resposta coerente.

É importante lembrar que o chat GPT-3 tem limitações de caracteres, então uma abordagem para aulas que eu acreditava ser longas, era a seguinte: 

>   Referente a próxima aula "Projetando um sistema de personagens em The Office" liste os conteúdos que serão ministrados

E aí era retornado uma lista e então eu respondia

> Inicie então a parte 1 : "Análise de requisitos: identificar as necessidades do sistema de personagens para a aplicação em The Office"

Importante: Tem perda de informações no decorrer dos conteúdos. Então por exemplo, tinham conteúdos em que as classes tinham atributos de escritório e em outros seguintes não, métodos que eram criados em uma aula e não eram utilizados em outras. Então, reforçando, utilizei o chat GPT-3 como um assistente de estudos, não como um professor formal.

Conclusão: Eu gostei. A possibilidade de ter um estudo direcionado para um tema personalizado é muito interessante. Gostei e pretendo fazer mais testes.

# Conteúdos abordados

Aqui vou só colocar a lista gerada pelo chat GPT-3. Dá pra ter noção na profundidade que ele dar.

##  Curso introdutório de Python orientado a objetos com o tema da série The Office

- **Armazenar informações sobre os personagens**: o sistema deve ser capaz de armazenar informações sobre todos os personagens da série, incluindo nome, idade, cargo, e outros detalhes relevantes.
- **Identificar relacionamentos entre personagens**: o sistema deve ser capaz de identificar os relacionamentos entre os personagens, como amizades, relacionamentos amorosos, inimizades, etc.
- **Exibir informações sobre os personagens**: o sistema deve ser capaz de exibir informações sobre os personagens, incluindo seus relacionamentos com outros personagens e outros detalhes relevantes.
- **Atualizar informações dos personagens**: o sistema deve permitir a atualização das informações dos personagens, como alterar seu cargo ou idade, por exemplo.
- **Adicionar e remover personagens**: o sistema deve permitir a adição e remoção de personagens da série, se necessário.

## Curso intermediário em Python Orientado a Objetos:

- **Revisão do básico de Python e Orientação a Objetos**
- **Herança múltipla em Python**: como modelar personagens com múltiplas relações e habilidades
- **Métodos mágicos em Python**: como customizar a exibição e manipulação dos personagens
- **Tratamento de exceções em Python**: como lidar com erros no sistema de personagens
- **Persistência de dados em Python**: como salvar informações dos personagens em um banco de dados
- **Testes em Python**: como testar o sistema de personagens e garantir a qualidade do código
- **Interfaces gráficas em Python**: como criar uma interface gráfica para exibir e manipular informações dos personagens

# Próximos passos

Pretendo ir adicionando camadas de dificuldades e adicionando mais detalhes em minhas solicitações. A ideia é criar um pacote de python com auxilio do chatgpt. Será que consigo?