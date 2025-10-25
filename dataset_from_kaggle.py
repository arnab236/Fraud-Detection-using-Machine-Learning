
#If needed to download dataset from Kaggle, then use this script

import kagglehub

# Download latest version
path = kagglehub.dataset_download("amanalisiddiqui/fraud-detection-dataset")

print("Path to dataset files:", path)

# otherwise, you can manually download the dataset from Kaggle and place it in your desired directory.
# Here is the link to the dataset: https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset