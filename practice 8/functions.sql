-- 1. Поиск по шаблону
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- 2. Пагинация
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, offs INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM contacts
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;