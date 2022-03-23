# Import the required packages
# ==============================

import json

# read from .env file
from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api

def main():

  # Upload an asset and get its URL
  # ==============================

  resp=cloudinary.uploader.upload("static/black_coat_portrait.jpg")
  srcURL = cloudinary.CloudinaryImage("quickstart/test-asset").build_url()
  print("****Uploaded Asset URL****")
  print(srcURL)
  print("****Upload Response****")
  print(json.dumps(resp,indent=2),"\n")
  
  # Transform the uploaded asset and get its URL
  # ==============================
  new_height=resp["height"]/5
  new_width=resp["width"]/10
  transformedURL = cloudinary.CloudinaryImage("quickstart/test-asset").build_url(width=new_width, height=new_height, radius="max", crop="fill", effect="sepia")
  print("****Transformation URL****")
  print(transformedURL, "\n")
  
  # Add tags to the asset 
  # ==============================  
  if resp["width"]>900:
    update_resp=cloudinary.api.update("quickstart/test-asset", tags = "small")
  elif resp["width"]>500:
    update_resp=cloudinary.api.update("quickstart/test-asset", tags = "medium")
  else:
    update_resp=cloudinary.api.update("quickstart/test-asset", tags = "large")    
  print("****Update response****") 
  print(update_resp["tags"])
  
  # Remove tags
  # ============================== 
  cloudinary.uploader.remove_all_tags("quickstart/test-asset")

main();
