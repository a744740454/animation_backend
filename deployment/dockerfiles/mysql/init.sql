create database `animation`;
SET character_set_client = utf8;
CREATE USER animation_user IDENTIFIED BY 'sadnesspineapple';
-- 给用户分配所有的权限，并且通过localhost访问
GRANT ALL ON animation.* to animation_user@'%' IDENTIFIED BY 'sadnesspineapple';


