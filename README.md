# 🐳 Basic Docker for Students

คู่มือการเรียนรู้ Docker สำหรับนักศึกษาและผู้เริ่มต้น พร้อมตัวอย่าง Flask API แบบ step-by-step

## 📚 Table of Contents
- [Docker คืออะไร?](#docker-คืออะไร)
- [สิ่งที่ต้องติดตั้ง](#สิ่งที่ต้องติดตั้ง)
- [โครงสร้างโปรเจค](#โครงสร้างโปรเจค)
- [วิธีใช้งาน](#วิธีใช้งาน)
- [คำสั่ง Docker พื้นฐาน](#คำสั่ง-docker-พื้นฐาน)
- [API Endpoints](#api-endpoints)
- [แบบฝึกหัด](#แบบฝึกหัด)

## 🤔 Docker คืออะไร?

Docker เป็นเทคโนโลยี containerization ที่ช่วยให้เราสามารถ:
- 📦 **Package** แอปพลิเคชันพร้อม dependencies ทั้งหมด
- 🚀 **Deploy** ได้ง่ายบนเครื่องไหนก็ได้
- 🔄 **Consistent** ทำงานเหมือนกันทุกที่ (Development, Testing, Production)

### Container vs Virtual Machine
- **Container**: เบากว่า, เริ่มเร็วกว่า, ใช้ resource น้อยกว่า
- **VM**: แยก OS สมบูรณ์, ใช้ resource มาก

## 💻 สิ่งที่ต้องติดตั้ง

1. **Docker Desktop** - [Download](https://www.docker.com/products/docker-desktop)
2. **Python 3.7+** (สำหรับ development)
3. **Git** (optional)

### ตรวจสอบการติดตั้ง
```bash
docker --version
docker-compose --version
python --version
```

## 📁 โครงสร้างโปรเจค

```
basicdockerforstudent/
│
├── app/
│   └── app.py              # Flask API application
│
├── Dockerfile              # คำสั่งสร้าง Docker image
├── docker-compose.yml      # Configuration สำหรับ multi-container
├── requirements.txt        # Python dependencies
└── README.md              # เอกสารนี้
```

## 🚀 วิธีใช้งาน

### Method 1: ใช้ Docker Compose (แนะนำ!)

1. **Clone repository**
```bash
git clone https://github.com/Tanatpon-d/basicdockerforstudent.git
cd basicdockerforstudent
```

2. **รัน Docker Compose**
```bash
docker-compose up --build
```

3. **เข้าถึง API**
```
http://localhost:5000
```

4. **หยุดการทำงาน**
```bash
# กด Ctrl+C หรือ
docker-compose down
```

### Method 2: ใช้ Docker Commands

1. **Build Docker Image**
```bash
docker build -t flask-api .
```

2. **Run Container**
```bash
docker run -p 5000:5000 flask-api
```

## 🐋 คำสั่ง Docker พื้นฐาน

### Image Commands
```bash
# ดู images ทั้งหมด
docker images

# ลบ image
docker rmi <image-id>

# Pull image จาก Docker Hub
docker pull python:3.7
```

### Container Commands
```bash
# ดู containers ที่กำลังรัน
docker ps

# ดู containers ทั้งหมด
docker ps -a

# หยุด container
docker stop <container-id>

# ลบ container
docker rm <container-id>

# ดู logs
docker logs <container-id>

# เข้าไปใน container
docker exec -it <container-id> bash
```

### Docker Compose Commands
```bash
# Build และ start services
docker-compose up --build

# Start services (background)
docker-compose up -d

# Stop services
docker-compose down

# ดู logs
docker-compose logs

# Rebuild specific service
docker-compose build <service-name>
```

## 🔌 API Endpoints

### 1. Health Check
```bash
GET /
Response: "formalinapp_api works !"
```

### 2. Hello World
```bash
GET /hello
Response: "We love . ....."
```

### 3. Calculate Circle Area
```bash
# คำนวณพื้นที่วงกลม
POST /radius
Content-Type: application/json
Body: {"radius": 5}
Response: {"Message": "Radius already add into database", "area": [78.57]}

# ดูประวัติการคำนวณ
GET /radius
Response: {"radius": [78.57, 113.14, ...]}
```

### 4. Book Management (CRUD)
```bash
# เพิ่มหนังสือ
POST /book
Content-Type: application/json
Body: {"id": 1, "title": "Docker Guide", "author": "John Doe"}

# ดูหนังสือทั้งหมด
GET /book

# อัพเดทหนังสือ
PUT /book
Body: {"id": 1, "title": "New Title", "author": "Jane Doe"}

# ลบหนังสือ
DELETE /book
Body: {"index": 0}
```

## 🧪 ทดสอบ API

### ใช้ curl
```bash
# Test health check
curl http://localhost:5000/

# Test radius calculation
curl -X POST http://localhost:5000/radius \
  -H "Content-Type: application/json" \
  -d '{"radius": 10}'

# Add book
curl -X POST http://localhost:5000/book \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Learn Docker", "author": "Student"}'
```

### ใช้ Python
```python
import requests

# Calculate radius
response = requests.post('http://localhost:5000/radius', 
                         json={'radius': 7})
print(response.json())

# Get all books
response = requests.get('http://localhost:5000/book')
print(response.json())
```

## 📝 แบบฝึกหัด

### Exercise 1: เพิ่ม Endpoint ใหม่
เพิ่ม endpoint `/triangle` ที่คำนวณพื้นที่สามเหลี่ยม

<details>
<summary>💡 Hint</summary>

```python
@app.route('/triangle', methods=['POST'])
def triangle_area():
    body = request.get_json()
    base = body['base']
    height = body['height']
    area = 0.5 * base * height
    return {'area': area}, 200
```
</details>

### Exercise 2: เพิ่ม Database
ใช้ SQLite แทน in-memory list

<details>
<summary>💡 Hint</summary>

1. เพิ่ม `sqlite3` ใน requirements.txt
2. สร้าง database connection
3. แก้ไข endpoints ให้ใช้ database
</details>

### Exercise 3: Multi-Container Setup
เพิ่ม MongoDB container ใน docker-compose.yml

<details>
<summary>💡 Hint</summary>

```yaml
services:
  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
```
</details>

## 🔧 Troubleshooting

### Port ถูกใช้งานแล้ว
```bash
# หา process ที่ใช้ port 5000
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# เปลี่ยน port ใน docker-compose.yml
ports:
  - "5001:5000"  # เปลี่ยนเป็น 5001
```

### Container ไม่ restart
```bash
# ดู logs
docker-compose logs flask-api

# Rebuild image ใหม่
docker-compose build --no-cache
```

### Permission denied
```bash
# Linux/Mac
sudo docker-compose up

# หรือเพิ่ม user เข้า docker group
sudo usermod -aG docker $USER
```

## 📚 เรียนรู้เพิ่มเติม

- [Docker Official Documentation](https://docs.docker.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Best Practices for Dockerfile](https://docs.docker.com/develop/dev-best-practices/)

## 🤝 Contributing

1. Fork repository
2. สร้าง feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

**Tanatpon D**
- GitHub: [@Tanatpon-d](https://github.com/Tanatpon-d)

---

⭐ ถ้าชอบโปรเจคนี้ อย่าลืมกด Star ให้ด้วยนะครับ!