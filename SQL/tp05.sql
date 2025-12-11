UPDATE article SET designation = LOWER(designation) WHERE id = 2;

UPDATE article SET designation = UPPER(designation) WHERE prix > 10;

UPDATE article SET prix = prix * 0.9 WHERE id NOT IN (SELECT id_art FROM compo);

UPDATE compo SET qte = qte * 2 FROM article JOIN fournisseur ON article.id_fou = fournisseur.id WHERE compo.id_art = article.id AND fournisseur.nom = 'Française d''Imports';

UPDATE article SET designation = TRIM(SUBSTRING(designation FROM 1 FOR POSITION('(' IN designation) - 1)) WHERE POSITION('(' IN designation) > 0;