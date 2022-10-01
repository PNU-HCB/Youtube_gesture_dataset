# 유튜브 동영상 데이터 셋

동장 생성 모델 학습을 위한 데이터 셋 생성을 위해 유튜브 채널로부터 영상과 자막 파일을 얻습니다. 영상으로부터 스켈레톤 데이터를 추출하고 클립으로 나누어 유효한 클립으로부터 포즈 데이터를 얻을 수 있습니다. 최종적으로는 3차원 Pose 데이터를 Lmdb 형식으로 얻을 수 있습니다.

[참고 논문](https://arxiv.org/abs/1810.12541)

## 환경 설정

- OS (Window10 64bit)
- CPU (Intel(R) Core(TM) i9-10900K)
- GPU (RTX 3090)
- RAM (64GM)
- CUDA (11.1)
- PyTorch (1.12.1)
- TensorFlow (2.9.1)
- OpenPose (1.7.0)
- FastText (0.9.2)

## 실행 순서

1. 구성

   - Youtube Develop Key와 채널 ID를 업데이트합니다.

2. `download_video.py` 실행

   - Youtube 영상, 메타데이터, 자막을 다운로드합니다.

3. `run_openpose.py` 실행

   - OpenPose를 통해 모든 동영상에서 2차원 Pose를 추출합니다.

4. `run_scenedetect.py` 실행

   - PySceneDetect를 실행하여 비디오를 클립으로 나눕니다.

5. `run_clip_filtering.py` 실행

   - 유효하지 않은 클립을 제거합니다.

6. `make_lmdb_test.py` 실행
   - 2차원 Pose를 바탕으로 3차원 Pose를 추정하고 일부 후처리 후 데이터 셋을 생성합니다.
