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
    cpf CHAR(11) UNIQUE NOT NULL
);

CREATE TABLE contas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titular VARCHAR(100) NOT NULL UNIQUE,
    saldo DECIMAL(10, 2) NOT NULL DEFAULT 0,
    cpf CHAR(11),
    numero_conta VARCHAR(20) UNIQUE,
    FOREIGN KEY (cpf) REFERENCES perfis(cpf)
);

INSERT INTO perfis (tipo_perfil, titular, senha, celular, sobrenome, email, cpf) VALUES 
('Gerente Geral', 'admin', 'senha_admin', '1234567890', 'Admin', 'admin@example.com', '12345678910'),
('Chefe de Setor', 'chefe1', 'senha_chefe', '1234567891', 'Chefe', 'chefe@example.com', '12345678911'),
('Funcionário', 'funcionario1', 'senha_funcionario', '1234567892', 'Func', 'funcionario@example.com', '12345678912'),
('Cliente', 'cliente1', 'senha_cliente', '1234567893', 'Cliente', 'cliente1@example.com', '12345678913'),
('Cliente', 'cliente2', 'senha_cliente2', '1234567894', 'Cliente', 'cliente2@example.com', '12345678914'),
('Cliente', 'paulo', 'paulo', '1234567895', 'Silva', 'paulo@example.com', '12345678915'),
('Cliente', 'rafaela', 'rafaela', '1234567896', 'Santos', 'rafaela@example.com', '12345678916'),
('Cliente', 'carlos', 'carlos', '1234567897', 'Lima', 'carlos@example.com', '12345678917'),
('Cliente', 'gabriel', 'gabriel', '1234567898', 'Costa', 'gabriel@example.com', '12345678918'),
('Cliente', 'davi', 'davi', '1234567899', 'Alves', 'davi@example.com', '12345678919')
ON DUPLICATE KEY UPDATE senha=VALUES(senha);

INSERT INTO contas (titular, saldo, cpf, numero_conta) VALUES 
('cliente1', 1000.00, '12345678913', '1'),
('cliente2', 1500.00, '12345678914', '2'),
('paulo', 10000.00, '12345678915', '3'),
('carlos', 1000.00, '12345678917', '4'),
('gabriel', 1000.00, '12345678918', '5'),
('davi', 1000.00, '12345678919', '6'),
('rafaela', 1000.00, '12345678916', '7')
ON DUPLICATE KEY UPDATE saldo=VALUES(saldo);
