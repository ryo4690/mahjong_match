import torch
precision = 'fp32'
ssd_model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd', model_math=precision)
utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')

# CPUで動くようにして、推論モード
ssd_model.to('cpu')
ssd_model.eval()

import glob
# 検出する画像リスト
img_files = glob.glob('od_dogs/*.jpg')
uris = [
    img_files[0],
    img_files[1],
]

# 入力データ作成
inputs = [utils.prepare_input(uri) for uri in uris]
tensor = utils.prepare_tensor(inputs, precision == 'fp16')
tensor = tensor.to('cpu')

