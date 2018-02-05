cd examples
python demo.py
mv demo.png ../images/demo.png
python grid.py
snapshot grid.html
python bar.py
mv snapshot.png ../images/snapshot.png
python pdf.py
snapshot render.html pdf 5
mv output.pdf snapshot_in_pdf.pdf
