-- # Fil för skapande av databasen för replog-programmet

-- # Fält att skapa:	
--
--	maskin_id
--	felkod
--	maskintyp
--	felbeskrivning
--	koll_komp
--	bytt_komp
--	resultat


CREATE TABLE reparation ( 
Maskin_ID varchar(6), 
Felkod varchar(6), 
Maskintyp varchar(12), 
Felbeskrivning varchar(255), 
Kollade_Komponenter varchar(255), 
Bytade_Komponenter varchar(255), 
Resultat varchar(255) 
);
