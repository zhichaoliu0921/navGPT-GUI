# NavGPT 
---

## How to Run
- `python>=3.8`
- `pip install ultralytics==8.0.48`
- `pip install pyside6==6.4.2`
- `python main.py`


## Notice
- `ultralytics` follows the `GPL-3.0`, if you need commercial use, you need to obtain its license.
- If you expect to use your own model, you need to use `ultralytics` to train the yolov8/5 model first, and then put the trained `.pt` file into the `models` folder.
- There are still some bugs in the software, and I will continue to optimize and add some more interesting functions as my time allows.
- If you check the save results, they will be saved in the `./run` path
- The UI design file is `home.ui`, if you modify it, you need to use the `pyside6-uic home.ui > ui/home.py` command to regenerate the `.py` file
- The resource file is `resources.qrc`, if you modify the default icon, you need to use the `pyside6-rcc resoures.qrc > ui/resources_rc.py` command to regenerate the `.py` file


## References

- [YoloSide](https://github.com/Jai-wei/YOLOv8-PySide6-GUI.git)
- [ultralytics](https://github.com/ultralytics/ultralytics)
