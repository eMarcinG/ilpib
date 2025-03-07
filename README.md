#
# ilpib app
#

Aplikacja umożliwia tworzenie, aktualizowanie, usuwanie oraz wyświetlanie postów. Każdy post zawiera tytuł, opis, słowa kluczowe, URL, autora i adres IP. 

Aplikacja posiada wbudowaną walidację pól "title" i "keywords" oraz sprawdza mozliwość wykonania akcji aktualizacji i usuwania tylko dla autora wpisu.

Projekt zawiera również testy jednostkowe, które zapewniają poprawność działania funkcji i walidacji danych wprowadzanych do modelu Post.

## Wymagania

- Docker
- Docker Compose

## Instalacja

### Krok 1: Sklonuj repozytorium

git clone zzz

### Krok 2: Dodaj plik .env

Skopiuj plik .env dołączony do wiadomości email.

### Krok 3: Docker

Zbuduj i uruchom obraz Docker korzystajac z docker-composer:

docker-compose up --build

ważne: 
* konto superużytkownika utworzy się automatycznie na podstawie danych w .env

## Użycie

### admin Panel

Dostęp do panelu administracyjnego:
http://localhost:8000/admin
zaloguj się przy użyciu danych logowania superużytkownika.
Uwaga:
* użyj panelu administracyjnego, aby utworzyć dodatkowego użytkownika

### API

Punkty końcowe API są dostępne pod adresem http://localhost:8000/api/.

Uwaga:
Zdecydowanie zaleca się zainstalowanie rozszerzenia REST Client (dla Visual Studio Code)
i użycie pliku „new.http” ze wszystkimi dostępnymi punktami końcowymi.

1. Uzyskaj token dostępu i odświeżania, podając swoją nazwę użytkownika i hasło w treści żądania

POST http://localhost:8000/api/token/

2. Dodaj post

POST http://localhost:8002/api/posts/

{
    "title": "słowo   1",
    "description": "Opis mojego pierwszego posta.",
    "keywords": "słowo  1  , słowo  1, słowo3",
    "url": "http://example.com"
}

3. Pobierz listę wszystkich postów

GET http://localhost:8000/api/posts/

3. Pobierz konkretny post

GET http://localhost:8000/api/posts/1

4. Usun post

DELETE http://localhost:8000/api/posts/1/

4. Edytuj post

PATCH http://localhost:8000/api/posts/2/


## Testy

Uruchom testy następującą komendą:

docker-compose exec web python manage.py test

