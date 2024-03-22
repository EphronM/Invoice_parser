


input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

# Define buttons and their corresponding queries
button_queries = {
    "Items List": "what are the items mentioned in this invoice? give me the answers in list of points",
    "Vendor Name": "what is the vendor name?",
    "Vendor Address": "what is the vendor address",
    "Item Quantity": "what is the quantity of each item? give me the answers in points",
    "Unit price": "what are the unit prices ? give me the answer in points",
    "Sub total": "what is the subtotal amount?",
    "Total Tax": "what is the total tax amount?",
}


def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")