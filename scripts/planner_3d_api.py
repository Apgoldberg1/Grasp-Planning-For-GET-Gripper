from get_3d_planner import get_grasps, Grasp3D

if __name__ == "__main__":
    grasps = get_grasps("meshes/gearbox_2.obj", target_count=10)
    best = grasps[0]
    print(best.position.as_matrix(), best.quality, best.force_closure)
