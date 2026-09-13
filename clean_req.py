import re
with open('requirements.txt', 'r') as f:
    content = f.read()
# ลบ --hash และเครื่องหมาย \ ที่ค้างอยู่ออกให้หมด
clean_content = re.sub(r'\\?\s*--hash=[^\s]+', '', content)
with open('requirements.in', 'w') as f:
    f.write(clean_content)
