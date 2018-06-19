# Aluguel de imóveis

Este projeto é um sistema em Django que permite: 
	* Listar imóveis disponíveis
	* Listar imóveis próximo a um endereço específico
	* Cadastrar novos imóveis através de uma tela especificada
	
	

## Navegando no projeto

As funcionalidades do projeto podem ser acessadas através de uma barra de navegação com quatro abas: Home, Alugar Imóveis, Registrar Imóvel e Sobre.
	* Home: Dá acesso à página inicial do site.
	* Alugar imóveis: Dá acesso à página que lista os imóveis para alugar. Os imóveis podem ser listados sem distinção, por categoria e baseado nas proximidades de um endereço fornecido pelo usuário.
	* Registrar Imóvel: Dá acesso à uma página com um formulário para registrar um novo imóvel.
	* Sobre: Dá acesso à uma página padrão sobre o site sem conteúdo relevante.


Os endereços previamente cadastrados utilizados para teste são pontos de referência reais dentro das cidades. Todas estas cidades estão dentro do estado do Rio de Janeiro.

## Endereços Cadastrados
	* Rua Niterói, 14, Inoã, Maricá, RJ, Brasil, 24900000
	* Rua Francisco Sabino da Costa, 905 - Centro, Marica - RJ, Brasil, Cep 24900100
	* Rua Alvares de Castro, 346 - Centro, Marica - RJ, Brasil, Cep 24900880
	* Rua Quinze de Novembro, 8 - Centro, Niterói - RJ, 24020125
	* Avenida Feliciano Sodre, 14 - Centro, Niteroi - RJ, Brasil, Cep 24030010
	* Rodovia Amaral Peixoto, 116 - Rio do ouro, Niteroi - RJ, Brasil, Cep 24020074
	* Alameda Sao Boaventura, 1086 - Fonseca, Niteroi - RJ, Brasil, Cep 24120192
	* Avenida Brasil, 500 - Sao Cristovao, Rio de Janeiro - RJ, Brasil, Cep 20940070
	
## Endereços para testar listagem por proximidade
	* Com resultados:
	  * Endereços dos imóveis cadastrados
	  * Rua Amadeu Pugliese, 4, Centro, Maricá, RJ
	* Sem resultados:
	  * University Parkway, San Bernardino, California, US

	 
	 
	 
### Lógica da busca
As buscas de endereços foram utilizadas pela biblioteca fornecida pelo GoogleMaps.
Por simplicidade, o perímetro da busca é um quadrante cujo ponto médio dos lados do quadrante está a 0.1 graus de latitude e longitude do endereço buscado.
Ou seja, o endereço buscado está no centro de um quadrado de 0.2 graus de latitude e longitude. Um lado de 0.2 graus corresponde à distância de aproximadamente 16 quilômetros.



	 
## Dependências

O projeto foi realizado em Django com Python 3.6.2. 
É aconselhável que seja criado um ambiente virtual para execução do projeto. 
É disponibilizado um arquivo requirements.txt para facilitar a instalação das dependências do projeto.
Dito isto, com seu ambiente virtual ativado, a partir da pasta raiz do repositório, execute a seguinte linha de comando:
`pip install -r aluguelimoveis/requirements.txt`

Lembrando de verificar o divisor de diretórios correspondente do seu sistema operacional ('/' para o Linux, '\' Windows).


## Executando o projeto

Para rodar o projeto, é necessário executar o arquivo do projeto Django "manage.py". Para isso, execute a seguinte linha de comando a partir do diretório raiz do repositório:
`python aluguelimoveis/projectAluguel/manage.py runserver`

Este comando iniciará o servidor na máquina local com a porta 8000 como padrão. Assim, para acessar a página, abra o seu navegador e escreva: "localhost:8000" na barra de endereços.

	
	
## Observação

Dentre as informações obtidas para este projeto, vale mencionar que o estilo do conteúdo da página inicial foi pego diretamente de um template da [w3-schools](https://www.w3schools.com/w3css/tryw3css_templates_start_page.htm).