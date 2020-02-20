# Käyttötapauksia
## Rooli: Käyttäjä
* Rekisteröityminen ja kirjautuminen
```sql
ÌNSERT INTO account (name, username, password) VALUES ('Nimi', 'username', 'password');

ÌNSERT INTO account (name, username, password) 
SELECT 'username'
WHERE NOT EXISTS (SELECT 1 FROM account WHERE username = 'username');
```
* Käyttäjä voi luoda useita muistilistoja esimerkiksi koulu/työ/koti
```sql
ÌNSERT INTO tasklist (name, account_id) VALUES ('Nimi', current_user.id);
```
* Käyttäjä voi listätä muistilistalle asioita (Syötteet validoitu)
```sql
ÌNSERT INTO task (name, tasklist_id) VALUES ('Nimi', current_list.id);
```
* Käyttäjä voi muokata muistilistalla olevia asioita esimerkiksi merkitä tehdyksi tai nimetä uudelleen
```sql
UPDATE task SET name = '?', urgency = ?, done = ? WHERE id = ?;
```
* Käyttäjä voi poistaa muistilistalta asioita tai muistilistoja
```sql
DELETE FROM task WHERE id = ?;
  
DELETE FROM task WHERE tasklist_id = ?;
DELETE FROM tasklist WHERE id = ?;
```
* Muistilistaa voidaan tarkastella kokonaisuudessaan
```sql
SELECT task.name, task.urgency, task.done FROM task
JOIN tasklist ON task.tasklist_id = tasklist.id
WHERE tasklist.id = ?;
```
* Käyttäjällä CRUD-oikeudet oman muistilistaan ja sen sisältämiin asioihin

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
```

