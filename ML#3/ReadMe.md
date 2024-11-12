[App](https://huggingface.co/spaces/valeralerleb/Predict_DW)

A docker was deployed in the space, Gunicorn (Application server for running web applications) was launched in it.
Next, main.py is launched in the container with the libraries:
- flask (a framework for creating web applications)
- Catboost
- Pandas, Numpy
- Pickle (for loading/saving ML models in code)
  
The file uses two pre-trained models downloaded from the notebook to predict the width and depth of the seam.
flask, in turn, uses html, in which forms for filling in and visualizing the results are created.
main.py takes all the incoming parameters (features) from the form, predicts two targets based on them and outputs them to the form.
