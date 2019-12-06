CREATE TABLE Review
(
    Data DATE NOT NULL,
    Aval INT NOT NULL,
    Util INT NOT NULL,
    Votos INT NOT NULL,
    ID_produto INT NOT NULL,
    ID_cliente CHAR(14) NOT NULL,
    FOREIGN KEY (ID_produto) REFERENCES Produto (ID_produto),
    FOREIGN KEY (ID_cliente) REFERENCES Cliente (ID_cliente),
    CONSTRAINT CHK_Review CHECK (Aval <= 5 AND Aval >= 0 AND Votos >= Util)
);