Welcome to the NSA Professional Services GitHub repository.
This script is a sample script that reads a __Sync.PurchaseOrder__ BOD and creates an IDM search item API request in json format.

## Feel free to use and modify the script to suit your needs
***

Also included is an ION Script that you can import into your own ION desk scripting application.

## Commands

* `python createRequest.py` - Create the API request.

## Project layout

    docs/
        mkdocs.yml                # The configuration file.
        docs/
            index.md              # The documentation homepage.
            ...                   # Other markdown pages, images and other files.
        createRequest.py          # Python classes to build the IDM API request 
        Sync.PurchaseOrder.xml    # Sample Sync.PurchaseOrder BOD
        TUG_2022_GetPONo.json     # Script that can be imported into ION Desk / Scripting

## Setup

1. If you don't already have Python installed, you will need to download and install python from [Python.org](https://www.python.org/downloads/) 
2. You can use the included __Sync.PurchaseOrder.xml__ to test it out.
3. If you choose to use a different BOD, you will want to download a new BOD to the same directory as the script
4. Change the following line in the script to reflect the name of the new file:  
5. Update the __poNo__ variable to search the correct path in the new BOD

### Code (Change the BOD name)   
    def getPO(): with open("Sync.PurchaseOrder.xml") as INPUT:  
***

### The request payload that is generated can be used for an __IDM "Items" POST request.__

__It is valid for the followig endpoints:__

    * /items/count  
    * /items/search  
    * /items/search/item/resource  
    * /items/search/item/resource/stream  
    * /items/search/item/resource/{conversion}  
    * /items/search/item/resource/{conversion}/stream  

You will also want to change the following values so that your payload is valid when requesting a document from IDM.

`entity = "Purchase_Order" `         

`keyattr = "Order_Number" `          

`operator = "="  `                   

`textSearch = False   `              

 __You can create another function in the DataInput class or reuse the existing function and change the search node__

`DataInput.getPO() `      

__Optional__

`logicalType = "" `                  

After you are done editing the script you can run it as usual to get the json output payload:

![image](https://user-images.githubusercontent.com/15594519/161635696-da937c17-5db8-4fef-9b2d-855af260b5f1.png)

Feel free to try it out, change it suit your needs or add it to a project of your own.



