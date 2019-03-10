from VTScan import VTScan
Scan = VTScan()
resource = Scan.fileScan(filename = "file_name")
detected = VTScan.MalwareDetect()
for reports in detected:
    for report in reports:
        print(report)
