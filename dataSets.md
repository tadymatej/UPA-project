# Návrh datasetů

## 1) Databáze časových řad (InfluxDB)

### Název datasetu: 
    Kvalita ovzduší
    
### Popis datasetu: 
Data o kvalitě ovzduší ze stanic na území města Brna. Nejedná se o verifikovaná data. Stanice jsou ve správě ČHMÚ, města Brna a Státního zdravotnického ústavu Ostrava.

### Dokumentace datasetu:
Souřadnicový systém: GCS WGS-84
#### Aktualizace:
SO2_1h (každou hodinu/updated hourly)
NO2_1h (každou hodinu/updated hourly)
CO_8h (každých 8h/each 8 hours)
PM10_1h (každou hodinu/updated hourly)
O3_1h (každou hodinu/updated hourly)
PM10_24h (24h průměr/daily average)
PM2_5_1h (každou hodinu/updated hourly)

#### Atributy:

| Atribut  | Typ |
| ------------- | ------------- |
| code  | string  |
| name  | string  |
| owner  | string  |
| lat | float(2)  |
| lon | float(2)  |
| actualized | Date  |
| so2_1h  | string  |
| no2_1h | string  |
| co_8h | string  |
| pm10_1h | float(2) |
| o3_1h | string |
| pm10_24h | float(2) |
| pm2_5_1h | string |

### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2F4907e5c199620d99a44c1ec388703cd5

### Vhodná distribuce datové sady:
CSV | JSON (Je to jedno, protože data jsou v obou formátech poměrně jednoduchá, bez zanořování struktur, záleží na potřebách dané aplikace)

### Proč právě tento typ databáze?
Tento dataset je výhodné ukládat v NoSQL databázi InfluxDB, jelikož se jedná o databázi časových řad. Již z popisu sloupců vidíme, že data se mění periodicky v poměrně krátkých intervalech. Současně víme, že datová sada obsahuje chronologickou posloupnost měření, což je typ dat, pro který InfluxDB byla navržena. Z datové sady jsme si všimli, že každé měření má svůj identifikátor (objectid) a každý měřič, který je identifikován atributem "code", generuje svoji časovou řadu měření. Pokud uvážíme typické operace nad těmito daty, dospějeme také k tomuto typu databáze. Například, pokud by nás zajímala maximální, průměrná a minimální naměřená hodnota so2 v určitém časovém intervalu a její zanesení do grafu, tento typ databáze velmi zjednoduší výsledný dotaz oproti ostatním typům databáze. Pokud bychom toto chtěli provádět u jakéhokoliv jiného typu databáze, museli bychom dotazy pro daný typ databáze psát ručně a následně průměrovat naměřené hodnoty v určitém časovém fragmentu, který by odpovídal nejmenšímu zobrazovatelnému časovému intervalu v grafu. Tento problém u databáze časových řad za nás řeší dotazovací konstrukce "GROUP BY time(12m)"

## 2) Grafová Databáze (Neo4J)

### Název datasetu:
    Intenzita dopravy - Intenzita cyklistů

### Popis datasetu:
Pentlogramy intenzity dopravy zpracovávají pravidelně Brněnské komunikace, a.s. (dále zkráceně BKOM). Výstupy pentlogramů jsou schémata uzlů a úseků mezi nimi. Tato data jsou od roku 2016 zpracována do gisové podoby (SHP) nad uličním grafem a jsou s vydáním nového pentlogramu doplněna. Pentlogramy sledují intenzitu motorových vozidel a cyklistů.   Intenzita cyklistů je zpracovávána jednou za 2 roky (zpracované 2016, 2018, 2020). Intenzity jsou vizualizovány šířkou jednotlivých úseků a popisem číselné hodnoty, která definuje počet cyklistů (v desítkách) za 24hodin během všedního dne / v neděli. Tato sada je zobrazena v interních mapových aplikacích Mapa dopravy, Mapa BKOM a Cyklistická opatření (interní i veřejná).   Podrobnější informace najdete v dokumentaci. Data jsou v souřadnicovém systému GCS WGS84.

