# เกณฑ์รีวิวโค้ดกลางของทีม

ไฟล์นี้เป็นเกณฑ์กลางที่ `/review` (Claude Code ในเครื่อง) ใช้ในการรีวิวโค้ดทุกครั้ง ก่อน merge เข้า `main`
ทีมสามารถปรับเพิ่ม/แก้ไขเกณฑ์ในไฟล์นี้ได้ตามความเหมาะสมของโปรเจกต์

## 🔴 Critical (ต้องแก้ก่อน merge)

- SQL ทุกจุดต้องเป็น parameterized query / prepared statement ห้าม concatenate string เข้า query ตรง ๆ
- ทุก endpoint หรือ route ที่เข้าถึงข้อมูลหรือ action ที่มีผลต่อระบบ ต้องมีการตรวจสอบ authentication/authorization
- ห้าม hardcode secret, API key, token, password ลงในโค้ด (ต้องอ่านจาก env var หรือ secret manager)
- ห้าม log ข้อมูล sensitive เช่น password, token, PII, เลขบัตร, ข้อมูลส่วนตัวของผู้ใช้

## 🟡 Warning (ควรแก้)

- จุดที่มีโอกาส fail ได้ (เช่น network call, file I/O, parsing) แต่ไม่มี error handling
- function/method ที่ยาวเกินประมาณ 50 บรรทัด ควรพิจารณาแยกย่อย
- ชื่อตัวแปร/ฟังก์ชัน/คลาส ที่ไม่สื่อความหมาย หรือทำให้เข้าใจผิด
- โค้ดที่ซ้ำซ้อนกันหลายจุด ซึ่งควร refactor ให้เป็นฟังก์ชันหรือ module ร่วม

## 🟢 Suggestion (แก้หรือไม่ก็ได้)

- แนวทางปรับปรุง readability เช่นจัดโครงสร้างโค้ดใหม่ให้อ่านง่ายขึ้น
- เพิ่ม comment ในจุดที่ logic ซับซ้อนหรือไม่ obvious
- แนะนำ pattern หรือแนวทางที่ดีกว่าที่ใช้อยู่ในปัจจุบัน (ไม่บังคับ)

---

หมายเหตุ: เกณฑ์นี้ใช้กับ diff ของโค้ดที่เปลี่ยนแปลงใน PR เท่านั้น ไม่ใช่การรีวิวทั้ง codebase
