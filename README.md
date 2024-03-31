
# Invoice Parsing using Gemini Vision Pro API

## Try it out

**[APP Link](http://13.201.88.76/)**


![image](https://github.com/EphronM/Invoice_parser/assets/94764266/a79138ac-93af-4de2-a50f-624bef510668)

## Overview
This project aims to facilitate the extraction of relevant information from invoices using the Gemini Vision Pro API. It provides a convenient interface to parse invoices, extracting important details such as vendor name, items list, quantities, unit prices, subtotal, and total tax. The project utilizes the capabilities of the Gemini Vision Pro API for image processing and text recognition.


## Installation
To run this project, follow these steps:

* Clone the repository from GitHub:

```
git clone https://github.com/EphronM/Invoice_parser.git
```

* Install the required dependencies:

```
pip install -r requirements.txt
```

* Set up Gemini Vision Pro API credentials | [documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini) . Create a **.env** file in the root directory of the project and add your API key. Gemini Vision Pro 

```
GOOGLE_API_KEY=<your-api-key>
```

* Run the Streamlit application:
```
streamlit run app.py
```

## Usage
* Once the Streamlit application is running, upload the image of the invoice using the provided interface.

* Use the predefined buttons to extract specific information from the invoice.

* You can also ask custom queries based on the information you want to extract

* The extracted data will be displayed on the Streamlit app interface.

The project provides predefined buttons with corresponding queries for extracting specific information from invoices

![image](https://github.com/EphronM/Invoice_parser/assets/94764266/cc4614d7-8a29-4421-bc72-c0b678454723)

Fin.