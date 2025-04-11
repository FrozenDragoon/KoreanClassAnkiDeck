<!-- markdownlint-disable MD024 -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.4] - 2025-04-11

**Note:** 임신듸다  card must be manually deleted.

### Added

- Add Section 2 Week 3 Vocab
  - 양치하다
  - 거실
  - 운동하다
  - 금요일
  - 월요일
  - 커피
  - 차
  - 만들다
  - 끓이다
  - 일어나다
  - 뒤뜰
  - 일요일
  - 매일
  - 면도하다
  - 목요일
  - 부엌
  - 샤워하다
  - 소변보다
  - 수요일
  - 식당
  - 정원
  - 주말
  - 주일
  - 침실
  - 토요일
  - 학요
  - 화요일
  - 화장실
  - 일하러가다
  - 아침
  - 아침식사
  - 식사
  - 먹다
  - 마당
  - 앞마당
  - 학요에가다
  - 가다
  - 학교
  - 화장실에가다
  - 대변보다
  - 月
  - 火
  - 水
  - 木
  - 金
  - 土
  - 日
  - 침대

### Fixed

- 임신듸다 -> 임신되다 "To become pregnant" / "To conceive" (#1)

## [0.0.3-1] - 2025-04-04

**Note:** 내의 and 성진 cards must be manually deleted.

### Added

- Add additional sentences

### Fixed

- 내의 -> 내외 "Couple"
- 성진 -> 성인 "Adult"
- 덩생 - "Sibling" corrected to "Younger Sibling"

## [0.0.3] - 2025-04-04

### Added

- Added Section 2 Week 2 Vocabulary
  - 내의
  - 배우자
  - 성진
  - 남편
  - 부인
  - 아내
  - 부모
  - 아버지
  - 아버님
  - 아빠
  - 어마니
  - 어마님
  - 엄마
  - 아이
  - 어린이
  - 아이들
  - 어린이들
  - 아들
  - 딸
  - 할부모
  - 할아버지
  - 할어마니
  - 삼촌
  - 이모
  - 사촌
  - 형
  - 누나
  - 오빠
  - 언니
  - 남동생
  - 여동생
  - 동생
  - 약혼하다
  - 결혼하다
  - 이혼하다
  - 죽다
  - 사망하다
  - 생일
  - 환갑

### Changed

- Removed `media` folder from the git repo. The audio files don't need to be (and in the case
of Forvo audio can't be) stored in the repo.

## [0.0.2-2] - 2025-04-02

### Changed

- Fixed typo in sentence for `제` (`이룸` -> `이름`)
- Added new sentences

## [0.0.2] - 2025-04-02

### Breaking Change

This import will create duplicate notes. This is due to changing how note IDs are generated.

### Added

- New vocab words from `Section 2 Week 1`
  - 저
  - 나
  - 제
  - 내
  - 네
  - 네
  - 저희
  - 저희의
  - 우리
  - 우리의
  - 그남자
  - 그여자
  - 그남자의
  - 그여자의
  - 그사람
  - 그사람의
  - 임신듸다
  - 임신이다
- Added tag `KJMSSection2Week1` to all relevant cards

## Changed

- Note IDs are now generated using fields `Vocab, Pre-Vocab-Context, Post-Vocab-Context, Vocab-Pro`
  - Previously it was incorrectly just `Vocab, Pre-Vocab-Context`
- Generated TTS audio now prefers the `Vocab-Pro` field (to generate a phonetic pronunciation)
- Create (and clean up if successful) a backup of `input.csv`, so it will not get accidentally wiped
- Additional logging added

## [0.0.1] - 2025-04-02

First release version

### Added

- New vocab words from `Section 2 Week 1`
  - 임신
  - 태어나다
  - 살다
  - 친구
  - 남자
  - 여자
  - 가족
  - 집
