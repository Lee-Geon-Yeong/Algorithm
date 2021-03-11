
1. SELECT
 1) 모든 레코드 조회하기
  SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;

 2) 역순 정렬하기
  SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;

 3) 아픈 동물 찾기
  SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION="Sick" ORDER BY ANIMAL_ID;
 
 4) 어린 동물 찾기
  SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION!='Aged' ORDER BY ANIMAL_ID ASC;
 
 5) 동물의 아이디와 이름
  SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC;
 
 6) 여러 기준으로 정렬하기
  SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC, DATETIME DESC;
 
 7) 상위 n개 레코드
  SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1;

2. SUM, MAX, MIN 
 1) 최댓값 구하기
  SELECT MAX(DATETIME) FROM ANIMAL_INS
 2) 최솟값 구하기
  SELECT MIN(DATETIME) FROM ANIMAL_INS
 3) 동물 수 구하기
  SELECT COUNT(*) FROM ANIMAL_INS
 4) 중복 제거하기

3. GROUP BY
 1) 고양이와 개는 몇 마리 있을까

 2) 동명 동물 수 찾기

 3) 입양 시각 구하기(1)

 4) 입양 시각 구하기(2)

4. IS NULL
 1) 이름이 없는 동물의 아이디

 2) 이름이 있는 동물의 아이디

 3) NULL 처리하기

5. JOIN
 1) 없어진 기록 찾기

 2) 있었는데요 없었습니다


 3) 오랜 기간 보호한 동물(1)

 4) 보호소에서 중성화한 동물

6. String, Date
 1) 루시와 엘라 찾기

 2) 이름에 el이 들어가는 동물 찾기

 3) 중성화 여부 파악하기

 4) 오랜 기간 보호한 동물(2)

 5) DATETIME에서 DATE로 형 변환
