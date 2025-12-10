
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    ville VARCHAR(25),
    age INT
);

CREATE TABLE compte (
    id SERIAL PRIMARY KEY,
    type_compte VARCHAR(20) NOT NULL,
    id_cli INT,
    solde DECIMAL(12,2),
    CONSTRAINT fk_client FOREIGN KEY (id_cli) REFERENCES client(id)
);

CREATE TABLE transaction (
    id SERIAL PRIMARY KEY,
    id_compte INT NOT NULL,
    montant DECIMAL(12,2) NOT NULL,
    date_transaction TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_compte FOREIGN KEY (id_compte) REFERENCES compte(id)
);

CREATE TABLE agence (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    ville VARCHAR(25) NOT NULL
);

