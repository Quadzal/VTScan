from VTScan import VTScan
Scan = VTScan()
resource = Scan.zipScan(zipname = "zip_name")
detected = Scan.MalwareDetect()
for reports in detected:
    for report in reports:
        print(report)
