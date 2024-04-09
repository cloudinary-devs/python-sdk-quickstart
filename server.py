# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv
load_dotenv()


# Import the Cloudinary libraries
# ==============================
import cloudinary
from cloudinary import CloudinaryImage
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True  
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")



def uploadImage():

  # Upload the image and get its URL
  # ==============================

  # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  cloudinary.uploader.upload("https://cloudinary-devs.github.io/cld-docs-assets/assets/images/butterfly.jpeg", public_id="quickstart_butterfly", unique_filename = False, overwrite=True)

  # Define the transformation separately
  transformation = [
      {"width": 400, "height": 400, "crop": "crop"}
  ]

  # Upload the image with the specified transformation
  result = cloudinary.uploader.upload(
      "https://res.cloudinary.com/demo/image/upload/v1702378721/docs/wines.jpg", 
      public_id="improve",
      transformation=
        [{"width": 400, "height": 400, "crop": "auto", "gravity":"auto", "effect": "improve:50"}]
  )

  # Build the URL for the image and save it in the variable 'srcURL'
  srcURL = CloudinaryImage("quickstart_butterfly").build_url()

  # Log the image URL to the console. 
  # Copy this URL in a browser tab to generate the image on the fly.
  print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")


def getAssetInfo():

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

  # Log the new tag to the console.
  print("New tag: ", update_resp["tags"], "\n")



def createTransformation():

  # Transform the image
  # ==============================

  transformedURL = CloudinaryImage("quickstart_butterfly").build_url(width = 100, height = 150, crop = "fill")

  # Log the URL to the console
  print("****4. Transform the image****\nTransfrmation URL: ", transformedURL, "\n")

  # Use this code instead if you want to create a complete HTML image element:
  # imageTag = cloudinary.CloudinaryImage("quickstart_butterfly").image(radius="max", effect="sepia")
  # print("****4. Transform the image****\nTransfrmation URL: ", imageTag, "\n")

  # Retrieve user's profile image ID from database
  user_profile_image_id = "quickstart_butterfly"

  # Instantiate a CloudinaryImage object with user's profile image ID
  profile_image = CloudinaryImage(user_profile_image_id)

  # Generate URL with custom transformations based on user preferences
  profile_image_url = profile_image.build_url(transformation={'width': 300, 'height': 300, 'crop': 'thumb'})
  print("User Profile Image URL:", profile_image_url)

  # User's preferred asset dimensions retrieved from database
  user_preferred_width = 300
  user_preferred_height = 200

  # Check if user prefers square thumbnails
  if user_preferred_width == user_preferred_height:
      # Generate square thumbnail with crop mode
      dynamic_asset_url, _ = cloudinary.utils.cloudinary_url("sample", transformation={'width': user_preferred_width, 'height': user_preferred_height, 'crop': 'fill'})
  else:
      # Generate rectangular thumbnail without crop
      dynamic_asset_url, _ = cloudinary.utils.cloudinary_url("sample", transformation={'width': user_preferred_width, 'height': user_preferred_height})

  print("Dynamic Asset URL:", dynamic_asset_url)

def main():
  uploadImage()
  getAssetInfo()
  createTransformation()
  
main();

