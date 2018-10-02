# Machine-Learning-For-Riemann-Zeta-Function

In this study, we applied machine learning to approximation of the non-trivial zeros of the Riemann-Zeta function.
In particular, we explored the replicative and predictive accuracies of SVR, Multilayer Perceptron and Recurrent
Neural Networks, and established their optimal architectures. The input space used by our models consists of 99,000
observations for the 50 different features, which were selected with Random Forest, and mRMR input selection algorithms.
We found that in the framework of this study, Recurrent Neural Networks outperformed both SVR and MLP based on R-squared
and RMSE error metrics. Predictions produced by this model are typically within 0.01 of the true target values.

This github project contains the main report of this study (Predicting Zeros of the Riemann Zeta Function Using Machine 
Learning), a custom Python program that facilitated computations of Gram and co-Gram points (GramPoints.py), and the description of this algorithm (GramPoints.py Annotation). Finally, NeuralNetworks.R provides the R code for MLP and RNN
neural network models that employed in this study.

This study was completed by Jennifer Kampe and Artem Vysogorets at the Research Experience for Undergraduates program
hosted by the San Diego State University. We extend our gratitude to our mentor, Dr. Huan Qin, and the program director, 
Vadim Ponomarenko. We thank San Diego State University for the provided facilities, and National Science Foundation for funding.
