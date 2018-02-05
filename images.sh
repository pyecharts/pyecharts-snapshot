cd examples
python grid.py
snapshot grid.html
mv output.png ../images/demo.png
python bar.py
mv snapshot.png ../images/snapshot.png
python pdf.py
snapshot render.html pdf 5
mv output.pdf snapshot_in_pdf.pdf
