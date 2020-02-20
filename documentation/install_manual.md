# Asennusohje
Nouda lähdekoodi esimerkiksi komennolla 
```
$ git clone https://github.com/Pentza/tsoha-todolist.git
```
## Suorittaminen paikallisesti
Luo virtuaaliympäristö projektin juuressa komennolla
```
$ python3 -m venv venv
```
Käynnistä virtuaaliympäristö komennolla
```
$ source venv/bin/activate
```
Asenna riippuvuudet komennolla 
```
$ pip install -r requirements.txt
```
Suorita komennolla
```
$ python3 run.py
```
Sovellus avautuu selaimessa osoitteessa
```
localhost:5000
```

## Suorittaminen Herokussa
Oletetaan, että sinulla on Heroku käyttäjätili ja HerokuCLI asennettuna, sekä yllä mainitut ohjeet tehtynä.  
  
  
  Luodaan sovellus Herokuun komennolla
  ```
  $ heroku create  //Heroku generoi random nimen sovellukselle tai voit antaa parametreiksi oman
  ```
  Lisää Herokuun Postgre-liitännäinen komennolla
  ```
  $ heroku addons:create heroku-postgresql:hobby-dev
  ```
  Puske sovellus Herokuun komennolla
  ```
  $ git push heroku master
  ```
  
