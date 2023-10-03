Cílem této části projektu je analyzovat požadavky a navrhnout optimální způsob uložení rozsáhlých dat do vhodné NoSQL databáze tak, aby tato data bylo možno rychle dotazovat a aktualizovat.

Řešení této části se skládá několika kroků:

Na základě přednášek a cvičení z předmětu prostudujte vlastnosti a možnosti použití NoSQL databází různých druhů, konkrétně
sloupcová wide-column databáze (např. Apache Cassandra)
dokumentová databáze (např. MongoDB)
grafová databáze (např. Neo4J)
databáze časových řad (např. InfluxDB)
Prostudujte dostupné datové sady Národním katalogu otevřených data pro statutární město Brno, zejména se soustřeďte na dílčí datové sady z daného zdroje, jejich strukturu (schéma), typy datových položek, identifikátory, možnosti propojení datových sad (společné entity) či napojení na externí data (jiné zdroje, entity reálného světa), změnu dat v čase (aktualizace), a jiné.
Pro každý z výše uvedených druhů NoSQL databází mezi výše odkazovanými datovými sadami najděte datovou sadu, kterou bude vhodné uložit a dotazovat v daném druhu NoSQL databáze (a ne v jiném). Celkem použijete tedy nejméně 4 různé datové sady pro 4 různé typy NoSQL databází. Konkrétně, pro každý jednotlivý případe, popište
plný název zvolené datové sady vč. odkazu URL ve výše uvedeném katalogu
vhodnou distribuci dané datové sady (např. CSV či GeoJSON) dle nabídky v katalogu
zvolený druh NoSQL databáze a konkrétní databázový produkt/server (např. Apache Cassandra)
podrobné a logické vysvětlení, proč je nejlepší k uložení a dotazování zvolené datové sady použít právě daný druh NoSQL databáze (oproti jiným druhům NoSQL databází) - vysvětlení musí být konkrétní pro danou datovou sadu a databázi a odkazovat se na konkrétní jejich charakteristické vlastnosti, např. sloupce (struktura/schéma, datové typy, velikosti domény, atp.), řádky (počet, velikost, různorodost, existence identifikátorů a referencí, atp.), způsob a průběh vzniku dat a jejich uložení (zdroj, frekvence a perioda aktualizace, důvěryhodnost/chybovost dat, možnost zpětné změny již publikovaných dat či jen přidávání nových, možnosti komprese a agregace, retence/zapomínání dat, distribuce a škálovatelnost úložiště, redundance, atp.), způsob a průběh spotřeby dat (předdefinované a ad-hoc dotazy, frekvence a perioda čtení výsledků, distribuce a škálovatelnost zpracování dat pro dotazy, pozice konzumentů výsledků vzhledem k místu uložení a zpracování dat, možnosti urychlení dotazů pomocí cache/před-počítání, možnosti indexace, atp.)
syntakticky i sémanticky korektní příkazy pro definici úložiště v daném produktu/serveru NoSQL databáze pro danou datovou sadu (zápis definice schéma v CQL, příklad vložení dokumentu v JavaScript, import uzlů a hran v Cypher, atp., dle zvoleného databázového serveru)
algoritmický popis importu dat ze zvolené distribuce dané datové sady do připravené databáze a to jak počáteční naplnění prázdné databáze daty, tak pozdější doplnění nových či změněných dat (soustřeďte se na zvolení a použití vhodného klíče záznamů v NoSQL tak, aby bylo podle něj možné provést UPSERT, namísto INSERTu duplicitního záznamu; smazání všech dat v databázi a jejich opětovné vložení není přípustné) - můžete odevzdat krátký skript (např. v jazyce Python) nebo uvedené popsat pseudokódem či popisem kroků zvoleného algoritmu
alespoň jeden syntakticky i sémanticky korektní dotaz v jazyce daného databázového produktu nad v databázi uloženými daty dané datové sady, který bude demonstrovat vhodnost zvoleného druhu NoSQL databáze pro daná data vč. popisu způsobu, jakým databázový server dotaz zodpoví (jak nalezne uzly, kde jsou uložena požadovaná data; jak data z uzlů získá a dále distribuovaným způsobem zpracuje; jak výsledky doručí klientovi, který zadal dotaz, a jak je tento zkonzumuje)
Zkontrolujte a v týmu diskutujte vhodnost zvolené datové sady, správnost odůvodnění zvoleného druhu NoSQL databáze, použitelnost a náročnost popsaného způsobu načítání dat do databáze a provádění dotazů v databázi a korektnost všech příkazů či dotazů (zde je nezbytné si příkazy a dotazy nad datovými sadami a databázovými produkty prakticky vyzkoušet, a tím ověřit jejich korektnost).
Požadované výsledky sepište strukturovanou formou do dokumentu, případně doplňte skripty či ukázkami v souborech z dokumentu odkazovaných, zabalte do ZIP archivu a odevzdejte do IS VUT.
V rámci projektu se pouze odevzdávají výsledky bez jejich obhajoby. Proto je nutné odevzdat také odpovídající dokumentaci tak, aby se podle ní dalo posoudit splnění zadání.

Odevzdaný výsledek bude ohodnocen vyučujícím a za správné řešení můžete získat výše uvedený počet bodů.

vážnější chyby a nedostatky a neúplnost budou penalizovány snížením počtu bodů
vyšší hodnocení bude udělováno v případě nadprůměrných projektů, které se budou vyznačovat nadprůměrnou kvalitou provedení výše uvedeného rozsahu, vytvořením dalších (explicitně nepožadovaných) výsledků, nápaditým použitím vhodných vlastností zvolených databází, kvalitní dokumentací apod.; takový projekt může získat nejen maximální hodnocení, ale i prémiové body navíc
je silně doporučeno udělat před odevzdáním v rámci týmu interní oponenturu, kde se všichni členové týmu snaží nalézt v řešení případné nedostatky a tyto později opravit
pokud dojde v průběhu řešení projektu k odpadnutí některých členů týmu (např. z důvodu zrušení zápisu předmětu či odstoupení od řešení), je potřeba to v týmu řešit co nejdříve nebo, pokud je problém, nahlásit situaci vyučujícímu; případní odpadlíci, nahlaste kolegům svou absenci co nejdříve, ať mají možnost projekt úspěšně dokončit
při hodnocení se bude přihlížet k velikosti řešitelského týmu
