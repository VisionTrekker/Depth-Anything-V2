import os

GPU_ID = 1

# 估计绝对深度（以m为单位）
print("--------------------------------------------------------------")
# 可选：--input-size 720   可能设为短边的整数除
#      --pred-only --grayscale --save-numpy
# 室内场景--max-depth 20；室外场景--max-depth 80
# remote_data/dataset_opensource
# Dataset/3DGS_Dataset
# CBD_building_02

scenes = {"TQZZ": 80}
for idx, scene in enumerate(scenes.items()):
        cmd = f'CUDA_VISIBLE_DEVICES={GPU_ID} \
                python run.py \
                --encoder vitl \
                --load-from ../checkpoints/depth_anything_v2_metric_hypersim_vitl.pth \
                --max-depth {scene[1]} \
                --img-path ../../../remote_data/dataset_reality/test/{scene[0]}/images \
                --outdir ../../../remote_data/dataset_reality/test/{scene[0]}/depth \
                --input-size 480 \
                --save-numpy'
        print(cmd)
        os.system(cmd)

# /home/liuzhi/Disk_data/dataset_reality/siyue/0830_F1_depth
# root_dir = "/data2/liuzhi/remote_data/dataset_reality/siyue/0910_F1+air_full/images"
# subfolder1_list = os.listdir(root_dir)
# for subfolder1 in subfolder1_list:
#         if subfolder1 == "F1yard_out":
#                 continue
#         folder1_path = os.path.join(root_dir, subfolder1)
#
#         if len(os.listdir(folder1_path)) == 4:
#                 for subfolder2 in ["00", "01", "02", "03"]:
#                         cmd = f'CUDA_VISIBLE_DEVICES={GPU_ID} \
#                                 python run.py \
#                                 --encoder vitl \
#                                 --load-from ../checkpoints/depth_anything_v2_metric_hypersim_vitl.pth \
#                                 --max-depth 80 \
#                                 --img-path /data2/liuzhi/remote_data/dataset_reality/siyue/0910_F1+air_full/images/{subfolder1}/{subfolder2} \
#                                 --outdir /data2/liuzhi/remote_data/dataset_reality/siyue/0910_F1+air_full/depth/{subfolder1}/{subfolder2} \
#                                 --input-size 518 \
#                                 --save-numpy \
#                                 '
#                         print(cmd)
#                         os.system(cmd)
#         else:
#                 cmd = f'CUDA_VISIBLE_DEVICES={GPU_ID} \
#                                                 python run.py \
#                                                 --encoder vitl \
#                                                 --load-from ../checkpoints/depth_anything_v2_metric_hypersim_vitl.pth \
#                                                 --max-depth 80 \
#                                                 --img-path /data2/liuzhi/remote_data/dataset_reality/siyue/0910_F1+air_full/images/{subfolder1} \
#                                                 --outdir /data2/liuzhi/remote_data/dataset_reality/siyue/0910_F1+air_full//depth/{subfolder1} \
#                                                 --input-size 518 \
#                                                 --save-numpy \
#                                                 '
#                 print(cmd)
#                 os.system(cmd)

# root_dir = "/data2/liuzhi/remote_data/dataset_reality/anji_qiyu/images"
# subfolder1_list = os.listdir(root_dir)
# for subfolder1 in subfolder1_list:
#         folder1_path = os.path.join(root_dir, subfolder1)
#
#         if len(os.listdir(folder1_path)) == 8:
#                 for subfolder2 in ["00", "01", "02", "03"]:
#                         cmd = f'CUDA_VISIBLE_DEVICES={GPU_ID} \
#                                 python run.py \
#                                 --encoder vitl \
#                                 --load-from ../checkpoints/depth_anything_v2_metric_hypersim_vitl.pth \
#                                 --max-depth 80 \
#                                 --img-path /data2/liuzhi/remote_data/gcc/images/{subfolder1}/{subfolder2} \
#                                 --outdir /data2/liuzhi/remote_data/gcc/depth/{subfolder1}/{subfolder2} \
#                                 --input-size 518 \
#                                 --save-numpy \
#                                 '
#                         print(cmd)
#                         os.system(cmd)



# 从2D图像生成点云
# print("--------------------------------------------------------------")
# cmd = f'CUDA_VISIBLE_DEVICES={GPU_ID} \
#         python depth_to_pointcloud.py \
#         --encoder vitl \
#         --load-from ../checkpoints/depth_anything_v2_metric_hypersim_vitl.pth \
#         --max-depth 30 \
#         --img-path ../assets/gm_Museum/00 \
#         --outdir ../results/metric_results/gm_Museum_vis/00 \
#         '
# print(cmd)
# os.system(cmd)
