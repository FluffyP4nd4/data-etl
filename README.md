# Get File List
## Clone repo and install requirements
```
git clone https://github.com/FluffyP4nd4/data-etl.git
cd data-etl
pip install -r requirements.txt
```
## For labelme folder
```
python get_img.py --path '/content/drive/Shareddrives/Ficha/Tech/Annotation/Truck_project/Annotated ones' --dest /content/labelme/
```
## For coco

```
python get_img.py --path '/content/drive/MyDrive/s/annotations/all_data_fixed.json' --coco True --dest /content/coco/
```

## Getting for Specific classes
```
python get_img.py --path ' ' --classes 1 2 3 4 5 6 7 8 9 # based on requirements
```

## Classes id to name
```
  0:'big cardboard',
  1:'bulky',
  2:'compactor',
  3:'dumpster',
  4:'electrical and electronic waste',
  5:'garbage bag',
  6:'glass',
  7:'green waste',
  8:'hygiene',
  9:'plastic bag',
  10:'recycle waste',
  11:'textile',
  12:'cylinders',
  13:'bag'
```
