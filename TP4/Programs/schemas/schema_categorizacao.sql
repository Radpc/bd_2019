CREATE TABLE IF NOT EXISTS Categorizacao
(
    ASIN_produto CHAR(10) NOT NULL,
    Categoria VARCHAR(80) NOT NULL,
    FOREIGN KEY (ASIN_produto) REFERENCES Produto (ASIN)
);