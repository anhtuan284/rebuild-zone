<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/static/v1?style=for-the-badge&message=Budibase&color=000000&logo=Budibase&logoColor=FFFFFF&label="></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white"></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/TensorFlow-FF3F06?style=for-the-badge&logo=tensorflow&logoColor=white"></a>
<a href="https://redis.io/"><img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" alt="redis" > </a>
<a href="https://www.docker.com/"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="docker" > </a>

# SafeZone

SafeZone được xây dụng với mục tiêu là phát triển một hệ thống cứu trợ khẩn cấp, hỗ trợ nhân đạo trong những thời điểm thiên tai (lũ lụt, sạt lở,..) và đại dịch. Đặc biệt là tại Việt Nam sau khi trải qua đại dịch COVID và bão YAGI.

Dự án được thực hiện trong cuộc thi [Phần Mềm Nguồn Mở-Olympic Tin học Sinh viên Việt Nam 2024](https://www.olp.vn/procon-pmmn/ph%E1%BA%A7n-m%E1%BB%81m-ngu%E1%BB%93n-m%E1%BB%9F). Được được open source theo giấy phép [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) bởi đội tác giả *Lazy Sunday Morning (LSM)*.

Để biết thêm chi tiết về cuộc thi, bạn có thể xem tại [vfossa.vn](https://vfossa.vn/tin-tuc/cong-bo-de-thi-noi-dung-phan-mem-nguon-mo-olympic-tin-hoc-sinh-vien-viet-nam-2024-727.html).

Link thuyết trình Canva tại cuộc thi [link]()

## Mục lục

1. [Giới Thiệu](#Giới-Thiệu)
2. [Chức Năng](#chức-năng-chính)
3. [Tổng Quan Hệ Thống](#kiến-trúc-hệ-thống)
4. [Cấu Trúc Thư Mục](#cấu-trúc-thư-mục)
5. [Hướng Dẫn Cài Đặt](#hướng-dẫn-cài-đặt)
   - [Yêu Cầu - Prerequisites](#yêu-cầu)
   - [Cài Đặt](#cài-đặt)
6. [CI/CD](#ci/cd)
7. [Đóng Góp](#đóng-góp-cho-dự-án)
8. [Bản Quyền](#bản-quyền)

## Giới Thiệu

## Chức Năng Chính

## Kiến trúc hệ thống

## Cấu trúc thư mục

## Hướng dẫn cài đặt

### Yêu cầu

### Cài đặt

### Bước 1: Cài đặt Docker

1. **Cài đặt Docker**:
   - Truy cập vào trang chính thức của Docker để tải và cài đặt Docker: [Docker Get Started](https://docs.docker.com/get-docker/).
   - Sau khi cài đặt, xác nhận Docker đã được cài đặt thành công bằng cách mở terminal và chạy lệnh:
     ```bash
     docker --version
     ```
   - Bạn cũng có thể kiểm tra trạng thái Docker daemon với:
     ```bash
     docker info
     ```

2. **Cài đặt Docker Compose (Tùy chọn)**:
   - Nếu bạn muốn sử dụng Docker Compose (để chạy Budibase cùng với MongoDB, ví dụ), bạn có thể tải Docker Compose từ [Docker Compose Documentation](https://docs.docker.com/compose/install/).
   - Sau khi cài đặt Docker Compose, kiểm tra lại phiên bản:
     ```bash
     docker-compose --version
     ```

### Bước 2: Chạy Budibase trong Docker
Lệnh này sẽ khởi động cả Budibase và MongoDB trong hai container riêng biệt. Bạn có thể truy cập Budibase qua http://localhost:10000.

```bash
docker-compose up -d
```
### Bước 3: Tạo tài khoản đăng nhập
![image](docs/images/images1.png)
### Bước 4: Tạo app mặc định
![image](docs/images/images2.png)
### Bước 5: Thêm app mà bạn đã tải về
![image](docs/images/images3.png)
Sau khi import xong thì vào tab ẩn danh và điền url http://localhost:10000/builder/portal/{ten-app} để trải nghiệm 
## Tích hợp và triển khai liên tục


## Đóng góp cho dự án

## 

<a href="https://github.com/anhtuan284/rebuild-zone/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=Bug+Report%3A+">Bug Report ⚠️
</a>

<a href="https://github.com/anhtuan284/rebuild-zone/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=RequestFeature:">Request Feature 👩‍💻</a>

Nếu bạn muốn đóng góp cho dự án, hãy đọc [CONTRIBUTING.md](.github/CONTRIBUTING.md) để biết thêm chi tiết.

Mọi đóng góp của các bạn đều được trân trọng, đừng ngần ngại gửi pull request cho dự án.

## Liên hệ

- Trần An Tiến: 2151013099tien@ou.edu.vn
- Võ Quốc Huy: 2151013029huy@ou.edu.vn
- Trương Bùi Anh Tuấn: dev.atuan03@gmail.com

## Bản quyền

This project is licensed under the terms of the [APACHE-2.0](LICENSE) license.
