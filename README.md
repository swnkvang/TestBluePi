# เกมส์จับคู่ไพ่
เกมส์จับคู่ไพ่ คือเกมส์ที่พัฒนาขึ้นด้วยภาษา Python 3.7  เป็นเกมส์เกี่ยวกับเกมส์จับคู่ไพ่ โดยจะมีไพ่ทั้งหมด 12 ใบ หน้าไพ่จะเป็นหมายเลข 1- 6 หมายเลขละ 2 ใบ ผู้เล่นจะต้องทำการจับคู่ไพ่โดยการคลิกเพื่อเปิดไพ่ออก ทุกครั้งที่มีการเปิดหน้าไพ่จะนับเป็น 1 คลิก ยิ่งจำนวนคลิกน้อยคือผลคะเเนนดี เมื่อผู้เล่นจับคู่ไพ่ได้ให้เปิดค้างไว้ หากเปิดมาไม่ใช่คู่ให้ทำการคว่ำหน้าไพ่ลงทั้งสองใบ เล่นจบกว่าจะเปิดไพ่ได้ครบทั้ง 12 ใบ และผู้เล่นสามารถเริ่มเกมส์ใหม่ได้เมื่อต้องการ

## เริ่มต้นการใช้งาน
<ul>
  <li>Install Python 3.7</li>
  <li>Install MaridDB</li>
  <li>Install Mongodb</li>
</ul>

## ข้อกำหนดเบื้องต้น
- ### Programming Language
    - Python 3.7
- ### database
    - MariaDB
        - database name  :  gamematching
        - table
            - tb_player_account
            - tb_token_player
    - MongoDB
        - database name : game_math
        - collection
            - transaction_game
- ### Constructor 
    - MariaDB
        - สร้าง database โดยใช้ชื่อ : gamematching
        - สร้าง table 
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
        - สร้าง database โดยใช้ชื่อ game_match
        - สร้าง collection โดยใช้ชื่อ : transaction_game

