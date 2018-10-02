# Machine-Learning-For-Riemann-Zeta-Function

In this study, we applied machine learning to approximation of the non-trivial zeros of the Riemann-Zeta function.
In particular, we explored the replicative and predictive accuracies of SVR, Multilayer Perceptron and Recurrent
Neural Networks, and established their optimal architectures. The input space used by our models consists of 99,000
observations for the 50 different features, which were selected with Random Forest, and mRMR input selection algorithms.
We found that in the framework of this study, Recurrent Neural Networks outperformed both SVR and MLP based on R-squared
and RMSE error metrics. Predictions produced by this model are typically within 0.01 of the true target values.

This github project contains the main report of this study (Predicting Zeros of the Riemann Zeta Function Using Machine 
Learning), the description of our custom algorithm that facilitated computation of Gram and co-Gram points ( 
predictions 


This project is a result of the Research Experience for Undergraduates program of the San Diego State University.
