# MONDE-MUNCHKIN
MONDEIQUE AI server

## API
### OD API (Object-Detection API)
- input image 에 대한 frozen_inference_graph.pb 를 불러와 ltrb 결과를 뽑아내 Response 로 반환
### CE API (Color-Extraction API)
- cropped image 가 input image로 들어와 image 전체를 colorgram으로 분석해 추출된 color_result 값을 Response 로 반환
### MTL API (Multi-Task Learning API)
- cropped image 가 input image로 들어와 image 에 대한 category 값을 saved_model.pb 를 이용해 category 결과를 뽑아내 Response 로 반환
