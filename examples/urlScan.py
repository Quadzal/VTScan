from VTScan import VTScan
Scan = VTScan()
detected = Scan.urlScan(url="https://www.google.com/")
for reports in detected:
    for report in reports:
        print(report)
