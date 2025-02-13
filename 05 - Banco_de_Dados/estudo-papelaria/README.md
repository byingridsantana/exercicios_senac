# Banco de dados Papelaria

## Modelo Conceitual

O modelo conceitual representa uma visão abstrata dos dados, sem se preocupar com a implementação técnica. Para uma papelaria, podemos identificar as seguintes entidades:.

* Produto: Nome, descrição, preço, quantidade em estoque, categoria;
* Cliente: Nome, CPF, endereço, telefone;
* Pedido: Número do pedido, data do pedido, cliente, produto e quantidade;

## Modelagem Conceitual: Relacionamentos

* Um produto pode ter muitos pedidos.
* Um cliente pode fazer muitos pedidos.
* Um pedido tem muitos produtos.


## Modelo Lógico

O modelo lógico traduz o modelo conceitual para uma estrutura de dados mais formal, geralmente utilizando um diagrama entidade-relacionamento (ER). Para o MySQL, podemos definir as seguintes tabelas:

* produtos: id_produto (PK), nome, descricao, preco, quantidade, categoria
* clientes: id_cliente (PK), nome, cpf(UK), endereco, telefone
* pedidos: id_pedido (PK), data_pedido, id_cliente (FK), 
itens_pedido: id_item (PK), id_pedido (FK), id_produto (FK), quantidade

* Chaves:
PK: Chave primária
FK: Chave estrangeira 
UK: Chave única


## Modelo Físico

O modelo físico define a implementação do banco de dados em um sistema gerenciador de banco de dados específico, no caso, o MySQL.


``` sql

-- Para criar o banco de dados CREATE DATABASE / USE:

CREATE DATABASE papelaria;
USE papelaria;

-- Para criar as tabelas CREATE TABLE:

CREATE TABLE produtos (
id_produto INT AUTO_INCREMENT PRIMARY KEY,  
nome VARCHAR(100),  
descricao TEXT,  
preco DECIMAL(10,2),  
quantidade INT,  
categoria VARCHAR(50));

CREATE TABLE pedidos ( 
id_pedido INT AUTO_INCREMENT PRIMARY KEY,
data_pedido DATE, 
id_cliente INT);

CREATE TABLE itens_pedido (
id_item INT AUTO_INCREMENT PRIMARY KEY,
id_pedido INT,
id_produto INT,
quantidade INT);

CREATE TABLE clientes ( 
id_cliente INT AUTO_INCREMENT PRIMARY KEY,  nome VARCHAR(100),
cpf VARCHAR(11) not null UNIQUE,
endereco TEXT,
telefone VARCHAR(20));

/*
Estabelecer o relacionaMento entre as tabelas pedidos e clientes.
Vamos fazer a ligação do campo id_cliente da tabela cliente com id_cliente da tabela pedidos.
O id_cliente da tabela pedidos é chave estrangeira
*/

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_pk_cliente
FOREIGN KEY pedidos(id_cliente) 
REFERENCES clientes(id_cliente);

ALTER TABLE itens_pedido
ADD CONSTRAINT fk_itens_pedido_pk_pedidos
FOREIGN KEY itens_pedido(id_pedido) 
REFERENCES pedidos(id_pedido);

ALTER TABLE itens_pedido
ADD constraint fk_itens_pedido_pk_produtos
foreign key itens_pedido(id_produto)
REFERENCES produtos(id_produto);

-- Descreve a estrutura da tabela: 
DESCRIBE produtos;
DESCRIBE clientes;
DESCRIBE pedidos;
DESCRIBE itens_pedido;

-- Para inserir dados dentro de uma tabela (produtos):
INSERT INTO produtos(nome, descricao, preco, quantidade, categoria) VALUES ("Mouse","Mouse sem Fio", 45.90, 23, "Informática");

-- Para inserir dados dentro de uma tabela (produtos):
INSERT INTO produtos(nome, descricao, preco, quantidade, categoria) VALUES ("Caderno Universitário","Caderno com 400 páginas", 25.90, 30, "Escolar");

-- Para inserir dados dentro de uma tabela (clientes):
INSERT INTO clientes(nome,cpf,endereco, telefone) VALUES ("Avulso","00000000001","Rua Nova","(11) 9999-9999");
INSERT INTO clientes(nome,cpf,endereco, telefone) VALUES ("Vanessa","00000000002","Rua do Jardim","(11) 2222-2222");

-- Para inserir dados dentro de uma tabela (pedidos):
INSERT INTO pedidos(data_pedido,id_pedido) VALUES (now(),4);

-- Para inserir dados dentro de uma tabela (itens_pedido):
INSERT INTO itens_pedido(id_pedido, id_produto, quantidade)
VALUES (4,2,4);

-- Para mostrar os dados que foram inseridos:
SELECT * FROM produtos;
SELECT * FROM clientes;
SELECT * FROM pedidos;
SELECT * FROM itens_pedido;

```