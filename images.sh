cd examples
python grid.py
snapshot grid.html
mv output.png ../images/demo.png
python bar.py
mv snapshot.png ../images/snapshot.png
snapshot render.html pdf
mv output.pdf snapshot.pdf
