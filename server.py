# Import the required packages
# ==============================

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================

import json

# Check your configuration
# ==============================
config = cloudinary.Config()
print(config.cloud_name)
print(config.api_key)

def main():

  # Upload an asset and get its URL
  # ==============================

  # Upload the image.
  cloudinary.uploader.upload("https://res.cloudinary.com/demo/image/upload/v1651575702/docs/sdk/test-asset.jpg", public_id="quickstart_butterfly", unique_filename=False, overwrite=True)

  # Build the URL for the image and save it in the variable 'srcURL'.
  srcURL = cloudinary.CloudinaryImage("quickstart_butterfly").build_url()

  print("****Uploaded Asset URL****\n", srcURL, "\n")
  
  # Get and use details of the image
  # ==============================

  # Get image details and save it in the variable 'image_info'.
  image_info=cloudinary.api.resource("quickstart_butterfly")
  print("****Asset details****\n", json.dumps(image_info,indent=2),"\n")

  # Assign tags to the uploaded image based on its width. Save the response to the update in the variable 'update_resp'.
  if image_info["width"]>900:
    update_resp=cloudinary.api.update("quickstart_butterfly", tags = "large")
  elif image_info["width"]>500:
    update_resp=cloudinary.api.update("quickstart_butterfly", tags = "medium")
  else:
    update_resp=cloudinary.api.update("quickstart_butterfly", tags = "small")
  
  print("****Tags****\n", update_resp["tags"])

  
  # Transform the image
  # ==============================
  
  # Transform the uploaded asset and save the generated URL in the variable 'transformedURL'.
  transformedURL = cloudinary.CloudinaryImage("quickstart_butterfly").build_url(radius="max", effect="sepia")

  print("****Transformation URL****\n", transformedURL, "\n")


main();
