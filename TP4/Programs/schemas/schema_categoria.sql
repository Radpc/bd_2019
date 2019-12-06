CREATE TABLE IF NOT EXISTS Categoria
(
    ID_categoria INT NOT NULL,
    Nome VARCHAR (30) NOT NULL,
    Pai INT REFERENCES Categoria (ID_categoria),
    PRIMARY KEY (ID_categoria)
);