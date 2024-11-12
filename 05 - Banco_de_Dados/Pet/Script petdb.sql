-- Criar bancos de dados com comoando CREATE DATABASE
CREATE DATABASE petdb; 
-- Selecionar o banco de dados petdb com o comando USE
USE petdb;
-- Criar a tabela pessoa com o comando CREATE TABLE 
CREATE TABLE pessoa(
cod_pes int auto_increment primary key,
nome varchar(100) not null,
cpf numeric(11) not null unique, 
email varchar(100) not null unique, 
endereco varchar (100) not null, 
telefone varchar (20) not null
);

CREATE TABLE responsavel(
cod_res int auto_increment primary key,
cod_pes int not null, 
dia_venc numeric(2) not null 
);

CREATE TABLE pet(
cod_pet int auto_increment primary key, 
cod_res int not null, 
nome varchar(100) not null, 
dt_nasc date not null,
rga numeric(10) not null unique, 
cor varchar(50), 
especie varchar(50)
);

CREATE TABLE veterinario(
cod_vet int auto_increment primary key,
cod_pes int not null, 
crmv numeric(20) not null unique, 
especialidade varchar(30) not null
);

CREATE TABLE consulta(
cod_con int auto_increment primary key,
cod_pet int not null,
cod_vet int not null,
horario time, 
dt_consulta date
);

-- Criar os relacionamentos
ALTER TABLE responsavel 
ADD CONSTRAINT fk_responsavel_pk_pessoa 
FOREIGN KEY responsavel(cod_pes)
REFERENCES pessoa(cod_pes);

ALTER TABLE veterinario 
ADD CONSTRAINT fk_veterinario_pk_pessoa
FOREIGN KEY veterinario(cod_pes)
REFERENCES pessoa(cod_pes);

ALTER TABLE pet 
ADD CONSTRAINT fk_pet_pk_responsavel 
FOREIGN KEY pet(cod_res)
references responsavel(cod_res);

SELECT * FROM pet;

ALTER TABLE consulta 
ADD CONSTRAINT fk_consulta_pk_pet 
FOREIGN KEY consulta(cod_pet)
REFERENCES pet(cod_pet);

ALTER TABLE consulta 
ADD CONSTRAINT fk_consulta_pk_veterinario
FOREIGN KEY consulta(cod_vet)
REFERENCES veterinario(cod_vet);

-- vamos cadastrar os dados nas tabelas
DESCRIBE veterinario;
DESCRIBE pessoa;
SELECT * FROM pessoa;
SELECT * FROM veterinario;

-- cadastro de pessoa
INSERT INTO pessoa(nome, cpf, email, endereco, telefone) VALUES ('Margarete', 25625893563, "margarete@gmail.com", "Rua Galvão Torres,12", "(11)2563-5896");
INSERT INTO pessoa(nome, cpf, email, endereco, telefone) VALUES ('João', 25625898696, "joao@gmail.com", "Rua Guilherme Almeida, 32", "(11)2253-5596");
INSERT INTO pessoa(nome, cpf, email, endereco, telefone) VALUES ('Mayara', 25625895896, "mayara@gmail.com", "Rua Margaridas, 12", "(11)2253-5266");
INSERT INTO pessoa(nome, cpf, email, endereco, telefone) VALUES ('Mariana', 25625892589, "mariana@gmail.com", "Rua Mirim, 32", "(11)2253-5825");

-- cadastro de veterinario 

INSERT INTO veterinario(cod_pes, crmv, especialidade) VALUES (1,41548,"Cirurgia");
INSERT INTO veterinario(cod_pes, crmv, especialidade) VALUES (2,41549,"Clinico");

describe responsavel;
INSERT INTO responsavel(cod_pes, dia_venc) VALUES (3,10);
INSERT INTO responsavel(cod_pes,dia_venc) VALUES (4,5);

SELECT * FROM responsavel;
DESCRIBE pet;

SELECT * FROM pet;

-- cadastro de pet 

INSERT INTO pet(cod_res,nome,dt_nasc, rga,cor, especie)
VALUE (5, "Paçoca", "2020-10-12", 4575, "caramelo", "Cachorro");

INSERT INTO pet(cod_res,nome,dt_nasc, rga,cor, especie)
VALUE (5, "Mel", "2021-09-20", 4574, "Preto", "Gato");

INSERT INTO pet(cod_res,nome,dt_nasc, rga,cor, especie)
VALUE (5, "Belo", "2021-09-20", 2575, "Amarelo e Vermelho", "Passaro");

INSERT INTO pet(cod_res,nome,dt_nasc, rga,cor, especie)
VALUE (6, "Pudim", "2020-10-15", 2576, "Preto", "Gato");

INSERT INTO pet(cod_res,nome,dt_nasc, rga,cor, especie)
VALUE (6, "Mya", "2019-10-18", 2577, "Marrom", "Gato");

INSERT INTO pet(cod_res,nome,dt_nasc, rga,cor, especie)
VALUE (6, "Pingo", "2018-08-17", 2578, "Preto", "Gato");

-- Inserir Consulta

INSERT INTO consulta(cod_pet, cod_vet, horario, dt_consulta) VALUES (4,1,"10:45","2024-12-14");

SELECT * FROM pessoa where cod_pes = 1;
SELECT * FROM pessoa order by nome;
SELECT * FROM pessoa where nome like 'm%';
SELECT * FROM pessoa where nome like '%a';
SELECT * FROM pessoa where nome like '%o%';
