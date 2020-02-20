## Käyttötapauksia
# Rooli: Käyttäjä
- Rekisteröityminen ja kirjautuminen
* Käyttäjä voi luoda useita muistilistoja esimerkiksi koulu/työ/koti
* Käyttäjä voi listätä muistilistalle asioita (Syötteet validoitu)
* Käyttäjä voi muokata muistilistalla olevia asioita esimerkiksi merkitä tehdyksi tai nimetä uudelleen
* Käyttäjä voi poistaa muistilistalta asioita
* Muistilistaa voidaan tarkastella kokonaisuudessaan esimerkiksi suodattamalla kiireellisyyden mukaan
* Ylläpitäjällä täydet CRUD-oikeudet kaikkeen
* Normaalilla käyttäjällä CRUD-oikeudet oman muistilistan sisältämiin asioihin

## Create table -lauseet
```sql
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE tasklist (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE task (
	date_created DATETIME, 
	date_modified DATETIME, 
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	urgency INTEGER, 
	done BOOLEAN NOT NULL, 
	tasklist_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (done IN (0, 1)), 
	FOREIGN KEY(tasklist_id) REFERENCES tasklist (id)
);


