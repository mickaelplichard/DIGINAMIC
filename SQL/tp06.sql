SET SQL_SAFE_UPDATES = 0;

DELETE FROM compo USING bon WHERE compo.id_bon = bon.id AND DATE_TRUNC('month', bon.date_cmde) = '2019-04-01';

DELETE FROM bon WHERE DATE_TRUNC('month', date_cmde) = '2019-04-01';