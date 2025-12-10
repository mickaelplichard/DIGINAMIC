SELECT * FROM article ORDER BY designation ASC;

SELECT * FROM article ORDER BY prix DESC;

SELECT * FROM article WHERE designation ILIKE '%boulon%' ORDER BY prix ASC;

SELECT * FROM article WHERE designation LIKE '%sachet%';

SELECT * FROM article WHERE designation ILIKE '%sachet%';

SELECT article.*, fournisseur.nom FROM article JOIN fournisseur ON article.id_fou = fournisseur.id ORDER BY fournisseur.nom ASC, article.prix DESC;

SELECT article.* FROM article JOIN fournisseur ON article.id_fou = fournisseur.id WHERE fournisseur.nom = 'Dubois & Fils';

SELECT AVG(article.prix) AS moyenne_prix FROM article JOIN fournisseur ON article.id_fou = fournisseur.id WHERE fournisseur.nom = 'Dubois & Fils';

SELECT fournisseur.nom, AVG(article.prix) AS moyenne_prix FROM article JOIN fournisseur ON article.id_fou = fournisseur.id GROUP BY fournisseur.nom ORDER BY fournisseur.nom ASC;

SELECT * FROM bon WHERE date_cmde BETWEEN '2019-03-01' AND '2019-04-05 12:00:00';

SELECT DISTINCT bon.* FROM bon JOIN compo ON bon.id = compo.id_bon JOIN article ON compo.id_art = article.id WHERE article.designation ILIKE '%boulon%';

SELECT DISTINCT bon.id, bon.numero, bon.date_cmde, fournisseur.nom AS fournisseur FROM bon JOIN compo ON bon.id = compo.id_bon JOIN article ON compo.id_art = article.id JOIN fournisseur ON article.id_fou = fournisseur.id WHERE article.designation ILIKE '%boulon%';

SELECT bon.id AS bon_id, SUM(article.prix * compo.qte) AS total FROM bon JOIN compo ON bon.id = compo.id_bon JOIN article ON compo.id_art = article.id GROUP BY bon.id ORDER BY bon.id;

SELECT bon.id AS bon_id, SUM(compo.qte) AS total_articles FROM bon JOIN compo ON bon.id = compo.id_bon GROUP BY bon.id ORDER BY bon.id;

SELECT bon.id AS bon_id, SUM(compo.qte) AS total_articles FROM bon JOIN compo ON bon.id = compo.id_bon GROUP BY bon.id HAVING SUM(compo.qte) > 25 ORDER BY bon.id;

SELECT SUM(article.prix * compo.qte) AS total_avril FROM bon JOIN compo ON bon.id = compo.id_bon JOIN article ON compo.id_art = article.id WHERE DATE_TRUNC('month', b.date_cmde) = '2019-04-01';

