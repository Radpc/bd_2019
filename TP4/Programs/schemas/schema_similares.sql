CREATE TABLE Similares
(
    ID_produto INT NOT NULL,
    ID_similar INT NOT NULL CHECK (ID_produto <> ID_similar),
    FOREIGN KEY (ID_produto) REFERENCES Produto(ID_produto),
    FOREIGN KEY (ID_similar) REFERENCES Produto(ID_produto)
);