
1. SELECT
 1) 모든 레코드 조회하기
  SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;

 2) 역순 정렬하기
  SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;

 3) 아픈 동물 찾기
  SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION="Sick" ORDER BY ANIMAL_ID;
 
 4) 어린 동물 찾기
 5) 동물의 아이디와 이름
 6) 여러 기준으로 정렬하기
 7) 상위 n개 레코드
2. SUM, MAX, MIN 
 1) 최댓값 구하기
 2) 최솟값 구하기
 3) 동물 수 구하기
 4) 중복 제거하기
3. GROUP BY
 1) 고양이와 개는 몇 마리 있을까
 2) 동명 동물 수 찾기
 3) 입양 시각 구하기(1)
 4) 입양 시각 구하기(2)