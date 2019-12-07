CREATE TABLE IF NOT EXISTS Produto
(
    ID_produto INT NOT NULL,
    ASIN CHAR(10) NOT NULL,
    Nome VARCHAR(300) NOT NULL,
    Group VARCHAR(30),
    Rank INT NOT NULL CHECK (Rank >= 0),
    PRIMARY KEY (ID_produto)
);