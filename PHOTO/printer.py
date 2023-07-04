import cups

def printing(PATH_TO_IMG, q):
    # Create a connection to the CUPS server
    print(PATH_TO_IMG, type(PATH_TO_IMG))
    
    for i in range(q):
        conn = cups.Connection()

        # Get the list of available printers
        printers = conn.getPrinters()

        # Select a printer
        printer_name = 'Canon_SELPHY_CP1500_2'
        printer_info = printers[printer_name]

        # Print a PNG filea
        file_path = PATH_TO_IMG
        job_id = conn.printFile(printer_name, file_path, "Print Job", {})
        print("Print job submitted with ID:", job_id)
