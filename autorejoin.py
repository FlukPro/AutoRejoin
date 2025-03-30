import os
import time

def open_roblox():
    """เปิด Roblox และเข้าสู่ Blox Fruits."""
    os.system("adb shell am start -a android.intent.action.VIEW -d roblox://placeID=2753915549")
    print("เปิด Roblox และเข้าสู่ Blox Fruits")

def close_roblox():
    """ปิด Roblox."""
    os.system("adb shell am force-stop com.roblox.client")
    print("ปิด Roblox")

def is_roblox_running():
    """ตรวจสอบว่า Roblox กำลังทำงานอยู่หรือไม่."""
    result = os.popen("adb shell ps | grep com.roblox.client").read()
    return 'com.roblox.client' in result

def is_app_responsive():
    """ตรวจสอบว่า Roblox ยังคงตอบสนองหรือไม่."""
    result = os.popen("adb shell dumpsys activity | grep 'com.roblox.client'").read()
    return 'Not Responding' not in result

def monitor_game():
    """ตรวจสอบสถานะของเกมและเปิดใหม่ถ้าหากปิด หรือค้าง"""
    rejoin_interval = 600  # กำหนดให้รีจอยน์ทุก 10 นาที (600 วินาที)
    last_rejoin_time = time.time()  # บันทึกเวลาครั้งสุดท้ายที่รีจอยน์

    while True:
        # ตรวจสอบว่า Roblox ทำงานอยู่หรือไม่
        if not is_roblox_running():
            print("Roblox ไม่ทำงานอยู่ กำลังเปิดใหม่...")
            open_roblox()
        
        # ตรวจสอบว่าเกมค้างหรือไม่
        elif not is_app_responsive():
            print("เกมค้าง กำลังปิดและเปิดใหม่...")
            close_roblox()
            time.sleep(5)  # รอ 5 วินาทีเพื่อให้ระบบปิดเกมสมบูรณ์
            open_roblox()
        
        # ตรวจสอบว่าเวลาผ่านไป 10 นาทีแล้วหรือยัง
        current_time = time.time()
        if current_time - last_rejoin_time >= rejoin_interval:
            print("ครบ 10 นาที กำลังรีจอยน์เกม...")
            close_roblox()  # ปิดเกม
            time.sleep(5)  # รอ 5 วินาทีเพื่อให้ระบบปิดเกมสมบูรณ์
            open_roblox()  # เปิดเกมใหม่
            last_rejoin_time = current_time  # อัพเดทเวลาของการรีจอยน์ครั้งล่าสุด

        # รอ 60 วินาทีก่อนตรวจสอบสถานะอีกครั้ง
        time.sleep(60)

if __name__ == "__main__":
    monitor_game()
