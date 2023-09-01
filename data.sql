-- Création de la table source
CREATE TABLE table_source (
    id INTEGER  PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    age INTEGER,
    ville VARCHAR(50)
);

-- Insertion des données
INSERT INTO table_source (nom, prenom, age, ville)
VALUES
    ('Dupont', 'Marie', 32, 'Paris'),
    ('Martin', 'Pierre', 28, 'Lyon'),
    ('Leroy', 'Sophie', 45, 'Marseille'),
    ('Roux', 'Thomas', 22, 'Toulouse'),
    ('Girard', 'Emma', 29, 'Bordeaux'),
    ('Leclerc', 'Nicolas', 38, 'Lille'),
    ('Fournier', 'Julie', 31, 'Nantes'),
    ('Moreau', 'Alex', 40, 'Strasbourg'),
    ('Lefebvre', 'Anna', 27, 'Rennes'),
    ('Petit', 'Louis', 55, 'Nice');
