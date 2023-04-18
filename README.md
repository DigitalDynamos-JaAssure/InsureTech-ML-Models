# InsureTech-ML MODELS
Used for extracting details from RC and Insurance Estimate(Trained Prebuilt OCR Model)
<h5> We have used MINDEE which is an open Source RESTFUL API that is used to extract <b> Required Objects from a document<b><br>
  We are extracting details the details like Car color, Chasis Number, Model , Owner, Reg Date from the RC</h5>
<br>
<br>
<h4> We started working with Car Damage detection but since everyone was working on it, we switched to pipes damage detection for industrial track. The model was initiated using YoloV5 Object Detection but then shifted to FAIR's Detectron2 model for instance Segmentation.</h4>

We have created two datasets one far which was scraped over the web and for the other we have trained a custom trained model on RoboFlow which has more than 1100 images for pipes and about 600 images for Car dataset with several classes for both.

