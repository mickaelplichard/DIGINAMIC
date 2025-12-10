\c compta

SELECT * FROM article;

SELECT ref, designation FROM article WHERE prix > 2;

SELECT * FROM article WHERE prix >= 2 AND prix <= 6.25;

SELECT * FROM article WHERE prix BETWEEN 2 AND 6.25;
 
SELECT article.* FROM article JOIN fournisseur ON article.id_fou = fournisseur.id WHERE (article.prix < 2 OR article.prix > 6.25) AND fournisseur.nom = 'Française d''Imports' ORDER BY article.prix DESC;

SELECT article.* FROM article JOIN fournisseur ON article.id_fou = fournisseur.id WHERE fournisseur.nom IN ('Française d''Imports', 'Dubois & Fils');

SELECT article.* FROM article JOIN fournisseur ON article.id_fou = fournisseur.id WHERE fournisseur.nom NOT IN ('Française d''Imports', 'Dubois & Fils');

SELECT * FROM bon WHERE date_cmde BETWEEN '2019-02-01' AND '2019-04-30';
