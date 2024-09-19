CREATE DATABASE bancoparca;
USE bancoparca;


CREATE TABLE perfis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_perfil ENUM('Gerente Geral', 'Chefe de Setor', 'Funcionário', 'Cliente') NOT NULL,
    titular VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    celular VARCHAR(20),
    sobrenome VARCHAR(50),
    email VARCHAR(100),
    cpf VARCHAR(11) UNIQUE
);

CREATE TABLE contas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titular VARCHAR(100) NOT NULL UNIQUE,
    saldo DECIMAL(10, 2) NOT NULL DEFAULT 0,
    cpf VARCHAR(11),
    numero_conta VARCHAR(20),
    FOREIGN KEY (cpf) REFERENCES perfis(cpf) 
);


INSERT INTO perfis (tipo_perfil, titular, senha, celular,sobrenome,email,cpf) VALUES 
('Gerente Geral', 'admin', 'senha_admin'),
('Chefe de Setor', 'chefe1', 'senha_chefe'),
('Funcionário', 'funcionario1', 'senha_funcionario'),
('Cliente', 'cliente1', 'senha_cliente'),
('Cliente', 'cliente2', 'senha_cliente2'),
('Cliente', 'paulo', 'paulo'),
('Cliente', 'rafaela', 'rafaela'),
('Cliente', 'carlos', 'carlos'),
('Cliente', 'gabriel', 'gabriel'),
('Cliente', 'davi', 'davi'),
('Gerente Geral', 'admpaulo', 'paulo'),
('Gerente Geral', 'admrafaela', 'rafaela'),
('Gerente Geral', 'admcarlos', 'carlos'),
('Gerente Geral', 'admgabriel', 'gabriel'),
('Gerente Geral', 'admdavi', 'davi')
ON DUPLICATE KEY UPDATE senha=VALUES(senha);

INSERT INTO contas (titular, saldo, cpf, numero_conta) VALUES 
('cliente1', 1000.00,12345678910,1),
('cliente2', 1500.00, 12345678911,2),
('paulo', 10000.00, 12345678912,3),
('carlos', 1000.00, 12345678913,4),
('gabriel', 1000.00,12345678914,5),
('davi', 1000.00,12345678915,6),
('rafaela', 1000.00,12345678916,7)
ON DUPLICATE KEY UPDATE saldo=VALUES(saldo);

