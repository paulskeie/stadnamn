# stadnamn
Character level self-supervised model to generate Norwegian place names

## Here are some examples of output from the model.

|        |          |          |          | Vestr    | Østre
-------- | -------- | -------- | -------- | -------- | --------
Fortenvika | Storfjellet | Hestberget | Salponøyvågen | Vestre Kjollen | Østren
Koløya | Gravdådalen | Sørhaugen | Tømmelibrua | Vestrane | Østre Varde
Sneveaflua | Sørneebotn | Flaten | Hårheim | Vestre Grønnholmen | Østre Kvernhaugen
Vagemyrhaugen | Orrerdalen | Vifjellskjærberget | Stormoen | Vestre Ganegrunnanturveg | Østre Sag
Steina | Medagen | Har-buholmen | Risa | Vestre nortelveien | Østrendgurd
Osen | Husvatnet | Nybakken | Nysnø | Vestre Haugen | Østre Øvrengetan
Borgita | Svartbakken | Heithaugen | Skáiuhelelen | Vestre Støle | Østredalskjær
Øvre høgda | Mábbetn, bua | Storengard | Steindalsheia | Vestre Fryvassbruneset | Østre Løkstad
Merkskardet | Skrud | Stordre Lodgegjer tøm | Storoialva | Vestre Hifjell | Østre Veslen
Gvapeskádjávri | Beiseberget | Austre Reaneset | Haugen | Vestre Sørestøya | Østredal

## Data

Data is downloaded from [Geonorge](https://www.geonorge.no). 


1. Search for "stedsnavn" in the data catalogue.
2. Download
3. Unzip
4. Extract the place names into csv using your favourite xml parser or use the code below or run `bash extract.sh` if on a mac or linux system

```
grep app:langnavn Basisdata_0000_Norge_25833_Stedsnavn_GML.gml |cut -d ">" -f 2|cut -d "<" -f 1 > stadnamn.csv
```

Have a look in the Jupyter notebook stadnamn for more details. However, stadnamn.csv was added to the repo for convenience.

## Training in colab, deploying to Azure

The model was trained for free using [colab](https://colab.research.google.com/) and data was persisted to Google Disk.

For now the repo contains code to deploy to Azure. If you want to do this yourself, sign up for Azure and create a machine learning Workspace and download config.json that allows you to instanciate the Workspace class.
The model must be registered to AzureML, see how to in register_model_azure.py.
See how to deploy to your local machine in deploy_azure.py. The model can be deployed to an ACI or kubernetes using a few additional lines of code.

To try the API there is a consume_azure.py that hits the api n times with a few different seeds and that outputs the results to a markdown table.

## Sampling strategy

Currently there are two sampling methods, a standard sampling method the always picks the most probable next character.
This method will have low entropy, little fantasy, and can get stuck in repeatable patterns.
The other is a temperature sampling method that does multinomial sampling and where you can set the degree of entropy using a temperature parameter. The table with place names at the top was produced setting samplingmethod to temperature and the temperature to 1.0.
