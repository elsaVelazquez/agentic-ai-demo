CREATE TABLE researchers (
    researcher_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE grants (
    grant_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    principal_investigator_id INTEGER NOT NULL,
    sponsor TEXT NOT NULL,
    amount REAL NOT NULL,
    status TEXT NOT NULL,
    source_url TEXT,
    FOREIGN KEY (principal_investigator_id)
        REFERENCES researchers(researcher_id)
);