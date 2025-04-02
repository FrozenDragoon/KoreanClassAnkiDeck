<!-- markdownlint-disable MD024 -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