### Dokumentace datasetu:

#### Atributy:
| Atribut  | Typ | Popis |
| ------------- | ------------- | ------------- |
| ID  | Jednoznačný identifikátor záznamu  | long int |
| prac_clk  | Počet cyklistů ve všední den (r. 2016)  | long int | 
| vik_clk |  Počet cyklistů o víkendu (r. 2016) | long int | 
| prac_clk |  Počet cyklistů ve všední den (r. 2018) | long int | 
| vik_clk |  Počet cyklistů o víkendu (r. 2018) | long int | 
| prac_clk |  Počet cyklistů ve všední den (r. 2020) | long int | 
| vik_clk | Počet cyklistů o víkendu (r. 2020)  | long int | 
| datum_exportu |  Datum exportu záznamů | Date | 


### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2F5e8c39d2f310479778e7bdd4c6f00ddf

### Vhodná distribuce datové sady:
CSV | GeoJSON (Je to jedno, protože data jsou v obou formátech poměrně jednoduchá, bez zanořování struktur, záleží na potřebách dané aplikace)

### Proč právě tento typ databáze?

## 3) Dokumentová Databáze (MongoDB)

### Název datasetu:
    Hlasování zastupitelstva

### Popis datasetu:
Datová sada obsahuje podrobné výsledky z hlasování na schůzích městského zastupitelstva. Zdrojem dat jsou oficiální zápisy z jednotlivých zasedání, které jsou zveřejňovány také na webu města.Data jsou poskytována ve formátu JSON, jejich schéma najdete zde. Záznamy lze řadit a stránkovat pomocí parametrů sort, limit a offset (více informací najdete v dokumentaci). Symbol (VK) v datech znamená "virtuální klient" (jedná se o vzdálený přístup k hlasování). Data jsou aktualizována v horizontu jednoho týdnu od skončení zastupitelstva.

### Dokumentace datasetu:
Viz json schema v souboru: schema-documentDB.json

### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2Fadbe37958992dd6ded7545352803e305 

### Vhodná distribuce datové sady:
JSON (Nutně JSON, protože v CSV to nelze stáhnout a navíc v CSV by se ani nedaly nijak efektivně zobrazit vztahy mezi objekty v dokumentu (Například kdo hlasoval pro koho do zastupitelstva), mohlo by docházet ke ztrátám informací z důvodu nedostatku metadat pro popis dat)

### Proč právě tento typ databáze?

## 4) Sloupcová databáze (Cassandra)

### Název datasetu:
    Firmy v Brně

### Popis datasetu:
Bodová vrstva firem se sídlem v Brně, které mají 5 a více zaměstnanců. Jedná se o aktuální data které pocházejí z databázy Albertina a jsou v souřadnicovém systému GCS WGS84. Data jsou aktualizována 2x ročně, vždy v lednu a červenci.

### Dokumentace datasetu:

#### Atributy:
| Atribut  | Typ |
| ------------- | ------------- |
| name  | string  |
| adresa | string  |
| foundation_year  | long int  |
| employees | string  |
| turnover_in_czk | string  |
| website | string  |
| odvetvi  | string  |
| industry | string  |
| address | string  |
| city | string |
| latitude | float(2) |
| longitude | float(2) |

### Odkaz na dataset: 
https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F44992785%2Fc91e300896498a57836201501e0a1d90 

### Vhodná distribuce datové sady:
CSV (Jelikož tato data se hodí pro sloupcovou NoSQL databázi, i formát souboru, ve kterém se tato data přenáší se hodí přenášet v CSV, neboť CSV si lze představit jako tabulku obsahující M řádků a N sloupců, v tomto případě N = počet atributů a M je počet záznamů)

### Proč právě tento typ databáze?