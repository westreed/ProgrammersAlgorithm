# 문제정리용 Repository

이 리포지토리는 코딩테스트를 대비하여 여러 문제의 코드풀이를 정리해서 업로드 및 관리하는 용도입니다.<br>
해당 리포티토리를 활용하시려면, 각 사이트별 난이도 폴더 안의 내용을 전부 삭제해주세요.<br><br>

！혹은 아래의 레포지토리 링크로 이동하여 사용하시면 됩니다.<br>
바로가기 → [ProgrammersAlgorithmDeploy](https://github.com/westreed/ProgrammersAlgorithmDeploy)

## 사용방법

1. `scripts/data.py` 안의 `folder_List` 내용을 (폴더이름, 사이트이름) 순으로 입력해주세요.
2. `scripts/data.py` 안의 `githubLink`는 레포지토리 링크를 적어주세요. (`https://github.com/` 생략)
3. 각 폴더 안에는 난이도별로 또다시 폴더를 구분해주세요. (이름은 마음대로 지으셔도 됩니다)
4. 해당 폴더 안에 풀었던 문제파일을 업로드하세요.
5. github에 업로드하면, gitAction에 의해, `scripts 폴더`안의 py파일이 실행되어 md 파일을 생성합니다.
6. 해결하지 못한 문제는 파일명 뒤에 X를 붙이면, 해결하지 못한 문제로 계산됩니다.

## Github Action 오류

1. Permission 오류

```bash
[main 73adc1d] update README.md
 2 files changed, 2 insertions(+), 2 deletions(-)
remote: Permission to westreed/ProgrammersAlgorithmDeploy.git denied to github-actions[bot].
fatal: unable to access 'https://github.com/westreed/ProgrammersAlgorithm/': The requested URL returned error: 403
Error: Process completed with exit code 128.
```

Action에서 다음과 비슷한 오류가 발생했을 때, [Settings]-[Actions]-[General]으로 들어가서<br>
아래 이미지와 같이 설정하세요.

![Setting](https://github.com/westreed/ProgrammersAlgorithm/blob/main/src/Settings.png)



## BAEKJOON


| 문제 난이도 | 문제 링크 | 해결한 문제 | 전체 문제 | 해결비율(%) |
| :--: |:--: |:--: |:--: |:--: |
|1Bronze|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/BAEKJOON/1Bronze.md)|24|24|100%|
|2Silver|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/BAEKJOON/2Silver.md)|104|104|100%|
|3Gold|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/BAEKJOON/3Gold.md)|53|55|96%|
|4Platinum|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/BAEKJOON/4Platinum.md)|01|02|50%|

## 프로그래머스


| 문제 난이도 | 문제 링크 | 해결한 문제 | 전체 문제 | 해결비율(%) |
| :--: |:--: |:--: |:--: |:--: |
|Level1|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/Programmers/Level1.md)|57|57|100%|
|Level2|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/Programmers/Level2.md)|59|63|94%|
|Level3|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/Programmers/Level3.md)|29|31|94%|
|Level4|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/Programmers/Level4.md)|01|02|50%|

## SAMSUNG SW Expert Academy


| 문제 난이도 | 문제 링크 | 해결한 문제 | 전체 문제 | 해결비율(%) |
| :--: |:--: |:--: |:--: |:--: |
|Level1|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/SAMSUNG_SW_Expert_Academy/Level1.md)|08|08|100%|
|Level2|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/SAMSUNG_SW_Expert_Academy/Level2.md)|06|06|100%|
|Level3|[바로가기](https://github.com/westreed/ProgrammersAlgorithm/blob/main/SAMSUNG_SW_Expert_Academy/Level3.md)|59|60|98%|


**Update Date 2024/10/18 20:21:01 KST**