# Gelir-Gider-Takip
Tüm ayların gelir gider takibinin kolay bir şekilde yapılabileceği Python otomasyonu.
<hr>

## Veri Tabanı Şeması
```sql
CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    description TEXT
);

CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    description TEXT,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
```