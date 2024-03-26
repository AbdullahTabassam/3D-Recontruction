import open3d as o3d
import matplotlib.pyplot as plt
import cv2



color_raw = o3d.io.read_image('model images/images/new.jpg')
depth_raw = o3d.io.read_image('model images/depth/new.png')
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color_raw, depth_raw)
print(rgbd_image)


plt.subplot(1, 2, 1)
plt.title('grayscale image')
plt.imshow(rgbd_image.color)
plt.subplot(1, 2, 2)
plt.title('depth image')
plt.imshow(rgbd_image.depth)
plt.show()


cv_file = cv2.FileStorage()
cv_file.open('cameraIntrinsic.xml', cv2.FileStorage_READ)

camera_intrinsic = cv_file.getNode('intrinsic').mat()


pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(width= 1366, 
                                  height= 768, 
                                  fx=camera_intrinsic[0][0],
                                  fy= camera_intrinsic[1][1],
                                  cx= camera_intrinsic[0][2], 
                                  cy= camera_intrinsic[1][2]))


# Flip it, otherwise the pointcloud will be upside down
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])



vis = o3d.visualization.Visualizer()
vis.create_window(visible=True)
# Call only after creating visualizer window.
vis.get_render_option().background_color = [100/225,100/225,100/225]
vis.add_geometry(pcd)
vis.run()




