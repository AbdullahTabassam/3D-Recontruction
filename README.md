# 3D Reconstruction Project

## Overview

This project focuses on utilizing computer vision techniques to reconstruct 3D scenes from monocular images captured by a single camera. The pipeline involves camera calibration, depth map generation, creation of RGBD images, point cloud generation, and trajectory estimation for multiple images. The ultimate goal is to combine these components to produce a complete 3D representation of the scene.

### Color Image, Depth Estimation, and 3D Point Cloud

<div>
<img src="https://github.com/AbdullahTabassam/3D-Recontruction/blob/main/model_images/images/new.jpg" alt="Image"  width="250">
<img src="https://github.com/AbdullahTabassam/3D-Recontruction/blob/main/model_images/depth/new.png" alt="Image"  width="250">
<img src="https://github.com/AbdullahTabassam/3D-Recontruction/blob/main/3D-PointCloud.png" alt="Image"  width="250">
</div>

## Features

- **Camera Calibration**: The camera intrinsic and extrinsic parameters are calibrated to accurately interpret the geometry of the scene.
  
- **Depth Map Generation**: Utilizing Transformer-based vision models, depth maps are generated from monocular images. Initially, Hugging Face Spaces platform is used, with future integration planned for MIDAS v3.1 model to enhance depth map quality.
  
- **RGBD Image Creation**: Depth maps are combined with corresponding RGB images to form RGBD images, providing both color and depth information.

    <img src="https://github.com/AbdullahTabassam/3D-Recontruction/blob/main/DepthMap.png" alt="Image"  width="600">
  
- **Point Cloud Generation**: RGBD images are processed to extract point clouds, representing the scene in a 3D coordinate system.
  
- **Trajectory Estimation**: ORB features and RANSAC will be employed to map multiple images and estimate rotational and translational parameters for each image. This information will be used to create a trajectory file, facilitating the alignment of multiple point clouds to reconstruct the complete scene in 3D.

## Libraries requited:
- Open3D
- OpenCV-Python
- Numpy
- Matplotlib
- Scikit-Image

## Skills Demonstrated

- Proficiency in camera calibration techniques.
- Experience with Transformer-based vision models for depth map generation.
- Familiarity with RGBD image processing.
- Understanding of point cloud generation from RGBD images.
- Knowledge of feature matching algorithms for trajectory estimation.
- Ability to integrate multiple components into a cohesive pipeline for 3D reconstruction.

## Future Work

- Integration of MIDAS v3.1 model for improved depth map generation.
- Optimization of trajectory estimation algorithms for better accuracy and efficiency.
- Exploration of additional techniques for scene reconstruction, such as bundle adjustment.

## Author

Abdullah Ikram Ullah Tabassam

<a href="https://www.linkedin.com/in/abdullah-ikram-ullah-tabassam-1103b021b/" target="_blank" >Linkedin</a>

Email: <a href="mailto:abdullahdar2017@gmail.com" >abdullahdar2017@gmail.com</a>
