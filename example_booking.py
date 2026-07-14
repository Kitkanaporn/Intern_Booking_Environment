import sqlite3

API_KEY = "sk-live-1234567890abcdef"  # 🔴 hardcoded secret

def get_booking_by_room(room_name):
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()
    # 🔴 SQL injection: ต่อ string เข้า query ตรง ๆ
    query = "SELECT * FROM bookings WHERE room = '" + room_name + "'"
    cursor.execute(query)
    return cursor.fetchall()

def cancel_booking(booking_id, user):
    # 🔴 ไม่มีการตรวจ auth ว่า user มีสิทธิ์ยกเลิก booking นี้จริงไหม
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
    conn.commit()
    print(f"user {user} cancelled booking, api_key={API_KEY}")  # 🔴 log secret

def create_booking(room, start_time, end_time, user):
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bookings (room, start_time, end_time, user) VALUES (?, ?, ?, ?)",
        (room, start_time, end_time, user)
    )
    conn.commit()  # 🟡 ไม่มี try/except ถ้า insert fail (เช่น room ชนกัน)
    return cursor.lastrowid
