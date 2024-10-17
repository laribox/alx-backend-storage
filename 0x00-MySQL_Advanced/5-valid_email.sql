-- Creates a trigger that resets the attribute valid_email
-- only when the email has been changed.

DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is changed
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;

//

DELIMITER ;
