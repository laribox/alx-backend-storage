-- Creates a stored procedure AddBonus
-- that adds a new correction for a student.

DELIMITER //

CREATE PROCEDURE AddBonus(
  IN user_id INT,
  IN project_name varchar(255),
  IN score INT
)
BEGIN
   INSERT INTO projects (name)
    SELECT project_name 
    WHERE project_name NOT IN (SELECT name FROM projects);

    INSERT INTO corrections (user_id, project_id, score)
    VALUES(user_id, (SELECT id from projects WHERE name=project_name), score);

END
//

DELIMITER ;
