# استفاده از تصویر پایه پایتون
FROM python:3.8-slim

# تعیین دایرکتوری کاری
WORKDIR /app

# کپی محتوا به داخل کانتینر
COPY . /app

# نصب نیازمندی‌ها
RUN pip install flask

# باز کردن پورت 8080
EXPOSE 8080

# اجرای برنامه
CMD ["python", "app.py"]
