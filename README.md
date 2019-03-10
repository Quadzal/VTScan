# VTScan
VTscan Performs Virus Scan Using the Virustotal Api.

# Example fileScan:
    from VTScan import VTScan
    Scan = VTScan()
    resource = Scan.fileScan(filename = "file_name")
    detected = VTScan.MalwareDetect()
    for reports in detected:
        for report in reports:
            print(report)
            
# Example zipScan:
    from VTScan import VTScan
    Scan = VTScan()
    resource = Scan.zipScan(zipname = "zip_name")
    detected = Scan.MalwareDetect()
    for reports in detected:
        for report in reports:
            print(report)

# Example urlScan:
    from VTScan import VTScan
    Scan = VTScan()
    detected = Scan.urlScan(url="https://www.google.com/")
    for reports in detected:
        for report in reports:
            print(report)
