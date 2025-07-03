# 🎯 Augmented Reality Project

> 🧠 A Computer Vision journey into projecting a 3D cube onto reality using calibration, homography, and tracking. Built with MATLAB 🧪📐

## 👨‍🎓 Project Info

📚 **Course**: MU4RBI09 – Vision par Ordinateur  
👨‍🏫 **Instructor**: Xavier Clady  
🧑‍💻 **Team**:  
- Leo Bellali – M1 ISI | CMI EEA  
- Edouard David – M1 ISI | CMI EEA

---

## ✨ What It Does

🔧 This project brings a **virtual 3D cube** into real-world scenes by:

- 📷 Calibrating a camera  
- 🔲 Calculating a homography  
- 📐 Estimating camera pose  
- 🧊 Projecting a cube onto 2D images  
- 🎯 Tracking points across frames  
- 🎬 Augmenting a full video with the 3D object

All steps are implemented in **MATLAB**.

---

## 🧪 How It Works

### 🔍 1. Camera Calibration
- Used a checkerboard pattern 🏁.
- Took 20 images from various angles 📸.
- Processed with MATLAB's **Camera Calibrator** app to get matrix **K**.

### 🔁 2. Homography Estimation
- Extracted corresponding points between pattern and image 🧩.
- Applied **DLT algorithm** with proper normalization 💡.
- Built the homography matrix **H** to transform image planes.

### 🧭 3. Pose Estimation
- Combined **K** and **H** to compute [**R | T**] 🤖.
- Built the projection matrix **P = K [R|T]**.
- Ensured physical plausibility (e.g., det(R) = 1).

### 🧊 4. 3D Cube Projection
- Defined cube points in 3D space 🧊.
- Projected onto 2D using **P** and plotted in MATLAB.
- Visualized the cube correctly over the pattern 🎨.

### 🕵️ 5. Feature Tracking
- Tried MinEig (Lucas-Kanade) ➡️ Switched to **KAZE** features ⚡.
- Improved tracking with 4-dot circular pattern 🎯.
- Exported tracked coordinates to augment across video frames 🎞️.

---

## ▶️ Getting Started

### ✅ Prerequisites
- MATLAB with Computer Vision Toolbox
- Your own camera or test video (see below)

### 🚀 Run the Project
1. Calibrate your camera with MATLAB’s Calibrator 🛠️.
3. Run the following files:
   - `Homography.mlx` – computes calibration, homography, and projection matrix.
   - `Augmented_REALITY.m` – selects points & displays cube.
   - `ProjectionMatrixVideo.mlx` – projects cube across video frames.

---

## 📷 Example Output

Here's what you'll see:

📦 ➡️ 🖼️  
A 3D cube projected in correct perspective onto a flat 2D scene!

---

## 📚 References

- 📘 *Multiple View Geometry in Computer Vision* – Hartley & Zisserman  
- 📎 [Laval Virtual – AR Maintenance Platform](https://blog.laval-virtual.com/la-premiere-plateforme-de-maintenance-en-realite-augmentee/)  
- 📰 [eMarketing – Potentiel de la Réalité Augmentée](https://www.e-marketing.fr/Thematique/cross-canal-1094/Breves/Comment-exploiter-potentiel-realite-augmentee-343772.htm)  
- 📎 [Sténopé Explanation – Wikipedia](https://fr.wikipedia.org/wiki/St%C3%A9nop%C3%A9)

---

## ✅ Achievements

✔️ Camera calibration complete  
✔️ Homography & projection matrix implemented  
✔️ Point tracking via KAZE  
✔️ Cube projection works in images & video frames

---

## ⚠️ Limitations

❌ Final video rendering not fully polished due to time constraints  
⚠️ Tracker sensitivity to image distance or compression

---

> *“Computer Vision is the process of discovering from images what is present in the world, and where it is.”*  
> — 🧠 **David Marr**

---

🛠️ Made with code, curiosity, and coffee ☕  
