# Hunter Estuary KBA, New South Wales

BirdLife Australia Key Biodiversity Area (KBA) Change Detection Report, September 2003 – September 2023

Prepared for [BirdLife Australia](https://birdlife.org.au/) by [Michael Dear](https://mjdear68.github.io/portfolio/), June 2024

## Objective
To quantify changes in land cover in the Hunter Estuary KBA, NSW for the period Sep 2003 2005 to Sep 2023.

## Method
The study area was developed by applying a 1000 metre exterior buffer to the KBA. A bi-temporal pair of Landsat 8 satellite images based on the mean of two dates in September 2003 and two dates in September 2023 was obtained from [Digital Earth Australia's](https://www.dea.ga.gov.au/) Open Data. Each 30m×30m=900m^2 in the study area was represented by one pixel in the dataset. The dataset included the red, green, blue, near-infrared, shortwave infrared 1, and shortwave infrared 2 bands, plus the NDVI, NBR, and NDWI indices. A classification with the classes No Data, Water, Developed, Green Grass, Brown Grass, Swamp, and Wooded was established. 

Colour-composite and NDVI images were used to develop training and test sets for each of the two dates. Four different classifications for each date were made using supervised machine learning algorithms. The algorithms were random forest (RF) and support vector machine (SVM) with three different kernels (linear, polynomial, and radial basis function (RBF)). The models were trained on 429 samples and tested on 107 samples in each class for each date. This represented an 80:20 split of the candidate sample dataset. A 3x3 sliding window modal filter was applied to the classifications to reduce noise. 

The four classifications were compared visually using QGIS and high-resolution imagery obtained from the [NSW Historical Imagery Viewer](https://portal.spatial.nsw.gov.au/portal/apps/webappviewer/index.html?id=f7c215b873864d44bccddda8075238cb) and Google Earth. It was determined that the SVM with a linear kernel represented the most accurate classification when applied to the whole study area. Post-classification analysis was applied to the classifications for the two dates to establish class change statistics.
 

## Usage
1. Clone the repository to the [Digital Earth Australia (DEA) Sandbox](https://app.sandbox.dea.ga.gov.au/hub/login?next=%2Fhub%2F)
2. (Recommended) Clone the repository locally to perfom the analysis steps.
3. Delete unwanted files from the data sub-directories.
4. Update relevant parameters in the [global_prameters.py](./nbk/global_params.py) file.
5. Save a `.geojson` polygon of the study area to the `data/vector ` directory. The filename should be `[study_area_abbrev].geojson` where `study_area_abbrev` matches the parameter in the `nbk/global_params.py` file.
6. Complete all relevant steps in the [DEA Data Preparation](./nbk/dea_data_prep.ipynb) notebook. Some steps are optional, depending on the objectives of the study.
7. Complete the steps in the [Exploratory Data Analysis](./nbk/eda.ipynb) notebook and review the potential change classes for the study site.
8. Complete relevant steps in the [Class Data Preparation](./nbk/class_data_prep.ipynb) notebook to create any necessary classification variables.
9. Complete the [Post-classification Analysis](./nbk/post_class_analysis.ipynb) notebook.


