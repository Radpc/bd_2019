CREATE TABLE Categoria
(
    ID_categoria INT NOT NULL,
    Nome VARCHAR (30) NOT NULL,
    Pai INT REFERENCES Categoria (ID_categoria)
);