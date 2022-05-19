# CeneoScrapper

##Struktura opinii w serwisie Ceneo [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|obj|
|indentyfikator opinii|div.js_product-review["data-entry-id"\]|opinion_id|int|
|autor opinii|span.user-post__author-name|author|||
|rekomendacja|span.user-post__author-recomendation > em|recommendation||
|liczba gwiazdek|span.user-post__score_count|stars|string|
|treść opinii|div.user-post__text|content|string|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|pros|obj|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|cons||
|dla ilu osób przydatna|buttton.vote-yes > span|useful|int|
|dla ilu osób nieprzydatna|buttton.vote-no > span|useless|int|
|data wystawienie opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date|list|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|list|


## Etapy pracy nad projektem
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojedycznej opinii do słownika
3. Ppbranie wszytskich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku .json
5. Pobranie wszytskich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie mozliwości podania numeru produktu przez uzytkownika
7. Optymalizacja kodu
    a. utworzenie funkcji do ekstrakcji elementów strony
    b. utworzenie słownika selektorów
    c. uycie dictionary comprehension do pobrania składowych pojedynczej opinii na podstawie słownika selektorów
8. Analiza pobranych opinii dla konkretnego produktu
    a. wyliczenie podstawowych statystyk 
        - liczba opinii
        - liczba opinii dla których podano zalety
        - liczba opinii dla których podanop wady
        - średnia ocena produktu
    b. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        - udział występowania poszczególnych ocen