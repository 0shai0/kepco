
-- 1. 자주 검색된 태그 상위 2개 확인 -> (해운대, 서면)


SELECT T.TAG_NAME
FROM tag_tb T
ORDER BY HIT_CNT DESC
LIMIT 2;


-- 2. 가장 많이 검색된 태그를 사용하는 매장 개수 확인 -> 44


SELECT COUNT(*)
FROM tag_tb T JOIN shop_tag_tb ST ON T.TAG_ID=ST.TAG_ID
GROUP BY T.TAG_ID
ORDER BY HIT_CNT DESC
LIMIT 1;


SELECT COUNT(*)
FROM tag_tb T JOIN shop_tag_tb ST
WHERE T.TAG_ID=ST.TAG_ID
AND T.TAG_ID= (SELECT TAG_ID FROM tag_tb ORDER BY HIT_CNT DESC LIMIT 1);


-- 3. '거북선횟집' 매장에 연결된 모든 태그명 확인 -> 부산, 해운대구, 해운대, 마포, 거북선횟집, 횟집, 모둠회, 바다보이는 집, 단체, 모임, 한식


SELECT T.TAG_NAME
FROM tag_tb T JOIN shop_tag_tb STT ON T.TAG_ID=STT.TAG_ID JOIN shop_tb ST ON STT.SHOP_ID=ST.SHOP_ID
WHERE ST.SHOP_NAME = '거북선횟집';


-- 4. '한구름' 사용자가 즐겨찾기로 등록된 매장명과 매장의 설명 확인 -> 디딤돌 싱싱한 굴과 고소한 보쌈 전문점 / 해림 꽃새우 회 전문점

SELECT ST.SHOP_NAME, ST.SHOP_DESC
FROM user_tb U JOIN favorite_tb FT ON U.USER_ID=FT.USER_ID JOIN shop_tb ST ON FT.SHOP_ID=ST.SHOP_ID
WHERE U.USER_NAME = '한구름';


-- 5. 아이디가 64인 매장을 즐겨찾기로 등록된 사용자의 이름과 이메일 주소 확인 -> 김명 windo@gmail.com / 양말 liox2xoil@nate.com


SELECT U.USER_NAME, U.EMAIL
FROM user_tb U
JOIN favorite_tb FT ON U.USER_ID = FT.USER_ID
WHERE FT.SHOP_ID = 64;





