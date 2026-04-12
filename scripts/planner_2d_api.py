from get_2d_planner import get_grasps, Grasp2D

MASK_PATH = "masks/camera_mount_1/mask.png"
MASK_PIXELS_PER_METER = 1985.6279949293314

grasps: list[Grasp2D] = get_grasps(MASK_PATH, pixels_per_meter=MASK_PIXELS_PER_METER)
best = grasps[0]
print(best.midpoint, best.epsilon, best.force_closure)