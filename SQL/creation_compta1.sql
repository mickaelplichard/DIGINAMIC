DROP DATABASE IF EXISTS compta;
CREATE DATABASE compta;

CREATE TABLE IF NOT EXISTS fournisseur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(25) NOT NULL
);

CREATE TABLE IF NOT EXISTS article (
    id SERIAL PRIMARY KEY,
    ref VARCHAR(13) NOT NULL,
    designation VARCHAR(255) NOT NULL,
    prix DECIMAL(7,2) NOT NULL,
    id_fou INT NOT NULL,
    CONSTRAINT fk_article_fou FOREIGN KEY (id_fou) REFERENCES fournisseur(id)
);

CREATE TABLE IF NOT EXISTS bon (
    id SERIAL PRIMARY KEY,
    numero INT,
    date_cmde TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delai INT,
    id_fou INT NOT NULL,
    CONSTRAINT fk_bon_fou FOREIGN KEY (id_fou) REFERENCES fournisseur(id)
);

CREATE TABLE IF NOT EXISTS compo (
    id SERIAL PRIMARY KEY,
    id_art INT NOT NULL,
    id_bon INT NOT NULL,
    qte INT NOT NULL,
    CONSTRAINT fk_compo_art FOREIGN KEY (id_art) REFERENCES article(id),
    CONSTRAINT fk_compo_bon FOREIGN KEY (id_bon) REFERENCES bon(id)
);
