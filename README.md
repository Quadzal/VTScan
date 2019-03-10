# VTScan
VTscan Performs Virus Scan Using the Virustotal Api.

# Example Using:
    from VTScan import VTScan
    Scan = VTScan(file="file_name")
    detected = VTScan.MalwareDetect()
    for reports in detected:
        for report in reports:
            print(report)
        
