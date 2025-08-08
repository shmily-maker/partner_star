FROM python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 复制整个项目到容器（确保 manage.py 和 mysite 目录正确映射）
COPY . /app/
RUN mkdir -p /app/data && chmod 755 /app/data
RUN python manage.py collectstatic --noinput
EXPOSE 8010
#CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8010", "--workers", "4"]