-- SQL script that creates a table users following these requirements:

-- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- If the table already exists, your script should not fail
-- Your script can be executed on any database

CREATE IF NOT EXISTS TABLE users (
  id int NOT NULL AUTO_INCREMENT,
  email varchar(255) NOT NULL UNIQUE,
  name varchar(255),
  PRIMARY KEY (id)
)
