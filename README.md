<div align="center">

# Emoji Prediction from Twitter Data using Deep Learning Approach

![GitHub last commit](https://img.shields.io/github/last-commit/Defcon27/Emoji-Prediction-using-Deep-Learning?label=Last%20commit&color=green&logo=git&logoColor=white&style=flat)
![GitHub stars](https://img.shields.io/github/stars/Defcon27/Emoji-Prediction-using-Deep-Learning?label=Stars&logo=github&style=flat)
![Github forks](https://img.shields.io/github/forks/Defcon27/Emoji-Prediction-using-Deep-Learning?label=Forks&logo=github&style=flat)
![GitHub issues](https://img.shields.io/github/issues/Defcon27/Emoji-Prediction-using-Deep-Learning?label=Issues&color=yellow&logo=github&style=flat)
</div>


## 📌Introduction

<h4 align="justify" ><i>Emojis are a small visual representation of emotions or objects that are usually used in text messages to enhance the communication experience between individuals.</i> This project aims to understand the underlying semantics of the text sentence using natural processing techniques to predict reasonable emojis based on the context. With the rise in the widespread use of social media platforms like Twitter and instant messaging, many users are using these emojis in their text messages to convey broad feelings efficiently, which sometimes cannot be expressed using just words. Thus, giving rise to a problem statement that is to identify the relationship between these text messages and the emojis used in them. This project aims to understand the underlying semantics of the text sentence using natural processing techniques to predict reasonable emojis based on the context.
</h4>
<p><br></p>


## 🗃️Dataset
<p align="justify">
The twitter emoji dataset obtained from CodaLab comprises of 50 thousand tweets along with the associated emoji label. Each tweet in the dataset has a corresponding numerical label which maps to a specific emoji. The emojis are of the 20 most frequent emojis and hence the labels range from 0 to 19. Initial dataset in raw text format is later written to a csv file using python scripts.</p>

Get the data [here](https://github.com/fvancesco/Semeval2018-Task2-Emoji-Detection)!

<p><br></p>


## Deep Learning Model Architecture
<p align="middle"> <img src='Docs/DL_LSTM.png' width=75%/></p>
<p align="justify">
The proposed architecture consists of Embedding layer followed by the Bidirectional LSTMs layer, then a layer of dense hidden layer which passes of its activations to a SoftMax activation function which outputs the final prediction scores. First the sequences that were created from the text data are passed batch wise to the neural network. These sequences are passed to an Embedding layer, here for each number in the sequence, vector of constant length is computed which will be adjusted while training. These embedding vectors are created to create similarity among related word. Meaning that words which are highly related, after computation will have vectors with high similarity. After the embedding layer, the vectors computed are passed to a layer of Bidirectional LSTMs which have the capability to store information in their memory. These cells encapsulate contextual information while training in their long-term and short-term memory, which are updated continuously while training. The output from the LSTMs layer is then passed to a dense layer, which basically contain neurons with Rectified Linear activation function (ReLU). The activation scores from these cells is then passed to another layer of neuron. Here the activation of these neurons will be Softmax function. Softmax function takes the activation of all the previous neurons and outputs a distribution of probabilities whose sum equals to one. A probability for each class will be predicted as the final output of the model. The class with highest probability among them can be chosen as the predicted class.
</p>
<p><br></p>


## Conclusion
<p align="justify">
In this paper, the results discussed above we can conclude that Support Vector Classifier model performed marginally better suggesting that this improvement in performance could be attributed to the fact that the SVM algorithm might have been able to draw out some relationships in the data than that of the probabilistic Naive Bayes model. These kinds of results obtained from machine learning models is due to the fact that the available data that is being used for training the model is not generalizable enough. Also, another drawback is that, some emojis overweight the count of other making the model to bias itself into predicting that emoji more often. Furthermore, from the confusion matrix, it is pretty clear that, the model is biased towards weights rather than the context of text which shows that the model has a low understanding of the semantic relationship between the sentence and the emoji. Thus, we have proposed and implemented a Deep Learning approach using Bidirectional LSTMs for predicting emojis based on the input text tweet. This approach yielded the optimal results than all the base machine models.
</p>
<p><br></p>


## References
[1] Barbieri Francesco et al., "Semeva12018 task 2: Multilingual emoji prediction", Proceedings of The 12th International Workshop on Semantic Evaluation, 2018.

[2] Barbieri Francesco, Luis Espinosa-Anke and Horacio Saggion, "Re-vealing patterns of Twitter emoji usage in Barcelona and Madrid", Frontiers in Artificial Intelligence and Applications. 2016; (Artificial Intelligence Research and Development), vol. 288, pp. 239-44, 2016.

[3] Barbieri, Francesco & Ballesteros, Miguel & Saggion, Horacio. (2017). Are Emojis Predictable?. 105-111. 10.18653/v1/E17-2017. 


<p><br></p>


### License
Copyright © 2021 Hemanth Kollipara, Pavithra Kollipara

