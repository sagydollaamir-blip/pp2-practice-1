-- 1. UPSERT (insert или update)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- 2. BULK INSERT с проверкой
CREATE OR REPLACE PROCEDURE bulk_insert(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP

        -- Проверка телефона (только цифры и длина >= 10)
        IF phones[i] ~ '^[0-9]+$' AND length(phones[i]) >= 10 THEN

            IF EXISTS (SELECT 1 FROM contacts WHERE name = names[i]) THEN
                UPDATE contacts SET phone = phones[i] WHERE name = names[i];
            ELSE
                INSERT INTO contacts(name, phone)
                VALUES (names[i], phones[i]);
            END IF;

        ELSE
            RAISE NOTICE 'Invalid phone: % (%)', names[i], phones[i];
        END IF;

    END LOOP;
END;
$$;


-- 3. DELETE
CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;