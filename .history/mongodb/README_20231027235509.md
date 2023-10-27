# Vytvoření MongoDB Atlas Clusteru a Připojení Python Scriptů

## 1. Vytvoření účtu na MongoDB Atlas

- Navštivte webovou stránku [MongoDB Atlas](https://www.mongodb.com/atlas).
- Vytvořte si účet nebo se přihlaste, pokud již účet máte.

## 2. Vytvoření clusteru

- Po přihlášení klikněte na tlačítko „Build a Cluster“.
- Vyberte si typ clusteru, který chcete vytvořit. Pro základní použití můžete využít zdarma dostupnou variantu.
- Nakonfigurujte cluster podle vašich potřeb (region, velikost, atd.).
- Klikněte na „Create Cluster“ a počkejte, než bude cluster vytvořen.

## 3. Konfigurace přístupu

- V Atlas rozhraní jděte na sekci „Security“ a vytvořte uživatelský účet, který bude mít přístup k databázi. Zaznamenejte si uživatelské jméno a heslo.
- V sekci „Network Access“ nastavte IP adresy, ze kterých je povolen přístup k vašemu clusteru.

## 4. Získání připojovacího řetězce

- Jděte na přehled clusteru a klikněte na tlačítko „Connect“.
- Vyberte „Connect Your Application“.
- Zkopírujte připojovací řetězec, který vám bude poskytnut.

## 5. Instalace MongoDB Driver v Pythonu

Otevřete příkazovou řádku nebo terminál a nainstalujte MongoDB driver pro Python pomocí pip:

```python
pip install pymongo
```

## 6. Připojení Python scriptu k MongoDB Atlas

V souboru `mongo_db.py` a `mongo_db_query.py` nahraďte `uri` vaším připojovacím řetězcem.

# Spuštění skriptů

Spuštění skriptu `mongo_db.py`:

```bash
python3 mongo_db.py
```

Spuštění skriptu `mongo_db_query.py`:

```bash
python3 mongo_db.py
```
