import torch

class ModelYolo:
    def __init__(self):
        # self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='Lens_best.pt', source='local') # yolov5n - yolov5x6 or custom
        # CUDA 장치 설정
        # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # if device.type == 'cuda': 
        #     torch.cuda.set_device(0)  #원하는 GPU 장치 번호로 설정
        # 모델 로드
        self.model = torch.hub.load('./ultralytics/yolov5', 'custom', path='SmartPhone_best.pt', source='local')
        # self.__model.to(device)  # 모델을 GPU로 이동