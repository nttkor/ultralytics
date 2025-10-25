---
comments: true
description: YOLO26 from Ultralytics delivers faster, simpler, end-to-end NMS-free object detection optimized for edge and low-power devices.
keywords: YOLO26, Ultralytics YOLO, object detection, end-to-end NMS-free, simplified architecture, computer vision, AI, machine learning, edge AI, low power devices, quantization, real-time inference
---

# Ultralytics YOLO26

!!! note "Coming Soon ⚠️"

    🚧 YOLO26 models are still under development and not yet released. Performance numbers shown here are **previews only**.
    Final downloads and releases will follow soon — stay updated via [YOLO Vision 2025](https://www.ultralytics.com/events/yolovision).

## Overview

[Ultralytics](https://www.ultralytics.com/) YOLO26 is the latest evolution in the YOLO series of real-time object detectors, engineered from the ground up for **edge and low-power devices**. It introduces a streamlined design that removes unnecessary complexity while integrating targeted innovations to deliver faster, lighter, and more accessible deployment.

The architecture of YOLO26 is guided by three core principles:

- **Simplicity:** YOLO26 is a **native end-to-end model**, producing predictions directly without the need for non-maximum suppression (NMS). By eliminating this post-processing step, inference becomes faster, lighter, and easier to deploy in real-world systems. This breakthrough approach was first pioneered in [YOLOv10](../models/yolov10.md) by Ao Wang at Tsinghua University and has been further advanced in YOLO26.
- **Deployment Efficiency:** The end-to-end design cuts out an entire stage of the pipeline, dramatically simplifying integration, reducing latency, and making deployment more robust across diverse environments.
- **Training Innovation:** YOLO26 introduces the **MuSGD optimizer**, a hybrid of [SGD](https://docs.pytorch.org/docs/stable/generated/torch.optim.SGD.html) and [Muon](https://arxiv.org/abs/2502.16982) — inspired by Moonshot AI's [Kimi K2](https://kimi.moonshot.cn/) breakthroughs in LLM training. This optimizer brings enhanced stability and faster convergence, transferring optimization advances from language models into computer vision.

Together, these innovations deliver a model family that achieves higher accuracy on small objects, provides seamless deployment, and runs **up to 43% faster on CPUs** — making YOLO26 one of the most practical and deployable YOLO models to date for resource-constrained environments.

![Ultralytics YOLO26 Comparison Plots](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolo-comparison-plot.png)

## Key Features

- **DFL Removal**  
  The Distribution Focal Loss (DFL) module, while effective, often complicated export and limited hardware compatibility. YOLO26 removes DFL entirely, simplifying inference and broadening support for **edge and low-power devices**.

- **End-to-End NMS-Free Inference**  
  Unlike traditional detectors that rely on NMS as a separate post-processing step, YOLO26 is **natively end-to-end**. Predictions are generated directly, reducing latency and making integration into production systems faster, lighter, and more reliable.

- **ProgLoss + STAL**  
  Improved loss functions increase detection accuracy, with notable improvements in **small-object recognition**, a critical requirement for IoT, robotics, aerial imagery, and other edge applications.

- **MuSGD Optimizer**  
  A new hybrid optimizer that combines [SGD](https://docs.pytorch.org/docs/stable/generated/torch.optim.SGD.html) with [Muon](https://arxiv.org/abs/2502.16982). Inspired by Moonshot AI's [Kimi K2](https://kimi.moonshot.cn/), MuSGD introduces advanced optimization methods from LLM training into computer vision, enabling more stable training and faster convergence.

- **Up to 43% Faster CPU Inference**  
  Specifically optimized for edge computing, YOLO26 delivers significantly faster CPU inference, ensuring real-time performance on devices without GPUs.

---

## Supported Tasks and Modes

YOLO26 is designed as a **multi-task model family**, extending YOLO's versatility across diverse computer vision challenges:

| Model       | Task                                         | Inference | Validation | Training | Export |
| ----------- | -------------------------------------------- | --------- | ---------- | -------- | ------ |
| YOLO26      | [Detection](../tasks/detect.md)              | ✅        | ✅         | ✅       | ✅     |
| YOLO26-seg  | [Instance Segmentation](../tasks/segment.md) | ✅        | ✅         | ✅       | ✅     |
| YOLO26-pose | [Pose/Keypoints](../tasks/pose.md)           | ✅        | ✅         | ✅       | ✅     |
| YOLO26-obb  | [Oriented Detection](../tasks/obb.md)        | ✅        | ✅         | ✅       | ✅     |
| YOLO26-cls  | [Classification](../tasks/classify.md)       | ✅        | ✅         | ✅       | ✅     |

This unified framework ensures YOLO26 is applicable across real-time detection, segmentation, classification, pose estimation, and oriented object detection — all with training, validation, inference, and export support.

---

## Performance Metrics

!!! tip "Performance Preview"

    The following benchmarks are **early previews**. Final numbers and downloadable weights will be released once training is complete.

    === "Detection (COCO)"

        Trained on [COCO](../datasets/detect/coco.md) with 80 pre-trained classes.
        See [Detection Docs](../tasks/detect.md) for usage once models are released.

        | Model   | size<br><sup>(pixels) | mAP<sup>val<br>50-95(e2e) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms)  | Speed<br><sup>T4 TensorRT10<br>(ms)  | params<br><sup>(M) | FLOPs<br><sup>(B) |
        | -----   | --------------------- | --------------------      | -------------------- | ------------------------------- | ------------------------------------ | ------------------ | ----------------- |
        | YOLO26n | 640                   | 40.1                      | 40.9                 | 38.9 ± 0.7                      | 1.7 ± 0.0                            | 2.4                | 5.4               |
        | YOLO26s | 640                   | 47.4                      | 47.0                 | 87.2 ± 0.9                      | 2.7 ± 0.0                            | 9.5                | 20.7              |
        | YOLO26m | 640                   | 51.9                      | 52.4                 | 220.0 ± 1.4                     | 4.9 ± 0.1                            | 20.4               | 68.2              |
        | YOLO26l | 640                   | 53.6                      | 54.1                 | 286.2 ± 2.0                     | 6.5 ± 0.2                            | 24.8               | 86.4              |
        | YOLO26x | 640                   | 55.9                      | 56.2                 | 525.8 ± 4.00                    | 11.8 ± 0.2                           | 55.73              | 193.88            |


    === "Segmentation (COCO)"

        | Model       | size<br><sup>(pixels) | mAP<sup>val<br>50-95(e2e) | mAP<sup>mask<br>50-95(e2e) | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>T4 TensorRT10<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
        |-------------|-----------------------|---------------------------|----------------------------|--------------------------------|-------------------------------------|--------------------|-------------------|
        | YOLO26n-seg | 640                   | 38.0                      | 31.6                       | 53.3 ± 0.5                     | 2.0 ± 0.0                           | 2.66               | 8.62              |
        | YOLO26s-seg | 640                   | 46.3                      | 38.2                       | 118.4 ± 0.9                    | 3.5 ± 0.0                           | 10.15              | 32.18             |
        | YOLO26m-seg | 640                   | 51.5                      | 42.3                       | 328.2 ± 2.4                    | 7.5 ± 0.1                           | 22.72              | 113.43            |
        | YOLO26l-seg | 640                   | 53.1                      | 43.6                       | 387.0 ± 3.7                    | 8.4 ± 0.1                           | 27.11              | 131.68            |
        | YOLO26x-seg | 640                   | 55.4                      | 45.4                       | 787.0 ± 6.8                    | 18.4 ± 0.1                          | 60.90              | 295.34            |

    === "Classification (ImageNet)"

        | Model       | size<br><sup>(pixels) | acc<br><sup>top1 | acc<br><sup>top5 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>T4 TensorRT10<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) at 224 |
        |-------------|-----------------------|------------------|------------------|--------------------------------|-------------------------------------|--------------------|--------------------------|
        | YOLO26n-cls | 224                   | 71.4             | 90.1             | 5.0 ± 0.3                      | 1.1 ± 0.0                           | 2.8                | 0.5                      |
        | YOLO26s-cls | 224                   | 76.0             | 92.9             | 7.9 ± 0.2                      | 1.3 ± 0.0                           | 6.7                | 1.6                      |
        | YOLO26m-cls | 224                   | 78.1             | 94.2             | 17.2 ± 0.4                     | 2.0 ± 0.0                           | 11.6               | 4.9                      |
        | YOLO26l-cls | 224                   | 79.0             | 94.6             | 23.2 ± 0.3                     | 2.8 ± 0.0                           | 14.1               | 6.2                      |
        | YOLO26x-cls | 224                   | 79.9             | 95.0             | 41.4 ± 0.9                     | 3.8 ± 0.0                           | 29.6               | 13.6                     |

    === "Pose (COCO)"

        | Model        | size<br><sup>(pixels) | mAP<sup>val<br>50-95(e2e) | mAP<sup>pose<br>50(e2e) | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>T4 TensorRT10<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
        |--------------|-----------------------|---------------------------|-------------------------|--------------------------------|-------------------------------------|--------------------|-------------------|
        | YOLO26n-pose | 640                   | 55.2                      | 82.4                    | 40.3 ± 0.5                     | 1.8 ± 0.0                           | 2.66               | 6.71              |
        | YOLO26s-pose | 640                   | 62.2                      | 86.9                    | 85.3 ± 0.9                     | 2.9 ± 0.0                           | 9.96               | 23.95             |
        | YOLO26m-pose | 640                   | 67.3                      | 89.4                    | 218.0 ± 1.5                    | 5.6 ± 0.1                           | 21.21              | 77.84             |
        | YOLO26l-pose | 640                   | 69.5                      | 90.5                    | 275.4 ± 2.4                    | 7.3 ± 0.1                           | 25.60              | 96.08             |
        | YOLO26x-pose | 640                   | 71.2                      | 91.4                    | 565.4 ± 3.0                    | 13.9 ± 0.2                          | 57.56              | 215.73            |

    === "OBB (DOTAv1)"

        | Model       | size<br><sup>(pixels) | mAP<sup>test<br>50(e2e) | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>T4 TensorRT10<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
        |-------------|-----------------------|-------------------------|--------------------------------|-------------------------------------|--------------------|-------------------|
        | YOLO26n-obb | 1024                  | 78.9                    | 97.7 ± 0.9                     | 2.9 ± 0.0                           | 2.45               | 14.0              |
        | YOLO26s-obb | 1024                  | 79.8                    | 218.0 ± 1.4                    | 5.6 ± 0.1                           | 9.76               | 55.1              |
        | YOLO26m-obb | 1024                  | 80.7                    | 579.2 ± 3.8                    | 12.2 ± 0.3                          | 21.21              | 183.3             |
        | YOLO26l-obb | 1024                  | 81.4                    | 735.6 ± 3.1                    | 16.5 ± 0.2                          | 25.61              | 230.0             |
        | YOLO26x-obb | 1024                  | 82.1                    | 1485.7 ± 11.5                  | 34.7 ± 0.9                          | 57.56              | 516.5             |

---

## Citations and Acknowledgements

!!! tip "Ultralytics YOLO26 Publication"

    Ultralytics has not published a formal research paper for YOLO26 due to the rapidly evolving nature of the models. Instead, we focus on delivering cutting-edge models and making them easy to use. For the latest updates on YOLO features, architectures, and usage, visit our [GitHub repository](https://github.com/ultralytics/ultralytics) and [documentation](https://docs.ultralytics.com/).

If you use YOLO26 or other Ultralytics software in your work, please cite it as:

!!! quote ""

    === "BibTeX"

        ```bibtex
        @software{yolo26_ultralytics,
          author = {Glenn Jocher and Jing Qiu},
          title = {Ultralytics YOLO26},
          version = {26.0.0},
          year = {2025},
          url = {https://github.com/ultralytics/ultralytics},
          orcid = {0000-0001-5950-6979, 0000-0003-3783-7069},
          license = {AGPL-3.0}
        }
        ```

DOI pending. YOLO26 is available under [AGPL-3.0](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) and [Enterprise](https://www.ultralytics.com/license) licenses.

---

## FAQ

### What are the key improvements in YOLO26 compared to YOLO11?

- **DFL Removal**: Simplifies export and expands edge compatibility
- **End-to-End NMS-Free Inference**: Eliminates NMS for faster, simpler deployment
- **ProgLoss + STAL**: Boosts accuracy, especially on small objects
- **MuSGD Optimizer**: Combines SGD and Muon (inspired by Moonshot's Kimi K2) for more stable, efficient training
- **Up to 43% Faster CPU Inference**: Major performance gains for CPU-only devices

### What tasks will YOLO26 support?

YOLO26 is designed as a **unified model family**, providing end-to-end support for multiple computer vision tasks:

- [Object Detection](../tasks/detect.md)
- [Instance Segmentation](../tasks/segment.md)
- [Image Classification](../tasks/classify.md)
- [Pose Estimation](../tasks/pose.md)
- [Oriented Object Detection (OBB)](../tasks/obb.md)

Each size variant (n, s, m, l, x) is planned to support all tasks at release.

### Why is YOLO26 optimized for edge deployment?

YOLO26 delivers **state-of-the-art edge performance** with:

- Up to 43% faster CPU inference
- Reduced model size and memory footprint
- Architecture simplified for compatibility (no DFL, no NMS)
- Flexible export formats including TensorRT, ONNX, CoreML, TFLite, and OpenVINO

### When will YOLO26 models be available?

YOLO26 models are still in training and not yet open-sourced. Performance previews are shown here, with official downloads and releases planned in the near future.
See [YOLO Vision 2025](https://www.ultralytics.com/events/yolovision) for YOLO26 talks.
