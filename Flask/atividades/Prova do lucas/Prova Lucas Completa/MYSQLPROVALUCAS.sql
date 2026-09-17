create database lanchonete;
use lanchonete; #Criando e usando os databases

create table cardapio(
id int auto_increment primary key,
nome varchar(100) not null,
preco decimal(10,2) not null,
tipo varchar(30),
disponivel boolean default True); #Criando a tabela e seus respectivos valores que devem ser preenchidos

insert into cardapio(nome, preco, tipo, disponivel) VALUES
('X Burguer', 30.99, 'Lanche', true),
('Pudim', 9.25, 'Sobremesa', true),
('Batata Frita', 15.99, 'Lanche', true),
('Taça de Sorvete', 12.89, 'Sobremesa', False),
('Coca cola', 9.99, 'Bebida', true); #Preenchendo os valores da tabela

select nome, preco from cardapio
order by preco; #exibindo de ordem crescente de preço

select * from cardapio
where tipo = 'Lanche'; #exibindo todos contendo o tipo lanche

select * from cardapio
where nome like '%Burguer'; #exibindo nome que contém Burguer

update cardapio
set preco = 35.99
where id = 1; #Dando update no preço do item de ID 1

update cardapio
set disponivel = False
where id=2; #Dando update na disponibilidade do item com ID 2

select * from cardapio;