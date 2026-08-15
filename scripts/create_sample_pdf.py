from reportlab.pdfgen import canvas

output = "sample_data/firewall_operations.pdf"

pdf = canvas.Canvas(output)

# Page 1
pdf.setFont("Helvetica", 16)
pdf.drawString(72, 750, "Firewall Operations Runbook")

pdf.setFont("Helvetica", 11)
pdf.drawString(72, 720, "Change implementation procedure")
pdf.drawString(72, 690, "1. Verify that the firewall service request is approved.")
pdf.drawString(72, 670, "2. Validate the source and destination network details.")
pdf.drawString(72, 650, "3. Confirm the requested ports and protocols.")
pdf.showPage()

# Page 2 - intentionally empty
pdf.showPage()

# Page 3
pdf.setFont("Helvetica", 16)
pdf.drawString(72, 750, "Firewall Troubleshooting")

pdf.setFont("Helvetica", 11)
pdf.drawString(72, 720, "Check the following when connectivity fails.")
pdf.drawString(72, 690, "1. Verify the firewall policy.")
pdf.drawString(72, 670, "2. Check traffic logs.")
pdf.drawString(72, 650, "3. Verify routing and return traffic.")
pdf.drawString(72, 630, "4. Confirm that recent changes did not introduce the issue.")

pdf.save()