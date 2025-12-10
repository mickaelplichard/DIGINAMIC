\c compta

SELECT * FROM article;

SELECT ref, designation FROM article WHERE prix > 2;

SELECT * FROM article WHERE prix >= 2 AND prix <= 6.25;

SELECT * FROM article WHERE prix BETWEEN 2 AND 6.25;
 
SELECT a.* FROM article a JOIN fournisseur f ON a.id_fou = f.id WHERE (a.prix < 2 OR a.prix > 6.25) AND f.nom = 'Française d''Imports' ORDER BY a.prix DESC;

SELECT a.* FROM article a JOIN fournisseur f ON a.id_fou = f.id WHERE f.nom IN ('Française d''Imports', 'Dubois & Fils');

SELECT a.* FROM article a JOIN fournisseur f ON a.id_fou = f.id WHERE f.nom NOT IN ('Française d''Imports', 'Dubois & Fils');

SELECT * FROM bon WHERE date_cmde BETWEEN '2019-02-01' AND '2019-04-30';
