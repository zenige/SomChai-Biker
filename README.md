<H1>HOW TO RUN</H1>

1. install your environment 

2. run this command -> pip install -r requirements.txt  // for installing all of dependencies

3. run 

```python detect.py  <<trainmodel.pd>> --img 640 --conf <<min_conf>> --source <<filename>> ```


- traninmode // if you would like to use your custom model you be able to push --weights modelname.pd to run script if 
in case you need to use Somchai model leave a method

- min_conf // the minimum confident that will detect on your model

- filename //name of your input file our script accept 3 types 1. image  2.video 3.device type 0 in filename to use webcam

<H1>More Argument</H1>

   '--weights', nargs='+', type=str, default=somchaimodel.pt', help='model.pt path(s)')

   '--source', type=str, default='data/images', help='source')  # file/folder, 0 for webcam

   '--img-size', type=int, default=640, help='inference size (pixels)')

   '--conf-thres', type=float, default=0.25, help='object confidence threshold')

   '--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')

   '--max-det', type=int, default=1000, help='maximum number of detections per image')

   '--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')

   '--view-img', action='store_true', help='display results')

   '--save-txt', action='store_true', help='save results to *.txt')

   '--save-conf', action='store_true', help='save confidences in --save-txt labels')

   '--save-crop', action='store_true', help='save cropped prediction boxes')

   '--nosave', action='store_true', help='do not save images/videos')

   '--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')

   '--agnostic-nms', action='store_true', help='class-agnostic NMS')

   '--augment', action='store_true', help='augmented inference')

   '--update', action='store_true', help='update all models')

   '--project', default='runs/detect', help='save results to project/name')

   '--name', default='exp', help='save results to project/name')

   '--exist-ok', action='store_true', help='existing project/name ok, do not increment')

   '--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')

   '--hide-labels', default=False, action='store_true', help='hide labels')

   '--hide-conf', default=False, action='store_true', help='hide confidences')


<br>
<br>
<br>
<H1> -----optional---- </H1>

<h3>Custom Data</h3>
<br>
<H3> 1.Create dataset.yaml </H3>

 train and val data as 1) directory: path/images/, 2) file: path/images.txt, or 3) list: [path1/images/, path2/images/]


```bash 
train: ../ML/images/train2017/
val: ../ML/images/train2017/

# number of classes
nc:2

# class names
names: [ 'motor_helmet','motor_nohelmet' ] 
```


<H3>2. Create Labels</H3>
<br>
After using a tool like CVAT, makesense.ai or Labelbox to label your images, export your labels to YOLO format, with one *.txt file per image (if no objects in image, no *.txt file is required). The *.txt file specifications are:


- One row per object
- Each row is class x_center y_center width height format.
- Box coordinates must be in normalized xywh format (from 0 - 1). If your boxes are in pixels, divide x_center and width by image width, and y_center and height by image height.
- Class numbers are zero-indexed (start from 0).
<br>
<br>
<H3>3. Select a Model </H3>
<br>
YoloV5 has 4 custom model

<img src="https://user-images.githubusercontent.com/26833433/103595982-ab986000-4eb1-11eb-8c57-4726261b0a88.png">
the smallest and fastest model available. See our README table for a full comparison of all models.
<br>
<br>

<h3> 4.Train </h3>

<br>

```python train.py --img 640 --batch 16 --epochs 5 --data <<custom_data.yaml>> --weights yolov5s.pt```


All training results are saved to runs/train/ with incrementing run directories, i.e. runs/train/exp2, runs/train/exp3



