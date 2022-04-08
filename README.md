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