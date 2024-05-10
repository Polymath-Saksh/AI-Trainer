# Vision-Personal-Trainer [![License: MIT][License-Badge]](LICENSE.md)  [![Made with Python][Python-Badge]](https://www.python.org/)

## Description

This project is a personal trainer that will help you to do exercises at home. It will show you how to do the exercises and will count the repetitions you do. It makes use of computer vision to detect the human body and the movements you do. The script uses the `mediapipe` library to detect the human body landmarks and calculate the number of repetitions based on the movements.

## Installation

- Clone the repository

    ```bash
    git clone https://github.com/Polymath-Saksh/Vision-Personal-Trainer.git
    ```

- Install the required libraries

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- Choose the points you want to track in the `main.py` file. You can choose from the following points:

    ```python
    points_pair_list = {
        "right_arm": [12, 14, 16],
        "left_arm": [11, 13, 15],
        "right_leg": [24, 26, 28],
        "left_leg": [23, 25, 27],
        "torso": [11, 12, 24],
        "neck": [11, 12, 23],
        "right_shoulder": [12, 24, 26],
        "left_shoulder": [11, 23, 25],
        "right_hip": [24, 26, 28],
        "left_hip": [23, 25, 27],
        "right_knee": [26, 28, 30],
        "left_knee": [25, 27, 29]
    }
    ```

- Then accordingly, modify the line 20 in the [main.py](main.py) file, with your choice of points. For example, if you want to track the right arm, you can modify the line as follows:

    ```python
    angle = detector.findAngle(img, 12, 14, 16,pts = True, lines= True)
    ```

- Run the script

    ```bash
    python main.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Mediapipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)

[License-Badge]: https://img.shields.io/badge/License-MIT-blue.svg

[Python-Badge]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
