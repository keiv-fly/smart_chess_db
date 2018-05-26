DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE pos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fen TEXT UNIQUE NOT NULL
);

CREATE TABLE move_t (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pos_id INTEGER NOT NULL,
  move_s TEXT NOT NULL,
  next_pos_id INTEGER NOT NULL,
  FOREIGN KEY (pos_id) REFERENCES pos (id),
  FOREIGN KEY (next_pos_id) REFERENCES pos (id)
);
CREATE TABLE eval (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pos_id INTEGER NOT NULL,
  score REAL NOT NULL,
  moves TEXT,
  depth integer,
  engine TEXT NOT NULL,
  date_recorded integer,
  FOREIGN KEY (pos_id) REFERENCES pos (id)
);

INSERT INTO pos (fen)
VALUES ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -");

INSERT INTO eval (pos_id, score, moves, depth, engine, date_recorded)
VALUES (1, 0.18, "1. d4 d5 2. c4", 52, "Komodo 11.01 64-bit",strftime("%s", "now"));