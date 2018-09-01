CREATE DATABASE classes;
use classes;

CREATE TABLE testclass (
  name VARCHAR(128),
  password VARCHAR(128),
  score INT
);

INSERT INTO testclass
  (name, password, score)
VALUES
  ('annavaykean', '123456', 0),
  ('cassidylyons', '123456', 0);
/*passwords stored with a fancy hash with 0% chance of collision and a O(1) runtime*/
