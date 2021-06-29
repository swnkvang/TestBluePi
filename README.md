# เกมส์จับคู่ไพ่
เกมส์จับคู่ไพ่ คือเกมส์ที่พัฒนาขึ้นด้วยภาษา Python 3.7  เป็นเกมส์เกี่ยวกับเกมส์จับคู่ไพ่ โดยจะมีไพ่ทั้งหมด 12 ใบ หน้าไพ่จะเป็นหมายเลข 1- 6 หมายเลขละ 2 ใบ ผู้เล่นจะต้องทำการจับคู่ไพ่โดยการคลิกเพื่อเปิดไพ่ออก ทุกครั้งที่มีการเปิดหน้าไพ่จะนับเป็น 1 คลิก ยิ่งจำนวนคลิกน้อยคือผลคะเเนนดี เมื่อผู้เล่นจับคู่ไพ่ได้ให้เปิดค้างไว้ หากเปิดมาไม่ใช่คู่ให้ทำการคว่ำหน้าไพ่ลงทั้งสองใบ เล่นจบกว่าจะเปิดไพ่ได้ครบทั้ง 12 ใบ และผู้เล่นสามารถเริ่มเกมส์ใหม่ได้เมื่อต้องการ

## Table of Contents
* [เริ่มต้นการใช้งาน](##เริ่มต้นการใช้งาน)
* [ข้อกำหนดเบื้องต้น](##ข้อกำหนดเบื้องต้น)
* [API Document](##API--Document)
* [Description Project](##Description--Project)
* [Deployment](##Deployment)

## เริ่มต้นการใช้งาน
<ul>
  <li>Install Python 3.7</li>
  <li>Install MaridDB</li>
  <li>Install Mongodb</li>
</ul>

## ข้อกำหนดเบื้องต้น
- ### Programming Language
    - Python 3.7
- ### Database
    - MariaDB
        - database name  :  gamematching
        - table
            - tb_player_account
            - tb_token_player
    - MongoDB
        - database name : game_math
        - collection
            - transaction_game
- ### Constructor Database
    - MariaDB
        - สร้าง database โดยใช้ชื่อ : gamematching
        - สร้าง table โดยใช้คำสั่งด้านล่าง
			- tb_player_account
			```javascript
                CREATE TABLE `tb_player_account` (
                `id` varchar(36) NOT NULL DEFAULT uuid(),
                `username` varchar(100) DEFAULT NULL,
                `password` varchar(100) DEFAULT NULL,
                `time_create` datetime DEFAULT current_timestamp(),
                `secret_key` text DEFAULT NULL,
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8; );
			```
			- tb_token_player
            ```javascript
                CREATE TABLE `tb_token_player` (
                `id` varchar(36) NOT NULL DEFAULT uuid(),
                `token` text DEFAULT NULL,
                `time_expire` datetime DEFAULT NULL,
                `key_decode` text DEFAULT NULL,
                `time_create` datetime DEFAULT current_timestamp(),
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            ```
    - MongoDB
        - สร้าง database โดยใช้ชื่อ : game_match
        - สร้าง collection โดยใช้ชื่อ : transaction_game

- ## API Document
    - สามารถดูคำอธิบายเกี่ยวกับการใช้งาน API เบื้องต้นได้ที่ลิงค์ด้านล่าง
     ```javascript
        https://documenter.getpostman.com/view/12061603/Tzef9NQA
     ```
- ## Description Project
    - **main.py** เป็นไฟล์ที่ใช้ในการ Run Project โดยสามารถใช้คำสั่งด้านล่างในการทดสอบ Run localhost ได้
        ```javascript
            python main.py
        ```
    - **requirements.txt** เป็นไฟล์ที่เก็บข้อมูล library ต่าง ๆ ที่ใช้ใน Project โดยสามารถใช้คำสั่งด้านล่างเพื่อใช้ในการ install library สำหรับการทดสอบโดย Run localhost ได้ทั้งหมด
        ```javascript
            python -m pip install -r requirements.txt
        ```
    - **Folder**
        - **api** : เป็น Folder สำหรับเก็บ file api ทั้งหมด
            - **file**
                - **api_game.py** เป็น file api เกี่ยวกับการประมวลผลเกมส์
                    - /game/start ใช้เพื่อกดเริ่มเกมส์
                    - /game/run ใช้เพื่อประมวลผลเกมส์
                - **api_login.py** เป็น file api เกี่ยวกับการประมวลผลบัญชีของผู้เล่นในเกมส์
                    - /game/createplayer ใช้สำหรับการสร้างบัญผู้เล่น
                    - /game/login ใช้สำหรับ login
        - **config** : เป็น Folder สำหรับเก็บ file ที่เกี่ยวกับการ config ต่าง ๆ ทั้งหมด
            - **file**
                - **db_maria.py** เป็น file สำหรับ config MariaDB สามารถปรับการเชื่อมต่อกับฐานข้อมูลได้ที่ไฟล์นี้
                - **db_mongo.py** เป็น file สำหรับ config MongoDB สามารถปรับการเชื่อมต่อกับฐานข้อมูล MongoDB ได้ที่ไฟล์นี้
                - **env.py** เป็น file สำหรับกำหนด environment สามารถกำหนด type_product ว่าเป็น prd หรือ uat ได้จากไฟล์นี้ (โดยการกำหนด type_product จะมีผลต่อการเข้าเงื่อนไขการกำหนด port ในการรันของไฟล์ main.py)
                - **lib.py** เป็น file สำหรับการ import library ต่าง ๆ ที่ใช้ใน project
        - **function** : เป็น Folder สำหรับเก็บ file ที่แยกส่วนการทำงานออกมาเพื่อใช้คำนวณต่าง ๆ
            - **file**
                - **cal_authen.py** เป็น file สำหรับเก็บโค้ดในส่วนการประมวลผลบัญชีของผู้เล่นในเกมส์
                    - **AuthLogin** เป็นฟังก์ชันสำหรับประมวลผลการ login ของผู้เล่นว่า login สำเร็จหรือไม่
                    - **GenToken** เป็นฟังก์ชันสำหรับการ generate token ของผู้เล่นเพื่อนำไปใช้ในการ authen api อื่น ๆ
                - **cal_Game.py** เป็น file สำหรับเก็บโค้ดในส่วนการประมวลผลเกมส์ทั้งหมด
                    - **createGame** เป็นฟังก์ชันสำหรับสร้างเกมส์โดยจะประมวลผลสุ่มตัวเลข 1-6 เพื่อใช้ในการสร้าง Array เพื่อจำลองหน้าไพ่แบบ 4*3
                    - **cal_num** เป็นฟังก์ชันที่ช่วยในการนำตัวเลขที่สุ่มได้ไปใส่ใน Array (เหมือนการจำลองการนำตัวเลขที่สุ่มไปวางหน้าไพ่แบบ 4*3)
                    - **cal_GlobalBestScore** เป็นฟังก์ชันที่ใช้คำนวณหาคะเเนนของผู้เล่นที่ดีที่สุดจากผู้เล่นทั้งหมด (ยิ่งจำนวนการคลิกน้อยผลคะเเนนคือดี)
                    - **cal_BestScorePlayer** เป็นฟังก์ชันที่ใช้คำนวณหาคะเเนนของผู้เล่นที่ดีที่สุด (ยิ่งจำนวนการคลิกน้อยผลคะเเนนคือดี)
                    - **cal_StatusGame** เป็นฟังก์ชันสำหรับการคำนวณสถานะเกมส์ของผู้เล่นว่าจบเกมส์เเล้วหรือยัง ถ้าไพ่ถูกเปิดครบทุกใบเเล้วสถานะเกมส์จะเป็น Win, ถ้าไพ่ยังเปิดไม่ครบสถานะเกมส์จะเป็น Pending
                    - **calBoxGame** เป็นฟังก์ชันสำหรับการคำนวณสถานะการเปิด/ปิดของไพ่ในทุก ๆ การคลิกเปิดไพ่ของผู้เล่น
        - **method** : เป็น Folder ที่ใช้สำหรับเก็บ file ที่เป็นการทำงานหลักที่ถูกส่งต่อมาจาก api
            - **file**
                - **player_account.py** เป็น file การทำงานหลักเกี่ยวกับการประมวลผลบัญชีของผู้เล่นในเกมส์
                    - **create_account** เป็นการทำงานในส่วนของการสร้างบัญชีผู้เล่น
                    - **login** เป็นการทำงานในส่วนการประมวลผลการ login ของผู้เล่น
                    - **authen_account** เป็นการประมวลผล token ของ user ที่แนบมากับ API อื่น ๆ ว่า authen สำเร็จหรือไม่ เเละถอดรหัส token ได้มาเป็นข้อมูล username ของผู้เล่น 
                - rungame.py เป็น file การทำงานหลักในการประมวลผลเกมส์
                    - **new_game** เมื่อผู้เล่นกดเริ่มเกมส์ใหม่จะทำการสร้างเกมส์ใหม่ให้ผู้เล่น
                    - **play_game** เมื่อผู้เล่นคลิกเปิดไพ่จะมีการประมวลผลสถานะการเปิด/ปิดของไพ่

- ## Deployment
    - ใช
    
