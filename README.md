# steg-detect-tool

## 📝 Project Description

* StegDetect is a lightweight digital forensics tool designed to detect and extract hidden messages embedded within digital images using the Least Significant Bit (LSB) technique. This project demonstrates image-based steganography and forensic investigation techniques for uncovering concealed information in multimedia files. The system analyzes image pixel bit patterns to identify randomness within the LSBs, indicating steganographic manipulation. Once detected, the tool extracts and decodes hidden content accurately for forensic examination.

## ⚙️ Features

* Detects steganography content with near-perfect accuracy on LSB-based samples.
* Supports channel-specific analysis (R, G, B).
* Allows extraction of embedded messages without knowing content format.
* Modular Python code — easy to extend and integrate.
* Includes a GUI (optional Tkinter) for non-technical users.

## 📂 System Architecture / Workflow

```bash
[Input Image]
       │
       ▼
[LSB Analysis Module]
       │
   Suspicion Score
       │
       ▼
[Extraction Module]
       │
   Binary Stream
       │
       ▼
[Decoded Message Output]
```

## 🛠️ Installation Steps and 
## 🚀 How to Run the Project

## Clone the Repository:

* Download or clone the project folder:
```bash
git clone https://github.com/yourusername/stegdetect.git
```
* Navigate to the Project Folder:
```bash
cd stegdetect
```
* Install python:
* Make sure Python 3.9 or higher is installed:
```bash
python3 --version
```
* If not installed, download it from:
```bash
https://www.python.org/downloads
```

* Create Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```
* Install Dependencies:
* Install required Python packages:
```bash
pip install -r requirements.txt
```
* Manually:
```bash
pip install Pillow numpy
```
* Run Detection:
```bash
python3 extract_lsb.py data/samples/stego_1lsb_blue_unknown.png --bits 1 --channel b --out outputs/extracted.bin
```
* Then view:
```bash
python3 verify_extraction.py
```
## 💡 Technologies Used

* Python 3.9+
* Pillow (PIL)
* NumPy
* Tkinter (optional), Matplotlib (optional)
* macOS Terminal / Windows CMD
* VS Code or Jupyter Notebook
  
## 📜 License

* This project is open-source and available under the MIT License.
