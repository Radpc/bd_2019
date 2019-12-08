CREATE TABLE IF NOT EXISTS Review
(
    ASIN_produto CHAR(10) NOT NULL,
    ID_cliente CHAR(14) NOT NULL,
    Data DATE NOT NULL,
    Aval INT NOT NULL,
    Votos INT NOT NULL,
    Util INT NOT NULL,
    FOREIGN KEY (ASIN_produto) REFERENCES Produto (ASIN),
    CONSTRAINT CHK_Review CHECK (Aval <= 5 AND Aval >= 0 AND Votos >= Util)
);