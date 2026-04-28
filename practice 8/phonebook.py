from connect import connect

# Поиск
def search(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


# UPSERT
def upsert(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    conn.close()


# BULK INSERT
def bulk_insert():
    conn = connect()
    cur = conn.cursor()

    names = ["Ali", "Bob", "John"]
    phones = ["87771234567", "invalid", "87001234567"]

    cur.execute("CALL bulk_insert(%s, %s)", (names, phones))

    conn.commit()
    conn.close()


# Пагинация
def pagination(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


# DELETE
def delete(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    upsert("Ali", "87771234567")
    search("Ali")
    bulk_insert()
    pagination(5, 0)
    delete("Ali")