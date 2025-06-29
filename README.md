
# 🏗️ 2D Frame Analysis Application (PyQt5 + Python)

This project is a graphical desktop application for performing 2D frame structural analysis. Built with Python and PyQt5, it allows users to define nodes, elements, supports, and loads through a user-friendly interface and computes displacements and internal forces using matrix-based methods.

---

## ✨ Features

- Multi-window GUI with PyQt5
- Node and element input through editable tables
- Structural drawing and visualization
- Displacement and internal force calculations
- Results shown in both table and graphical format
- Structured using the Model–View–Controller (MVC) pattern
- Matrix-based stiffness method implementation (Euler–Bernoulli beams)

---

## 🧱 Project Structure

```
📁 src/
├── main.py                      # Main entry point
├── FrameModelData.py           # Model: Stores structural data
├── FrameSolver.py              # Controller: Solver and logic
├── ShowResults.py              # Controller: Displays results
├── ResultsWindow.py            # View: Results interface
├── MenuWindow.py               # View: Main menu
├── PreFrameProperties.py       # Controller: Initial frame size input
├── PreFramePropertiesWindow.py# View: Initial input window
├── MainFrameProperties.py      # Controller: Main input window logic
├── MainFramePropertiesWindow.py# View: Main input window interface
```

---

## 🛠️ Installation

Ensure you have Python 3.8+ installed. Then install the required packages:

```bash
pip install pyqt5 numpy
```

To run the application:

```bash
python main.py
```

---

## 🧠 Design Approach

This application follows a simplified **Model–View–Controller (MVC)** design:

- **Model**: `FrameModelData.py` holds all structural data and logic for preparing matrices.
- **View**: UI windows created with Qt Designer (e.g., `ResultsWindow`, `MainFramePropertiesWindow`).
- **Controller**: Scripts like `FrameSolver.py` and `PreFrameProperties.py` control the logic and workflow.

The UI was designed using **Qt Designer**, and integrated with Python using **PyQt5**.

---

## 🚀 Future Improvements

- Improve error handling and input validation
- Add support for **Timoshenko beam theory**
- Implement a full **Finite Element Method (FEM)** module
- Improve design pattern consistency
- Enable file export and save/load model features

---

## 📚 References

1. Fitzpatrick, M. (2021). *Create GUI Applications with Python & Qt5*. Independently published.  
2. Summerfield, M. (2008). *Rapid GUI Programming with Python and Qt*. Prentice Hall.  
3. Felippa, C. A. (2004). *Variational Formulation of Beam Elements*. University of Colorado.  

---

## 🧑‍💻 Author

**Çağlar Temiz**  
MSc Student in Structural Engineering in METU

---


