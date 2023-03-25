BEGIN TRANSACTION;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    level INT NOT NULL,
    avatarImage VARCHAR
);

CREATE TABLE modules(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    level INTEGER NOT NULL 
);

CREATE TABLE enrolment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (userId)
        REFERENCES users (id),
    FOREIGN KEY (moduleCode)
        REFERENCES modules (code)
);

CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    allText VARCHAR,
    FOREIGN KEY (authorId)
        REFERENCES users (id)
);