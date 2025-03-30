# Roblox Game Monitor

โปรแกรมนี้ช่วยตรวจสอบสถานะของเกม **Blox Fruits** บน **Roblox** โดยสามารถเปิดเกมใหม่อัตโนมัติเมื่อเกมปิดหรือค้าง และจะรีจอยน์ทุก ๆ 10 นาทีเพื่อให้เกมทำงานอย่างต่อเนื่อง

## ฟีเจอร์หลัก
- ตรวจสอบว่า Roblox กำลังทำงานอยู่หรือไม่
- ตรวจสอบว่า Roblox ยังตอบสนองอยู่หรือไม่
- เปิด Roblox และเข้าสู่ **Blox Fruits** อัตโนมัติ
- ปิด Roblox และเปิดใหม่เมื่อเกมค้าง
- รีจอยน์เกมทุก 10 นาที (สามารถปรับเวลาตามต้องการ)

## ความต้องการ
- **Python 3.x**
- **ADB (Android Debug Bridge)**: ใช้สำหรับการควบคุมแอปพลิเคชันในโทรศัพท์ Android ผ่านคำสั่ง
- **Roblox app**: ต้องติดตั้ง Roblox บนอุปกรณ์ Android

## การติดตั้ง
1. ติดตั้ง **ADB**:
   - [ติดตั้ง ADB](https://developer.android.com/studio/command-line/adb)
2. เชื่อมต่อโทรศัพท์ Android กับคอมพิวเตอร์และเปิด **USB Debugging** ในการตั้งค่า Developer Options
3. ดาวน์โหลดโค้ดนี้:
   ```bash
   git clone https://github.com/your-repo/Roblox-Game-Monitor.git
   cd Roblox-Game-Monitor
