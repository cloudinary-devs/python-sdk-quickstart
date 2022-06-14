# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv
load_dotenv()

# Import the required libraries
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
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

def main():

  # Upload the image and get its URL
  # ==============================

  # Upload the image.
  cloudinary.uploader.upload("https://cloudinary-devs.github.io/cld-docs-assets/assets/images/butterfly.jpeg", public_id="quickstart_butterfly", unique_filename = False,overwrite=True)

  # Build the URL for the image and save it in the variable 'srcURL'.
  srcURL = cloudinary.CloudinaryImage("quickstart_butterfly").build_url()

  print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")

  # Get and use details of the image
  # ==============================

  # Get image details and save it in the variable 'image_info'.
  image_info=cloudinary.api.resource("quickstart_butterfly")
  print("****3. Get and use details of the image****\nUpload response:\n", json.dumps(image_info,indent=2), "\n")

  # Assign tags to the uploaded image based on its width. Save the response to the update in the variable 'update_resp'.
  if image_info["width"]>900:
    update_resp=cloudinary.api.update("quickstart_butterfly", tags = "large")
  elif image_info["width"]>500:
    update_resp=cloudinary.api.update("quickstart_butterfly", tags = "medium")
  else:
    update_resp=cloudinary.api.update("quickstart_butterfly", tags = "small")

  print("New tag: ", update_resp["tags"], "\n")
  
  # Transform the image
  # ==============================

  # Transform the uploaded image and save the generated URL in the variable 'transformedURL'.
  transformedURL = cloudinary.CloudinaryImage("quickstart_butterly").build_url(radius="max", effect="sepia")

  print("****4. Transform the image****\nTransfrmation URL: ", transformedURL, "\n")



main();
