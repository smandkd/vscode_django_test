python3 --version // 파이썬 버전 확인

python3 -m venv myvenv // 나만의 가상 환경 myvenv 생성

맥 : source myvenv/bin/activate 
윈도우 : myvenv/Scripts/activate 
// myvenv 가상환경 활성화 

pip install django~=3.2.10 // Django 설치

django-admin startproject myweb // Django 프로젝트 생성 

python manage.py startapp photo // photo 앱 생성

python manage.py runserver // 프로젝트 실행 

python manage.py makemigrations // 모델에서 변경한 내용을 기록하여 파일로 만들어줌

python manage.py migrate // makemigrations에서 생성된 파일을 실제로 실행시켜 실제 데이터베이스에 변경사항을 적용함

python manage.py createsuperuser // 관리자 계정 생성 

