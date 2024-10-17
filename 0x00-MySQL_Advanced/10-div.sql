-- SQL script that creates a function SafeDiv
-- This function divides the first number by the second
-- or returns 0 if the second number is 0.

DELIMITER //

CREATE FUNCTION SafeDiv(
  a INT,
  b INT
) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- Check if b is 0 to avoid division by zero
    RETURN IF(b = 0, 0, a / b);
END
//

DELIMITER ;

