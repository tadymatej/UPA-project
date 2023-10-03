# Návrh datasetů

## 1) Databáze časových řad (InfluxDB)

### Název datasetu: 
    Kvalita ovzduší
    
### Popis datasetu: 
Data o kvalitě ovzduší ze stanic na území města Brna. Nejedná se o verifikovaná data. Stanice jsou ve správě ČHMÚ, města Brna a Státního zdravotnického ústavu Ostrava. Data a jejich aktualizace je uvedená níže.

### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2F4907e5c199620d99a44c1ec388703cd5


## 2) Grafová Databáze (Neo4J)

### Název datasetu:
    Intenzita dopravy - Intenzita cyklistů

### Popis datasetu:
Pentlogramy intenzity dopravy zpracovávají pravidelně Brněnské komunikace, a.s. (dále zkráceně BKOM). Výstupy pentlogramů jsou schémata uzlů a úseků mezi nimi. Tato data jsou od roku 2016 zpracována do gisové podoby (SHP) nad uličním grafem a jsou s vydáním nového pentlogramu doplněna. Pentlogramy sledují intenzitu motorových vozidel a cyklistů.   Intenzita cyklistů je zpracovávána jednou za 2 roky (zpracované 2016, 2018, 2020). Intenzity jsou vizualizovány šířkou jednotlivých úseků a popisem číselné hodnoty, která definuje počet cyklistů (v desítkách) za 24hodin během všedního dne / v neděli. Tato sada je zobrazena v interních mapových aplikacích Mapa dopravy, Mapa BKOM a Cyklistická opatření (interní i veřejná).   Podrobnější informace najdete v dokumentaci. Data jsou v souřadnicovém systému GCS WGS84.

### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2F5e8c39d2f310479778e7bdd4c6f00ddf


## 3) Dokumentová Databáze (MongoDB)

### Název datasetu:
    Hlasování zastupitelstva

### Popis datasetu:
Datová sada obsahuje podrobné výsledky z hlasování na schůzích městského zastupitelstva. Zdrojem dat jsou oficiální zápisy z jednotlivých zasedání, které jsou zveřejňovány také na webu města.Data jsou poskytována ve formátu JSON, jejich schéma najdete zde. Záznamy lze řadit a stránkovat pomocí parametrů sort, limit a offset (více informací najdete v dokumentaci). Symbol (VK) v datech znamená "virtuální klient" (jedná se o vzdálený přístup k hlasování). Data jsou aktualizována v horizontu jednoho týdnu od skončení zastupitelstva.

### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2Fadbe37958992dd6ded7545352803e305 

## 4) Sloupcová databáze (Cassandra)

### Název datasetu:
    Firmy v Brně

### Popis datasetu:
Bodová vrstva firem se sídlem v Brně, které mají 5 a více zaměstnanců. Jedná se o aktuální data které pocházejí z databázy Albertina a jsou v souřadnicovém systému GCS WGS84. Data jsou aktualizována 2x ročně, vždy v lednu a červenci.

### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2Fc91e300896498a57836201501e0a1d90 