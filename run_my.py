import os

GPU_ID = 3

# 估计相对深度
print("--------------------------------------------------------------")
# 可选：--pred-only --grayscale
# 估计图片

# scenes = {"bicycle":4, "bonsai":2, "counter":2, "garden":4, "stump":4, "kitchen":2, "room":2}
scenes = {"garden":4}
for idx, scene in enumerate(scenes.items()):
        cmd = f'CUDA_VISIBLE_DEVICES={GPU_ID} \
                python run.py \
                --encoder vitl \
                --img-path ../../remote_data/dataset_opensource/Mip_NeRF360_v2/{scene[0]}/train/images_{scene[1]} \
                --outdir ../../remote_data/dataset_opensource/Mip_NeRF360_v2/{scene[0]}/train/depth_relative \
                --input-size 840 \
                --pred-only \
                --grayscale \
                '
        print(cmd)
        os.system(cmd)
# 估计视频
# cmd = f'CUDA_VISIBLE_DEVICES={GPU_ID} \
#         python run_video.py \
#         --encoder vitl \
#         --video-path assets/example_video \
#         --outdir video_depth_vis \
#         --input-size 720 \
#         --pred-only \
#         --grayscale'

# print(cmd)
# os.system(cmd)


