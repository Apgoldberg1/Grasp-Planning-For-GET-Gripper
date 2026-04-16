# 2D and 3D Grasp Planners for the GET Asymmetrical Gripper

**[Paper](https://apgoldberg1.github.io/GET_Planning/media/GET_Planning_Paper.pdf) | [Website](https://apgoldberg1.github.io/GET_Planning/)**

**Andrew Goldberg**<sup>1</sup>, **Ethan Ransing**<sup>1</sup>, **Anton Kourakin**<sup>1</sup>, **Cael Magner**<sup>1</sup>, **Edward H. Adelson**<sup>2</sup>, **Ken Goldberg**<sup>1</sup>

<sup>1</sup>AUTOLab at the University of California, Berkeley &nbsp;&nbsp; <sup>2</sup>Massachusetts Institute of Technology

---

This is the official codebase for the grasp planners, data, and designs accompanying the paper 2D and 3D Grasp Planners for the GET Asymmetrical Gripper. We release two planners: GET-2D-1.0, a 2D planner that operates on object cross-sections, masks, or point clouds, and GET-3D-1.0, a 3D planner that plans directly on mesh geometry.

## Overview

**`get_2d_planner/`** — Grasp planner operating on 2D cross-sections. Accepts meshes (`.obj`, `.stl`, `.ply`), binary masks (`.png`, `.jpg`), or point clouds (`.npy`). Returns grasps ranked by epsilon quality and force closure.

**`get_3d_planner/`** — Grasp planner operating on 3D meshes. Samples and optimizes grasp poses using Ferrari-Canny quality with optional robustness evaluation under pose perturbations. Accepts `.obj`, `.stl`, `.ply`, `.glb`, `.gltf`.

**`gripper_files/`** — CAD files (`.f3d`, `.step`, `.stl`) for the GET gripper with flat and rounded finger variants.

**`meshes/`** — 20 benchmark object meshes used in our evaluation.

**`masks/`** — Binary masks, precomputed grasps, and summary files for each benchmark object.

**`scripts/`** — Minimal Python API usage examples for both planners.

## Setup

Clone the repository with submodules:

```bash
git clone --recurse-submodules https://github.com/Apgoldberg1/Grasp-Planning-For-GET-Gripper.git
```

Or if already cloned:

```bash
git submodule update --init --recursive
```

Both planners require Python 3.12+ and [uv](https://docs.astral.sh/uv/).

To use the API scripts in `scripts/`, create a virtual environment and install both planners into it:

```bash
uv venv
uv pip install -e get_2d_planner -e get_3d_planner
```

## Quick Start

**2D planner grasp generation example:**
```bash
uv run scripts/planner_2d_api.py 
```

**3D planner grasp generation example:**
```bash
uv run scripts/planner_3d_api.py 
```

See each planner's `README.md` for full CLI usage, available parameters, and visualization options.

## Citation

If you use this code, please cite our paper:

```bibtex
@article{goldberg2026getplanning,
  title   = {2D and 3D Grasp Planners for the GET Asymmetrical Gripper},
  author  = {Goldberg, Andrew and Ransing, Ethan and Kourakin, Anton and Magner, Cael and Adelson, Edward H. and Goldberg, Ken},
  journal = {},
  year    = {2026},
  url     = {},
}
```
