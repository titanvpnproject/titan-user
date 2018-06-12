해피용 django 프로젝트 프레임
=============

개발환경
-------------

- mysql 5.7
- django 2.0.5
- djangomako 1.1.1
- djangorestframework 3.8.2
- django-rest-swagger 2.2.0

개발환경 구축 방법
-------------

- <code>mkdir workspace</code>    
- <code>cd workspace</code>    
- <code>git clone https://github.com/h4ppyy/main</code>    
- <code>cd main</code>    
- <code>docker-compose up</code>  
  
##### 아래 문구 출력 시 종료 후 다시 docker-compose up  
##### django_db | Version: '5.7.22'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)    
  
- <code>docker-compose up</code>    
  
##### 성공 시 아래의 문구가 출력됨  
##### django_web | Quit the server with CONTROL-C.    
  
접속 방법
-------------
- django  
127.0.0.1:8005/sample  
- mysql  
127.0.0.1:3315  

꿀팁
-------------
##### docker background 실행  
- <code>docker-compose up -d</code>  
##### docker background 실행 후 log 보기  
- <code>docker-compose logs</code>  

브랜치 정보
-------------
##### version1
- 기본 프레임

##### version2
- 디렉토리 모듈화
